from ..base import BaseAPI
from ..firewall import Firewall

from .server_mixin import ServerManager
from .ip_address_mixin import IPManager
from .storage_mixin import StorageManager
from .firewall_mixin import FirewallManager

import base64


class CloudManager(BaseAPI, ServerManager, IPManager, StorageManager, FirewallManager):
	"""
	CloudManager contains the core functionality of the upcloud API library.
	All other managers are mixed in so code can be organized in corresponding submanager classes.
	"""

	def __init__(self, username, password):
		self.token = "Basic " + base64.b64encode( (username + ":" + password).encode() ).decode()

	def authenticate(self):
		return self.get_account()

	def get_account(self):
		return self.get_request("/account")

	def get_zones(self):
		return self.get_request("/zone")

	def get_timezones(self):
		return self.get_request("/timezone")

	def get_prices(self):
		return self.get_request("/price")

	def get_server_sizes(self):
		return self.get_request("/server_size")

