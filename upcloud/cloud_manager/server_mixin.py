from ..tools import _create_ip_address_objs
from ..tools import _create_storage_objs

from ..server import Server

class ServerManager():
	"""
	Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
	"""

	def get_servers(self, populate=False):
		"""
		Returns a list of (populated or unpopulated) Server instances. 
		Populate = False (default) => 1 API request, returns unpopulated Server instances.
		Populate = True => Does 1 + n API requests (n = # of servers), returns populated Server instances.
		"""
		servers = self.__fetch_servers()		

		server_list = list()
		for server in servers:
			server_list.append( Server(server, cloud_manager = self) )

		if( populate ):
			for server_instance in server_list:
				server_instance.populate()

		return server_list

	
	def get_server(self, UUID):
		"""
		Returns a (populated) Server instance.
		"""
		server, IP_addresses, storages = self.get_server_data(UUID)
		
		return Server(	server, 
						ip_addresses = IP_addresses, 
						storage_devices = storages, 
						populated = True,
						cloud_manager = self )


	def create_server(self, VM, storage_devices):
		body = dict()
		body["server"] = {
			"core_number": VM["cores"],
			"memory_amount": VM["ram"],
			"hostname": VM["hostname"],
			"zone": VM["zone"],
			"title": VM["title"],
			"storage_devices": {}
		}
		body["server"]["storage_devices"] = {
			"storage_device": []
		}

		for storage in storage_devices:
			device = dict()
			device["action"] = storage["action"]
			device["tier"] = storage["tier"]
			device["title"] = storage["title"]

			if device["action"] == "create" or device["action"] == "clone":
				device["size"] = storage["size"]

			if device["action"] == "attach" or device["action"] == "clone":
				device["storage"] = storage["storage"]

			if "type" in storage:
				device["type"] = storage["type"]

			body["server"]["storage_devices"]["storage_device"].append(device)

		res = self.post_request("/server", body)
		server = res["server"]
		
		# Populate subobjects
		IP_addresses = _create_ip_address_objs( server.pop("ip_addresses"), cloud_manager = self )
		storages = _create_storage_objs( server.pop("storage_devices"), cloud_manager = self )

		return Server(	server, 
						ip_addresses = IP_addresses, 
						storage_devices = storages, 
						populated = True,
						cloud_manager = self )


	def modify_server(self, UUID, **kwargs):
		body = dict()
		body["server"] = {}
		for arg in kwargs:
			if arg not in Server.updateable_fields:
				Exception( str(arg) + " is not an updateable field" )
			body["server"][arg] = kwargs[arg]

		res = self.request("PUT", "/server/" + UUID, body)
		server = res["server"]
		
		# Populate subobjects
		IP_addresses = _create_ip_address_objs( server.pop("ip_addresses"), cloud_manager = self )
		storages = _create_storage_objs( server.pop("storage_devices"), cloud_manager = self )

		return Server(	server, 
						ip_addresses = IP_addresses, 
						storage_devices = storages, 
						populated = True,
						cloud_manager = self )


	def delete_server(self, UUID):
		return self.request("DELETE", "/server/" + UUID)
	
	def __fetch_servers(self):
		"""
		Returns '/servers' data in Python dict.
		"""
		data = self.get_request("/server")
		return data["servers"]["server"]

	
	def get_server_data(self, UUID):
		"""
		Returns '/server/uuid' data in Python dict. 
		Creates object representations of any IP-address and Storage.
		"""
		data = self.get_request("/server/" + UUID)		
		server = data["server"]
		
		# Populate subobjects
		IP_addresses = _create_ip_address_objs( server.pop("ip_addresses"), cloud_manager = self )
		storages = _create_storage_objs( server.pop("storage_devices"), cloud_manager = self )

		return server, IP_addresses, storages
