from .base import BaseAPI

class Server(BaseAPI):
	"""
	Object representation of UpCloud Server instance.

	Partially immutable class; only fields that are persisted with .save() may be set with the server.field = value syntax.
	See __setattr__ override. Any field can still be set with object.__setattr__(self, field, val) syntax.
	"""

	updateable_fields = [ 	"boot_order", "core_number", "firewall", "hostname", "memory_amount",
							"nic_model", "title", "timezone", "video_model", "vnc", "vnc_password" ]

	post_fields = []


	def __init__(self, *initial_data, **kwargs):
		object.__setattr__(self, "populated", False)
		self._reset(*initial_data, **kwargs)

		if not hasattr(self, "title"):
			self.title = self.hostname

	def __setattr__(self, name, value):
		"""
		Override to prevent updating readonly fields.
		"""
		if name not in self.updateable_fields:
			raise Exception( "'" + str(name) + "' is a readonly field")
		else:
			object.__setattr__(self, name, value)

	def _reset(self, *initial_data, **kwargs):
		"""
		Reset all given attributes.
		May also be given
		"""
		for dictionary in initial_data:
			for key in dictionary:
				object.__setattr__(self, key, dictionary[key])

		for key in kwargs:
			object.__setattr__(self, key, kwargs[key])

	def populate(self):
		"""
		Sync changes from the API to the local object.
		Note: syncs ip_addresses and storage_devices too (/server/uuid endpoint)
		"""
		server, IP_addresses, storages = self.cloud_manager.get_server_data(self.uuid)
		self._reset( server,
					ip_addresses = IP_addresses,
					storage_devices = storages,
					populated = True)
		return self

	def save(self):
		"""
		Sync local changes in server's attributes to the API.

		Note: DOES NOT sync IP_addresses and storage_devices,
		use add_IP, add_storage, remove_IP, remove_storage instead.
		"""
		kwargs = {}
		for field in self.updateable_fields:
			kwargs[field] = getattr(self, field)

		self.cloud_manager.modify_server(self.uuid, **kwargs)
		self._reset(kwargs)

	def destroy(self):
		self.cloud_manager.delete_server(self.uuid)

	def shutdown(self):
		"""
		Shutdown/stop the server. Issue a soft shutdown with a timeout of 30s.
		After the a timeout a hard shutdown is performed if the server has not stopped.

		Note: API responds immediately (unlike in start), with state: started.
		This client will, however, set state as "maintenance" to signal that the server is neither started nor stopped.
		"""
		body = dict()
		body["stop_server"] = {
			"stop_type" : "soft",
 			"timeout" : "30"
		}
		self.cloud_manager.post_request("/server/" + self.uuid + "/stop" , body)
		object.__setattr__(self, "state", "maintenance") # post_request already handles any errors from API


	def stop(self):
		"""
		Alias for shutdow.
		"""
		self.shutdown()

	def start(self):
		"""
		Starts the server. Note: slow and blocking request.
		The API waits for confirmation from UpCloud's IaaS backend before responding.
		"""
		res = self.cloud_manager.post_request("/server/" + self.uuid + "/start")
		object.__setattr__(self, "state", "started") # post_request already handles any errors from API

	def restart(self):
		"""
		Restart the server. Issue a soft restart with a timeout of 30s.
		After the a timeout a hard restart is performed if the server has not stopped.

		Note: API responds immediately (unlike in start), with state: started.
		This client will, however, set state as "maintenance" to signal that the server is neither started nor stopped.
		"""
		body = dict()
		body["restart_server"] = {
			"stop_type" : "soft",
 			"timeout" : "30",
 			"timeout_action" : "destroy"
		}
		self.cloud_manager.post_request("/server/" + self.uuid + "/restart" , body)
		object.__setattr__(self, "state", "maintenance") # post_request already handles any errors from API

	def add_IP(self, family="IPv4"):
		"""
		Allocate a new (random) IP-address to the Server.
		"""
		IP = self.cloud_manager.attach_IP(self.uuid, family)
		self.ip_addresses.append(IP)
		return IP

	def remove_IP(self, IP_address):
		"""
		Release the specified IP-address from the server.
		"""
		self.cloud_manager.release_IP(IP_address.address)
		self.ip_addresses.remove(IP_address)


	def add_storage(self, Storage=None, type="disk", address=None):
		"""
		To add a Storage instance to a server: add_storage(Storage).
		Default address is "next available". To add a CDROM slot: add_storage("cdrom").
		"""
		self.cloud_manager.attach_storage(server_uuid=self.uuid, storage_uuid=Storage.uuid, storage_type=type, address=address)
		self.storage_devices.append(Storage)

	def remove_storage(self, Storage):
		"""
		Remove Storage from a Server. The Storage must be a reference to an object in Server.storage_devices or the method will throw and Exception.
		A Storage from get_storage(uuid) will not work as it is missing the "address" property.
		"""
		if not hasattr(Storage, "address"):
			raise Exception("Storage does not have an address. Access the Storage via Server.storage_devices so they include address. (This is due how the API handles Storages)")

		self.cloud_manager.detach_storage(server_uuid=self.uuid, address=Storage.address)
		self.storage_devices.remove(Storage)

	def add_firewall_rule(self, FirewallRule):
		"""
		Adds the specified FirewallRule to this server. Returns a FirewallRule instance
		that is associated with this server instance.

		Instantly calls the API, no need to call .save(). This is because firewall can not
		be configured with the same request as the rest of the Server.
		"""
		firewall_rule_body = FirewallRule.prepare_post_body()
		firewall_rule = self.cloud_manager.create_firewall_rule(self.uuid, firewall_rule_body)
		firewall_rule._associate_with_server(self)
		return firewall_rule

	def remove_firewall_rule(self, FirewallRule):
		return FirewallRule.destroy()


	def get_firewall_rules(self):
		"""
		Returns all FirewallRule instances that are associated with this server instance.
		"""
		firewall_rules = self.cloud_manager.get_firewall_rules(self.uuid)
		for firewall_rule in firewall_rules:
			firewall_rule._associate_with_server(self)
		return firewall_rules

	def configure_firewall(self, FirewallRules):
		"""
		Helper function for automatically adding several FirewallRules in series.
		"""
		firewall_rule_bodies = []
		for FirewallRule in FirewallRules:
			firewall_rule_bodies.append(FirewallRule.prepare_post_body())

		firewall_rules = self.cloud_manager.configure_firewall(self.uuid, firewall_rule_bodies)
		for firewall_rule in firewall_rules:
			firewall_rule._associate_with_server(self)
		return firewall_rules


	def prepare_post_body(self):
		body = dict()
		# mandatory
		body["server"] = {
			"hostname": self.hostname,
			"zone": self.zone,
			"title": self.title,
			"storage_devices": {}
		}

		# optional
		if hasattr(self, "core_number"): 		body["server"]["core_number"] = self.core_number
		if hasattr(self, "memory_amount"): 		body["server"]["memory_amount"] = self.memory_amount
		if hasattr(self, "boot_order"): 		body["server"]["boot_order"] = self.boot_order
		if hasattr(self, "firewall"): 			body["server"]["firewall"] = self.firewall
		if hasattr(self, "nic_model"):			body["server"]["nic_model"] = self.nic_model
		if hasattr(self, "password_delivery"):	body["server"]["password_delivery"] = self.password_delivery
		if hasattr(self, "timezone"):			body["server"]["timezone"] = self.timezone
		if hasattr(self, "video_model"):		body["server"]["video_model"] = self.video_model
		if hasattr(self, "vnc_password"):		body["server"]["vnc_password"] = self.vnc_password


		body["server"]["storage_devices"] = {
			"storage_device": []
		}

		storage_title_id = 0 # running number for unique storage titles
		for storage in self.storage_devices:
			if storage.os == None:
				storage_title_id +=  1
			storage_body = storage.prepare_post_body(self.hostname, storage_title_id)
			body["server"]["storage_devices"]["storage_device"].append(storage_body)

		return body


	def __str__(self):
		return "Server: " + self.hostname
