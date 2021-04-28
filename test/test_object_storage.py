import datetime

import responses
from conftest import Mock


class TestObjectStorage:
    @responses.activate
    def test_get_object_storages(self, manager):
        data = Mock.mock_get('object-storage')
        object_storages = manager.get_object_storages()

        for object_storage in object_storages:
            assert type(object_storage).__name__ == 'ObjectStorage'

    @responses.activate
    def test_create_object_storage(self, manager):
        data = Mock.mock_post('object-storage', ignore_data_field=True)
        object_storage = manager.create_object_storage(
            'fi-hel2', 'access_key', 'secret_key', 250, 'test-os', 'for tests'
        )

        assert type(object_storage).__name__ == 'ObjectStorage'
        assert object_storage.name == 'test-os'
        assert object_storage.description == 'for tests'
        assert object_storage.zone == 'fi-hel2'
        assert object_storage.size == 250

    @responses.activate
    def test_get_object_storage(self, manager):
        data = Mock.mock_get('object-storage/06b0e4fc-d74b-455e-a373-60cd6ca84022')
        object_storage = manager.get_object_storage('06b0e4fc-d74b-455e-a373-60cd6ca84022')

        assert type(object_storage).__name__ == 'ObjectStorage'
        assert object_storage.name == 'pyapi-test3'
        assert object_storage.description == 'test for python api'
        assert object_storage.zone == 'fi-hel2'
        assert object_storage.size == 250

    @responses.activate
    def test_modify_object_storage(self, manager):
        data = Mock.mock_patch(
            'object-storage/0608edc4-d4a3-4b01-abe4-e147bd7ffe45', ignore_data_field=True
        )
        object_storage = manager.modify_object_storage(
            '0608edc4-d4a3-4b01-abe4-e147bd7ffe45',
            'access_key',
            'secret_key',
            'new description',
            500,
        )

        assert type(object_storage).__name__ == 'ObjectStorage'
        assert object_storage.name == 'test-os'
        assert object_storage.description == 'new description'
        assert object_storage.zone == 'fi-hel2'
        assert object_storage.size == 500

    @responses.activate
    def test_delete_object_storage(self, manager):
        data = Mock.mock_delete('object-storage/0608edc4-d4a3-4b01-abe4-e147bd7ffe45')
        res = manager.delete_object_storage('0608edc4-d4a3-4b01-abe4-e147bd7ffe45')

        assert res == {}

    @responses.activate
    def test_get_object_storage_network_statistics(self, manager):
        Mock.mock_get(
            'object-storage/06b0e4fc-d74b-455e-a373-60cd6ca84022/stats/network/',
            response_file='object-storage_06b0e4fc-d74b-455e-a373-60cd6ca84022_stats_network.json',
        )
        res = manager.get_object_storage_network_statistics(
            object_storage='06b0e4fc-d74b-455e-a373-60cd6ca84022',
            datetime_from=datetime.datetime(2020, 11, 3),
        )

        assert 'stats' in res
        assert len(res.get('stats').get('stat')) == 3
