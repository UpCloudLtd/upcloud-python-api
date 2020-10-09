from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from conftest import Mock
import responses


class TestNetwork(object):
    @responses.activate
    def test_get_networks(self, manager):
        data = Mock.mock_get('network')
        networks = manager.get_networks()

    @responses.activate
    def test_get_network(self, manager):
        data = Mock.mock_get('network/03000000-0000-4000-8001-000000000000')
        network = manager.get_network('03000000-0000-4000-8001-000000000000')

        assert type(network).__name__ == "Network"
        assert network.uuid == '03000000-0000-4000-8001-000000000000'
        assert network.type == 'public'
        assert network.zone == 'fi-hel1'

    @responses.activate
    def test_get_routers(self, manager):
        data = Mock.mock_get('router')
        routers = manager.get_routers()

        for router in routers:
            assert type(router).__name__ == "Router"

    @responses.activate
    def test_get_router(self, manager):
        data = Mock.mock_get('router/03b34bc2-5adf-4fc4-8c44-83f869058f5a')
        router = manager.get_router('03b34bc2-5adf-4fc4-8c44-83f869058f5a')

        assert type(router).__name__ == "Router"
        assert router.type == "normal"
        assert router.name == "test router"

    @responses.activate
    def test_create_router(self, manager):
        data = Mock.mock_post('router')
        router = manager.create_router('test router')

        assert type(router).__name__ == "Router"
        assert router.type == "normal"
        assert router.name == "test router"

    @responses.activate
    def test_modify_router(self, manager):
        data = Mock.mock_patch('router/04da7f97-dc03-4df0-868f-239f304ba72f')
        router = manager.modify_router('04da7f97-dc03-4df0-868f-239f304ba72f', 'test router modify')

        assert type(router).__name__ == "Router"
        assert router.type == "normal"
        assert router.name == "test router modify"

    @responses.activate
    def test_delete_router(self, manager):
        data = Mock.mock_delete('router/04da7f97-dc03-4df0-868f-239f304ba72f')
        res = manager.delete_router('04da7f97-dc03-4df0-868f-239f304ba72f')

        assert res == {}
