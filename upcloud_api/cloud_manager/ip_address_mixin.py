from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object, str
from future import standard_library
standard_library.install_aliases()

from upcloud_api import IP_address

class IPManager(object):
	"""
	Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
	"""

	def get_IP(self, address):
		"""
		Get an IP_address object with the IP address (string) from the API.
		e.g manager.get_IP("80.69.175.210")
		"""
		res = self.get_request("/ip_address/" + address)
		return IP_address( cloud_manager=self, **res["ip_address"] )

	def get_IPs(self):
		"""
		Get all IP_address objects from the API.
		"""
		res = self.get_request("/ip_address")
		IPs = IP_address._create_ip_address_objs( res["ip_addresses"], cloud_manager=self )
		return IPs

	def attach_IP(self, server, family="IPv4"):
		"""
		Attach a new (random) IP_address to the given server (object or UUID)
		"""

		if not isinstance(server, str):
			server = server.uuid

		body = {
			"ip_address": {
				"server": server,
				"family": family
			}
		}

		res = self.request("POST", "/ip_address", body)
		return IP_address( cloud_manager=self, **res["ip_address"] )

	def modify_IP(self, IP_addr, ptr_record):
		"""
		Modify an IP address' ptr-record (Reverse DNS).
		Accepts an IP_address instance (object) or its address (string).
		"""

		if not isinstance(IP_addr, str):
			IP_addr = IP_addr.address

		body = {
			"ip_address": {
				"ptr_record": ptr_record
			}
		}

		res = self.request("PUT", "/ip_address/" + IP_addr, body)
		return IP_address( cloud_manager=self, **res["ip_address"] )

	def release_IP(self, IP_addr):
		"""
		Destroy an IP_address. Returns an empty object.
		Accepts an IP_address instance (object) or its address (string).
		"""
		if not isinstance(IP_addr, str):
			IP_addr = IP_addr.address

		return self.request( "DELETE", "/ip_address/" + IP_addr )

