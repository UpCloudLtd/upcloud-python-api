import responses
from conftest import Mock


class TestHost:
    @responses.activate
    def test_get_hosts(self, manager):
        data = Mock.mock_get('host')
        hosts = manager.get_hosts()

        for host in hosts:
            assert type(host).__name__ == 'Host'

    @responses.activate
    def test_get_host(self, manager):
        data = Mock.mock_get('host/7653311107')
        host = manager.get_host('7653311107')

        assert type(host).__name__ == 'Host'
        assert host.id == 7653311107
        assert host.description == 'My Host #1'
        assert host.zone == 'private-zone-id'
        assert host.windows_enabled == 'no'
        assert len(host.stats.get('stat')) == 2

    @responses.activate
    def test_modify_host(self, manager):
        data = Mock.mock_patch('host/7653311107')
        host = manager.modify_host('7653311107', 'My New Host')

        assert type(host).__name__ == 'Host'
        assert host.id == 7653311107
        assert host.description == 'My New Host'
        assert host.zone == 'private-zone-id'
        assert host.windows_enabled == 'no'
        assert len(host.stats.get('stat')) == 2
