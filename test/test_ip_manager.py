from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from future import standard_library
standard_library.install_aliases()

from conftest import Mock
import json, responses

class TestIP(object):
	@responses.activate
	def test_get_ip(self, manager):
		data = Mock.mock_get("ip_address/10.1.0.101")
		ip_addr = manager.get_IP("10.1.0.101")

		assert type(ip_addr).__name__ == "IP_address"
		assert ip_addr.address == "10.1.0.101"
		assert ip_addr.ptr == "a.ptr.record"

	@responses.activate
	def test_get_ips(self, manager):
		data = Mock.mock_get("ip_address")
		ip_addrs = manager.get_IPs()

		for ip_addr in ip_addrs:
			assert type(ip_addr).__name__ == "IP_address"

	@responses.activate
	def test_modify_ip_oop(self, manager):
		# get ip
		data = Mock.mock_get("ip_address/10.1.0.101")
		ip_addr = manager.get_IP("10.1.0.101")

		# put ip
		data = Mock.mock_put("ip_address/10.1.0.101")
		ip_addr.ptr = "my.ptr.record"
		ip_addr.save()

		assert ip_addr.ptr == "my.ptr.record"

	@responses.activate
	def test_modify_ip(self, manager):
		data = Mock.mock_put("ip_address/10.1.0.101")
		ip_addr = manager.modify_IP("10.1.0.101", ptr_record="my.ptr.record")

		assert ip_addr.ptr == "my.ptr.record"

	@responses.activate
	def test_modify_ip(self, manager):
		data = Mock.mock_put("ip_address/10.1.0.101")
		ip_addr = manager.modify_IP("10.1.0.101", ptr_record="my.ptr.record")
		assert ip_addr.ptr == "my.ptr.record"


	@responses.activate
	def test_ip_delete(self, manager):
		Mock.mock_delete("ip_address/10.1.0.101")
		res = manager.release_IP("10.1.0.101")
		assert res == {}
