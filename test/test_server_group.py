import responses
from conftest import Mock

from upcloud_api import Label, ServerGroup, ServerGroupAffinityPolicy


class TestServerGroup:
    @responses.activate
    def test_get_server_group(self, manager):
        Mock.mock_get("server-group/0b5169fc-23aa-4ba7-aaab-f38868ce99cd")
        server_group = manager.get_server_group("0b5169fc-23aa-4ba7-aaab-f38868ce99cd")

        assert type(server_group).__name__ == "ServerGroup"
        assert server_group.uuid == "0b5169fc-23aa-4ba7-aaab-f38868ce99cd"
        assert server_group.title == "test group"

    @responses.activate
    def test_create_server_group(self, manager):
        Mock.mock_post("server-group", ignore_data_field=True)
        server_group = ServerGroup(
            title="rykelma",
            labels=[Label('foo', 'bar')],
            anti_affinity=ServerGroupAffinityPolicy.ANTI_AFFINITY_PREFERRED,
        )
        created_group = manager.create_server_group(server_group)

        assert created_group.uuid == "0b5169fc-23aa-4ba7-aaab-f38868ce99cd"
        assert created_group.title == "foo"

    @responses.activate
    def test_delete_server_group(self, manager):
        Mock.mock_delete("server-group/0b5169fc-23aa-4ba7-aaab-f38868ce99cd")
        res = manager.delete_server_group("0b5169fc-23aa-4ba7-aaab-f38868ce99cd")
        assert res == {}
