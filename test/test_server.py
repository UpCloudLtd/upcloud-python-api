import pytest
import responses
from conftest import Mock


class TestServer:
    @responses.activate
    def test_get_server(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        assert type(server).__name__ == 'Server'
        assert server.uuid == '00798b85-efdc-41ca-8021-f6ef457b8531'
        assert len(server.labels['label']) == 1
        assert server.labels['label'][0]['value'] == "example"

    @responses.activate
    def test_get_unpopulated_servers(self, manager):
        data = Mock.mock_get('server')
        servers = manager.get_servers()

        for server in servers:
            assert type(server).__name__ == 'Server'

    @responses.activate
    def test_get_populated_servers(self, manager):
        data = Mock.mock_get('server')
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        data = Mock.mock_get('server/009d64ef-31d1-4684-a26b-c86c955cbf46')
        servers = manager.get_servers(populate=True)

        for server in servers:
            assert type(server).__name__ == 'Server'

    @responses.activate
    def test_start_server(self, manager):
        data = Mock.mock_get('server/009d64ef-31d1-4684-a26b-c86c955cbf46')
        server = manager.get_server('009d64ef-31d1-4684-a26b-c86c955cbf46')

        assert server.state == 'stopped'

        data = Mock.mock_server_operation('server/009d64ef-31d1-4684-a26b-c86c955cbf46/start')
        server.start()

        assert server.state == 'started'

    @responses.activate
    def test_stop_server(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        assert server.state == 'started'

        data = Mock.mock_server_operation('server/00798b85-efdc-41ca-8021-f6ef457b8531/stop')
        server.stop()

        assert server.state == 'maintenance'

    @responses.activate
    def test_restart_server(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        assert server.state == 'started'

        data = Mock.mock_server_operation('server/00798b85-efdc-41ca-8021-f6ef457b8531/restart')
        server.restart()

        assert server.state == 'maintenance'

    @responses.activate
    def test_attach_and_detach_ip(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')
        assert len(server.ip_addresses) == 2

        data = Mock.mock_post('ip_address')
        server.add_ip()
        assert len(server.ip_addresses) == 3

        Mock.mock_delete('ip_address/' + server.ip_addresses[2].address)
        server.remove_ip(server.ip_addresses[2])
        assert len(server.ip_addresses) == 2

    @responses.activate
    def test_attach_and_detach_storage(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')
        assert len(server.storage_devices) == 1
        assert server.storage_devices[0].title == 'Storage for server1.example.com'

        data = Mock.mock_get('storage/01d4fcd4-e446-433b-8a9c-551a1284952e')
        storage = manager.get_storage('01d4fcd4-e446-433b-8a9c-551a1284952e')

        responses.add(
            responses.POST,
            Mock.base_url + '/server/00798b85-efdc-41ca-8021-f6ef457b8531/storage/attach',
            body=Mock.read_from_file('storage_attach.json'),
            status=200,
            content_type='application/json',
        )
        server.add_storage(storage)
        assert len(server.storage_devices) == 2
        assert server.storage_devices[0].title == 'Storage for server1.example.com'
        assert server.storage_devices[1].title == 'Operating system disk'

        responses.add(
            responses.POST,
            Mock.base_url + '/server/00798b85-efdc-41ca-8021-f6ef457b8531/storage/detach',
            body=Mock.read_from_file('storage_attach.json'),
            status=200,
            content_type='application/json',
        )
        server.remove_storage(server.storage_devices[1])

        assert len(server.storage_devices) == 1
        assert server.storage_devices[0].title == 'Storage for server1.example.com'

    @responses.activate
    def test_update_server_oop(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        server.core_number = 6
        server.memory_amount = 1024
        server.title = 'Updated server'

        data = Mock.mock_put('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server.save()

        assert server.core_number == 6
        assert server.memory_amount == 1024
        assert server.title == 'Updated server'

    @responses.activate
    def test_update_server_non_updateable_fields(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        with pytest.raises(Exception) as excinfo:
            server.state = 'rekt'
        assert "'state' is a readonly field" in str(excinfo.value)
