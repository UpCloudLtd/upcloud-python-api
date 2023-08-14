import json

import responses
from conftest import Mock


class TestCloudManagerBasic:
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

    @responses.activate
    def test_get_plans(self, manager):
        data = Mock.mock_get("plan")

        res = manager.get_server_plans()
        assert json.loads(data) == res
