from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from future import standard_library
standard_library.install_aliases()

from conftest import Mock
import json, responses


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
		storage.update(title="my bigger data collection", size=15)
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

