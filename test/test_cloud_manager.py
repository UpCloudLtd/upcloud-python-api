from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from future import standard_library
standard_library.install_aliases()

from conftest import Mock
import json, responses


class TestCloudManagerBasic(object):
	@responses.activate
	def test_get_account(self, manager):
		data = Mock.mock_get("account")

		res = manager.authenticate()
		assert json.loads(data) == res
		res = manager.get_account()
		assert json.loads(data) == res

	@responses.activate
	def test_get_prices(self, manager):
		data = Mock.mock_get("price")

		res = manager.get_prices()
		assert json.loads(data) == res

	@responses.activate
	def test_get_zones(self, manager):
		data = Mock.mock_get("zone")

		res = manager.get_zones()
		assert json.loads(data) == res

	@responses.activate
	def test_get_timezones(self, manager):
		data = Mock.mock_get("timezone")

		res = manager.get_timezones()
		assert json.loads(data) == res


