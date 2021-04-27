import responses
from conftest import Mock


class TestNetwork:
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
        data = Mock.mock_post('network', ignore_data_field=True)
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
            gateway='172.16.0.1',
        )

        assert type(network).__name__ == "Network"
        assert network.uuid == '036df3d0-8629-4549-984e-dc86fc3fa1b0'
        assert network.type == 'private'
        assert network.zone == 'fi-hel1'

    @responses.activate
    def test_modify_network(self, manager):
        data = Mock.mock_put(
            'network/036df3d0-8629-4549-984e-dc86fc3fa1b0', ignore_data_field=True
        )
        network = manager.modify_network(
            network='036df3d0-8629-4549-984e-dc86fc3fa1b0',
            dhcp='yes',
            family='IPv4',
            router='04b65749-61e2-4f08-a259-c75afbe81abf',
            name='test network modify',
            dhcp_default_route='no',
            dhcp_dns=["172.16.0.10", "172.16.1.10"],
            dhcp_bootfile_url='tftp://172.16.0.253/pxelinux.0',
            gateway='172.16.0.1',
        )

        assert type(network).__name__ == "Network"
        assert network.name == 'test network modify'
        assert network.uuid == '036df3d0-8629-4549-984e-dc86fc3fa1b0'
        assert network.type == 'private'
        assert network.zone == 'fi-hel1'

    @responses.activate
    def test_get_server_networks(self, manager):
        data = Mock.mock_get('server/0082c083-9847-4f9f-ae04-811251309b35/networking')
        networks = manager.get_server_networks('0082c083-9847-4f9f-ae04-811251309b35')

        for network in networks:
            assert type(network).__name__ == "Interface"

    @responses.activate
    def test_create_network_interface(self, manager):
        data = Mock.mock_post(
            'server/0082c083-9847-4f9f-ae04-811251309b35/networking/interface',
            ignore_data_field=True,
        )
        network_interface = manager.create_network_interface(
            server='0082c083-9847-4f9f-ae04-811251309b35',
            network='036df3d0-8629-4549-984e-dc86fc3fa1b0',
            type='private',
            ip_addresses=[{'family': 'IPv4', 'address': '172.16.1.10'}],
            index=7,
            source_ip_filtering='yes',
            bootable='yes',
        )
        assert type(network_interface).__name__ == "Interface"

    @responses.activate
    def test_modify_network_interface(self, manager):
        data = Mock.mock_put(
            'server/0082c083-9847-4f9f-ae04-811251309b35/networking/interface/7',
            ignore_data_field=True,
        )
        network_interface = manager.modify_network_interface(
            server='0082c083-9847-4f9f-ae04-811251309b35',
            index_in_path=7,
            index_in_body=8,
            ip_addresses=[{'family': 'IPv4', 'address': '172.16.1.10'}],
            source_ip_filtering='no',
            bootable='no',
        )
        assert type(network_interface).__name__ == "Interface"

    @responses.activate
    def test_delete_network_interface(self, manager):
        data = Mock.mock_delete(
            'server/0082c083-9847-4f9f-ae04-811251309b35/networking/interface/8'
        )
        res = manager.delete_network_interface('0082c083-9847-4f9f-ae04-811251309b35', 8)

        assert res == {}

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
        router = manager.modify_router(
            '04da7f97-dc03-4df0-868f-239f304ba72f', 'test router modify'
        )

        assert type(router).__name__ == "Router"
        assert router.type == "normal"
        assert router.name == "test router modify"

    @responses.activate
    def test_delete_router(self, manager):
        data = Mock.mock_delete('router/04da7f97-dc03-4df0-868f-239f304ba72f')
        res = manager.delete_router('04da7f97-dc03-4df0-868f-239f304ba72f')

        assert res == {}
