from .base import BaseAPI

class IP_address(BaseAPI):

	def __init__(self, access, address, cloud_manager, ptr_record=None, server=None):
		"""
		ptr_record and server not returned by the API in every case (e.g. when IP is nested).
		Only ptr_record is editable due to restrictions of the API.
		"""
		self._cloud_manager = cloud_manager
		self.__reset(access, address, ptr_record, server)

	@property
	def address(self):
		return self._address
	
	@property
	def access(self):
		return self._access	
	
	@property
	def server_uuid(self):
		return self._server_uuid
		

	def __reset(self, access, address, ptr_record=None, server=None):
		"""
		Reset after repopulating from API.
		"""
		self._access = access
		self._address = address
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

	@staticmethod
	def _create_ip_address_objs(IP_addrs, cloud_manager):
		IP_addrs = IP_addrs["ip_address"]
		IP_objs = list()
		for IP_addr in IP_addrs:
			IP_objs.append( IP_address(cloud_manager = cloud_manager, **IP_addr) )
		return IP_objs

	@staticmethod
	def _create_ip_address_obj(IP_addr, cloud_manager):
		return IP_address(cloud_manager = cloud_manager, **IP_addr)