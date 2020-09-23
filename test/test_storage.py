from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from conftest import Mock
import responses


class TestStorage(object):
    @responses.activate
    def test_get_storage(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        assert type(storage).__name__ == "Storage"
        assert storage.uuid == "01d4fcd4-e446-433b-8a9c-551a1284952e"

    @responses.activate
    def test_get_storages(self, manager):
        data = Mock.mock_get("storage/public")
        storages = manager.get_storages("public")

        for storage in storages:
            assert type(storage).__name__ == "Storage"

    @responses.activate
    def test_storage_create(self, manager):
        Mock.mock_post("storage")
        storage = manager.create_storage(666, "maxiops", "My data collection", "fi-hel1")
        assert type(storage).__name__ == "Storage"
        assert storage.size == 666
        assert storage.tier == "maxiops"
        assert storage.title == "My data collection"
        assert storage.zone == "fi-hel1"

    @responses.activate
    def test_clone_storage(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/clone")
        cloned_storage = manager.clone_storage(storage, 'cloned-storage-test', 'fi-hel1')
        assert type(cloned_storage).__name__ == "Storage"
        assert cloned_storage.size == 666
        assert cloned_storage.tier == "maxiops"
        assert cloned_storage.title == "cloned-storage-test"
        assert cloned_storage.zone == "fi-hel1"

    @responses.activate
    def test_cancel_clone_storage(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/clone")
        cloned_storage = manager.clone_storage(storage, 'cloned-storage-test', 'fi-hel1')

        Mock.mock_post("storage/01d3e9ad-8ff5-4a52-9fa2-48938e488e78/cancel", empty_content=True)
        res = manager.cancel_clone_storage(cloned_storage)
        assert res == {}

    @responses.activate
    def test_load_cd_rom(self, manager):
        data = Mock.mock_post("server/00798b85-efdc-41ca-8021-f6ef457b8531/cdrom/load", ignore_data_field=True)
        storage_devices = manager.load_cd_rom("00798b85-efdc-41ca-8021-f6ef457b8531", "01ec5c26-a25d-4752-94e4-27bd88b62816")
        assert len(storage_devices) == 2

    @responses.activate
    def test_eject_cd_rom(self, manager):
        data = Mock.mock_post("server/00798b85-efdc-41ca-8021-f6ef457b8531/cdrom/eject", ignore_data_field=True, empty_payload=True)
        storage_devices = manager.eject_cd_rom("00798b85-efdc-41ca-8021-f6ef457b8531")
        assert len(storage_devices) == 1

    @responses.activate
    def test_create_storage_backup(self, manager):
        data = Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/backup")
        storage = manager.create_storage_backup("01d4fcd4-e446-433b-8a9c-551a1284952e", "test-backup")
        assert storage.title == "test-backup"
        assert storage.size == 666
        assert storage.zone == "fi-hel1"

    @responses.activate
    def test_restore_storage_backup(self, manager):
        data = Mock.mock_post("storage/01350eec-6ebf-4418-abe4-e8bb1d5c9643/restore", empty_content=True)
        res = manager.restore_storage_backup("01350eec-6ebf-4418-abe4-e8bb1d5c9643")
        assert res == {}

    @responses.activate
    def test_templatize_storage(self, manager):
        data = Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/templatize")
        storage = manager.templatize_storage("01d4fcd4-e446-433b-8a9c-551a1284952e", "my server template")
        assert storage.title == "my server template"
        assert storage.type == "template"

    @responses.activate
    def test_storage_update(self, manager):

        Mock.mock_put("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.modify_storage("01d4fcd4-e446-433b-8a9c-551a1284952e", title="my bigger data collection", size=15)
        assert type(storage).__name__ == "Storage"
        assert storage.size == 15
        assert storage.title == "my bigger data collection"

    @responses.activate
    def test_storage_update_oop(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        Mock.mock_put("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage.title = "my bigger data collection"
        storage.size = 15
        storage.save()
        assert storage.title == "my bigger data collection"
        assert storage.size == 15

    @responses.activate
    def test_storage_delete(self, manager):
        Mock.mock_delete("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        res = manager.delete_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")
        assert res == {}

    @responses.activate
    def test_storage_delete_oop(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")
        Mock.mock_delete("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage.destroy()
        # just assert no errors
