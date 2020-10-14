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

        for network in networks:
            assert type(network).__name__ == "Network"

    @responses.activate
    def test_get_network(self, manager):
        data = Mock.mock_get('network/03000000-0000-4000-8001-000000000000')
        network = manager.get_network('03000000-0000-4000-8001-000000000000')

        assert type(network).__name__ == "Network"
        assert network.uuid == '03000000-0000-4000-8001-000000000000'
        assert network.type == 'public'
        assert network.zone == 'fi-hel1'

    @responses.activate
    def test_create_network(self, manager):
        data = Mock.mock_post('network')
        network = manager.create_network(
            name='test network',
            zone='fi-hel1',
            address='172.16.0.0/22',
            dhcp='yes',
            family='IPv4',
            router='04b65749-61e2-4f08-a259-c75afbe81abf',
            dhcp_default_route='no',
            dhcp_dns=["172.16.0.10", "172.16.1.10"],
            dhcp_bootfile_url='tftp://172.16.0.253/pxelinux.0',
            gateway='172.16.0.1'
        )

        assert type(network).__name__ == "Network"
        assert network.uuid == '036df3d0-8629-4549-984e-dc86fc3fa1b0'
        assert network.type == 'private'
        assert network.zone == 'fi-hel1'

    @responses.activate
    def test_modify_network(self, manager):
        data = Mock.mock_put('network/036df3d0-8629-4549-984e-dc86fc3fa1b0')
        network = manager.modify_network(
            uuid='036df3d0-8629-4549-984e-dc86fc3fa1b0',
            dhcp='yes',
            family='IPv4',
            router='04b65749-61e2-4f08-a259-c75afbe81abf',
            name='test network modify',
            dhcp_default_route='no',
            dhcp_dns=["172.16.0.10", "172.16.1.10"],
            dhcp_bootfile_url='tftp://172.16.0.253/pxelinux.0',
            gateway='172.16.0.1'
        )

        assert type(network).__name__ == "test network modify"
        assert network.uuid == '036df3d0-8629-4549-984e-dc86fc3fa1b0'
        assert network.type == 'private'
        assert network.zone == 'fi-hel1'

    @responses.activate
    def test_delete_network(sekf, manager):
        data = Mock.mock_delete('network/03000000-0000-4000-8001-000000000000')
        res = manager.delete_network('03000000-0000-4000-8001-000000000000')

        assert res == {}

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
