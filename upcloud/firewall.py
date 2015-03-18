#GET /1.1/server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule

from .base import BaseAPI

class Firewall(BaseAPI):

	def rules(self, UUID, rule=""):
		res = self.get("/server/" + UUID + "/firewall_rule/" + rule)
		return res