from .base import BaseAPI
from .firewall import Firewall

class Server(BaseAPI):
	"""
	Object representation of UpCloud Server instance.

	Partially immutable class; only fields that are persisted with .save() may be set with the server.field = value syntax.
	See __setattr__ override. Any field can still be set with object.__setattr__(self, field, val) syntax.
	"""
	
	updateable_fields = [ 	"boot_order", "core_number", "firewall", "hostname", "memory_amount", 
							"nic_model", "title", "timezone", "video_model", "vnc", "vnc_password" ]


	def __init__(self, *initial_data, **kwargs):
		object.__setattr__(self, "populated", False)
		object.__setattr__(self, "cloud_manager", kwargs["cloud_manager"])
		self.__reset(*initial_data, **kwargs)

	def __setattr__(self, name, value):
		"""
		Override to prevent updating readonly fields. 
		"""
		if name not in self.updateable_fields:
			raise Exception( "'" + str(name) + "' is a readonly field")
		else:
			object.__setattr__(self, name, value)

	def __reset(self, *initial_data, **kwargs):
		"""
		Reset all given attributes.
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
		self.__reset( server, 
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
		self.__reset(kwargs)
			
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

	def add_IP(self):
		"""
		Allocate a new (random) IP-address to the Server.
		"""
		IP = self.cloud_manager.attach_IP(self.uuid)
		self.ip_addresses.append(IP)

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

	def __str__(self):
		if self.populated: status = "populated"
		else: status = "not populated"
		return self.title + " (" + status + ")"