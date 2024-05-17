import responses
from conftest import Mock


class TestStorage:
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
    def test_get_templates(self, manager):
        data = Mock.mock_get("storage/template")
        templates = manager.get_templates()

        for template in templates:
            assert type(template) is dict

    @responses.activate
    def test_storage_create(self, manager):
        Mock.mock_post("storage")
        storage = manager.create_storage(
            zone="fi-hel1", encrypted=True, size=666, tier="maxiops", title="My data collection"
        )
        assert type(storage).__name__ == "Storage"
        assert storage.encrypted
        assert storage.size == 666
        assert storage.tier == "maxiops"
        assert storage.title == "My data collection"
        assert storage.zone == "fi-hel1"

    @responses.activate
    def test_clone_storage(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/clone")
        cloned_storage = storage.clone('cloned-storage-test', 'fi-hel1')
        assert type(cloned_storage).__name__ == "Storage"
        assert not cloned_storage.encrypted
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
        res = cloned_storage.cancel_cloning()
        assert res == {}

    @responses.activate
    def test_load_cd_rom(self, manager):
        data = Mock.mock_post(
            "server/00798b85-efdc-41ca-8021-f6ef457b8531/cdrom/load", ignore_data_field=True
        )
        storage_devices = manager.load_cd_rom(
            "00798b85-efdc-41ca-8021-f6ef457b8531", "01ec5c26-a25d-4752-94e4-27bd88b62816"
        )
        assert len(storage_devices) == 2

    @responses.activate
    def test_eject_cd_rom(self, manager):
        data = Mock.mock_post(
            "server/00798b85-efdc-41ca-8021-f6ef457b8531/cdrom/eject",
            ignore_data_field=True,
            empty_payload=True,
        )
        storage_devices = manager.eject_cd_rom("00798b85-efdc-41ca-8021-f6ef457b8531")
        assert len(storage_devices) == 1

    @responses.activate
    def test_create_storage_backup(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        data = Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/backup")
        storage_backup = storage.create_backup("test-backup")
        assert storage_backup.title == "test-backup"
        assert storage_backup.size == 666
        assert storage_backup.zone == "fi-hel1"

    @responses.activate
    def test_restore_storage_backup(self, manager):
        data = Mock.mock_get("storage/01350eec-6ebf-4418-abe4-e8bb1d5c9643")
        storage_backup = manager.get_storage("01350eec-6ebf-4418-abe4-e8bb1d5c9643")

        data = Mock.mock_post(
            "storage/01350eec-6ebf-4418-abe4-e8bb1d5c9643/restore", empty_content=True
        )
        res = storage_backup.restore_backup()
        assert res == {}

    @responses.activate
    def test_templatize_storage(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.get_storage("01d4fcd4-e446-433b-8a9c-551a1284952e")

        data = Mock.mock_post("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/templatize")
        storage_template = storage.templatize("my server template")
        assert storage_template.title == "my server template"
        assert storage_template.type == "template"

    @responses.activate
    def test_create_storage_import(self, manager):
        data = Mock.mock_post(
            "storage/01d4fcd4-e446-433b-8a9c-551a1284952e/import", ignore_data_field=True
        )
        storage_import = manager.create_storage_import(
            "01d4fcd4-e446-433b-8a9c-551a1284952e", 'direct_upload'
        )
        assert storage_import.state == "prepared"
        assert storage_import.source == "direct_upload"

    @responses.activate
    def test_upload_file_for_storage_import(self, manager):
        # TODO: this test probably doesn't correctly test for the actual format of the data being uploaded
        data = Mock.mock_post(
            "storage/01d4fcd4-e446-433b-8a9c-551a1284952e/import", ignore_data_field=True
        )
        storage_import = manager.create_storage_import(
            "01d4fcd4-e446-433b-8a9c-551a1284952e", 'direct_upload'
        )
        data = Mock.mock_put(
            "https://fi-hel1.img.upcloud.com/uploader/session/07a6c9a3-300e-4d0e-b935-624f3dbdff3f",
            ignore_data_field=True,
            empty_payload=True,
            call_api=False,
        )
        res = manager.upload_file_for_storage_import(
            storage_import, 'test/json_data/test_file.json'
        )
        assert res.get("written_bytes") == 909500125
        assert res.get("md5sum") == "5cc6f7e7a1c52303ac3137d62410eec5"
        assert (
            res.get("sha256sum")
            == "bdf14d897406939c11a73d0720ca75c709e756d437f8be9ee26af6b58ede3bd7"
        )

    @responses.activate
    def test_get_storage_import_details(self, manager):
        data = Mock.mock_get("storage/01d4fcd4-e446-433b-8a9c-551a1284952e/import")
        storage_import = manager.get_storage_import_details("01d4fcd4-e446-433b-8a9c-551a1284952e")
        assert storage_import.state == "pending"
        assert storage_import.uuid == "07a6c9a3-300e-4d0e-b935-624f3dbdff3f"

    @responses.activate
    def test_cancel_storage_import(self, manager):
        data = Mock.mock_post(
            "storage/01d4fcd4-e446-433b-8a9c-551a1284952e/import/cancel",
            empty_payload=True,
            ignore_data_field=True,
        )
        storage_import = manager.cancel_storage_import("01d4fcd4-e446-433b-8a9c-551a1284952e")
        assert storage_import.state == "cancelling"
        assert storage_import.uuid == "07a6c9a3-300e-4d0e-b935-624f3dbdff3f"

    @responses.activate
    def test_storage_update(self, manager):
        Mock.mock_put("storage/01d4fcd4-e446-433b-8a9c-551a1284952e")
        storage = manager.modify_storage(
            "01d4fcd4-e446-433b-8a9c-551a1284952e", title="my bigger data collection", size=15
        )
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
