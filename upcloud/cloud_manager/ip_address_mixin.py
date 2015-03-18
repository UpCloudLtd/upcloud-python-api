from ..ip_address import IP_address
from ..tools import _create_ip_address_obj
from ..tools import _create_ip_address_objs


class IPManager():
	"""
	Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
	"""
	
	def get_IP(self, UUID):
		res = self.get_request("/ip_address/" + UUID)
		IP = _create_ip_address_obj( res["ip_address"], cloud_manager=self )
		return IP

	def get_IPs(self):
		res = self.get_request("/ip_address")
		IPs = _create_ip_address_objs( res["ip_addresses"], cloud_manager=self )
		return IPs

	def attach_IP(self, server_UUID):
		body = dict()
		body["ip_address"] = {
			"server" : server_UUID
		}

		res = self.request("POST", "/ip_address", body)
		IP = _create_ip_address_obj( res["ip_address"], cloud_manager=self )
		return IP

	def modify_IP(self, IP_addr, ptr_record):
		body = dict()
		body["ip_address"] = {
			"ptr_record": ptr_record
		}

		res = self.request("PUT", "/ip_address/" + IP_addr, body)
		IP = _create_ip_address_obj( res["ip_address"], cloud_manager=self )
		return IP

	def release_IP(self, IP_addr):
		return self.request("DELETE", "/ip_address/" + IP_addr)

