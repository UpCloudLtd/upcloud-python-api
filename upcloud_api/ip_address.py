from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from upcloud_api.base import BaseAPI

class IP_address(BaseAPI):
	"""
	Object representation of the IP-address.

	Attributes:
	access -- "public" or "private"
	address -- the actual IP_address (string)
	ptr_record -- the reverse DNS name (string)
	server -- the UUID of the server this IP is attached to (string)

	The only updateable field is the ptr_record.
	ptr_record and server are present only if /server/uuid endpoint was used.
	"""

	def __init__(self, access, address, cloud_manager, family="IPv4",
				 ptr_record=None, server=None, *args, **kwargs):
		"""
		ptr_record and server not returned by the API in every case (e.g. when IP is nested).
		Only ptr_record is editable due to restrictions of the API.
		"""
		self._cloud_manager = cloud_manager
		self.__reset(access, address, family, ptr_record, server)

	def __reset(self, access, address, family="IPv4", ptr_record=None, server=None):
		"""
		Reset after repopulating from API.
		"""
		# Always present
		self._access = access
		self._address = address
		self._family = family

		# Present when not populated from /server/uuid endpoint
		self._server_uuid = server
		self.ptr = ptr_record

	def save(self):
		"""
		IP_address can only change its PTR record. Saves the current state, PUT /ip_address/uuid.
		"""
		body = { "ip_address": { "ptr_record": self.ptr } }
		data = self._cloud_manager.request("PUT", "/ip_address/" + self.address, body)
		self.__reset(**data["ip_address"])

	def destroy(self):
		"""
		Release the IP_address. DELETE /ip_address/uuid
		"""
		self._cloud_manager.release_IP(self.address)

	def __str__(self):
		return "IP-address: " + self.address

	@property
	def address(self):
		return self._address

	@property
	def access(self):
		return self._access

	@property
	def server_uuid(self):
		return self._server_uuid

	@property
	def family(self):
	    return self._family


	@staticmethod
	def _create_ip_address_objs(IP_addrs, cloud_manager):
		IP_objs = list()
		for IP_addr in IP_addrs["ip_address"]:
			IP_objs.append( IP_address(cloud_manager = cloud_manager, **IP_addr) )
		return IP_objs
