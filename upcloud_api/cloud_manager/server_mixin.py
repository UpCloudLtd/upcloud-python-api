from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict, str, object

from future import standard_library
standard_library.install_aliases()

from upcloud.tools import assignIfExists
from upcloud import IP_address
from upcloud import Storage
from upcloud import Server


class ServerManager(object):
	"""
	Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
	"""

	def get_servers(self, populate=False):
		"""
		Returns a list of (populated or unpopulated) Server instances.
		Populate = False (default) => 1 API request, returns unpopulated Server instances.
		Populate = True => Does 1 + n API requests (n = # of servers), returns populated Server instances.
		"""

		servers = self.get_request("/server")["servers"]["server"]

		server_list = list()
		for server in servers:
			# remove the extra "tag" dict to simplify accessing tags
			server['tags'] = server['tags']['tag']
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


	def create_server(self, server):
		"""
		Creates a server and its storages based on a (locally created) Server object.
		Populates the given Server instance with the API response.

		0.3.0: also supports giving the entire POST body as a dict that is directly
		serialised into JSON. Refer to the REST API documentation for correct format.

		Example:
		server1 = Server( core_number = 1,
					memory_amount = 512,
					hostname = "my.example.1",
					zone = ZONE.London,
					storage_devices = [
						Storage(os = "Ubuntu 14.04", size=10, tier=maxiops, title='The OS drive'),
						Storage(size=10),
						Storage()
					title = "My Example Server"
				])
		manager.create_server(server1)

		One storage should contain an OS. Otherwise storage fields are optional.
		- size defaults to 10,
		- title defaults to hostname + " OS disk" and hostname + " storage disk id" (id is a running starting from 1)
		- tier defaults to maxiops
		- valid operating systems are:
			"CentOS 6.5", "CentOS 7.0"
			"Debian 7.8"
			"Ubuntu 12.04", "Ubuntu 14.04"
			"Windows 2003","Windows 2008" ,"Windows 2012"

		"""
		if isinstance(server, Server):
			body = server.prepare_post_body()
		else:
			ip_data = server.pop("ip_addresses", None)
			storage_data = server.pop("storage_devices", None)

			server_dict = dict()
			server_dict['cloud_manager'] = self
			if ip_data: 	 server_dict['ip_addresses'] = IP_address._create_ip_address_objs( ip_data, cloud_manager = self )
			if storage_data: server_dict['storage_devices'] = Storage._create_storage_objs( storage_data, cloud_manager = self )

			server_from_dict = Server(server, **server_dict)
			body = server_from_dict.prepare_post_body()


		res = self.post_request("/server", body)

		# Populate subobjects
		IP_addresses = IP_address._create_ip_address_objs( res["server"].pop("ip_addresses"), cloud_manager = self )
		storages = Storage._create_storage_objs( res["server"].pop("storage_devices"), cloud_manager = self )

		if isinstance(server, Server):
			server_to_return = server
		else:
			server_to_return = server_from_dict

		server_to_return._reset( res["server"],
						ip_addresses = IP_addresses,
						storage_devices = storages,
						cloud_manager = self,
						populated = True)
		return server_to_return


	def modify_server(self, UUID, **kwargs):
		"""
		modify_server allows updating the server's updateable_fields.
		Note: Server's IP-addresses and Storages are managed by their own add/remove methods.
		"""
		body = dict()
		body["server"] = {}
		for arg in kwargs:
			if arg not in Server.updateable_fields:
				Exception( str(arg) + " is not an updateable field" )
			body["server"][arg] = kwargs[arg]

		res = self.request("PUT", "/server/" + UUID, body)
		server = res["server"]

		# Populate subobjects
		IP_addresses = IP_address._create_ip_address_objs( server.pop("ip_addresses"), cloud_manager = self )
		storages = Storage._create_storage_objs( server.pop("storage_devices"), cloud_manager = self )

		return Server(	server,
						ip_addresses = IP_addresses,
						storage_devices = storages,
						populated = True,
						cloud_manager = self )


	def delete_server(self, UUID):
		"""
		DELETE '/server/UUID'. Permanently destroys the virtual machine.
		DOES NOT remove the storage disks.

		Returns an empty object.
		"""
		return self.request("DELETE", "/server/" + UUID)


	def get_server_data(self, UUID):
		"""
		Returns '/server/uuid' data in Python dict.
		Creates object representations of any IP-address and Storage.
		"""
		data = self.get_request("/server/" + UUID)
		server = data["server"]

		# remove the extra "tag" dict to simplify accessing tags
		server['tags'] = server['tags']['tag']

		# Populate subobjects
		IP_addresses = IP_address._create_ip_address_objs( server.pop("ip_addresses"), cloud_manager = self )
		storages = Storage._create_storage_objs( server.pop("storage_devices"), cloud_manager = self )

		return server, IP_addresses, storages
