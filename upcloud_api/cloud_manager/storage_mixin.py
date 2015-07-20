from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import dict, object
from future import standard_library
standard_library.install_aliases()

from upcloud_api import Storage

class StorageManager(object):
	"""
	Functions for managing Storage disks. Intended to be used as a mixin for CloudManager.
	"""

	def get_storages(self, storage_type="normal"):
		"""
		Returns a list of Storage objects from the API.
		Storage types: public, private, normal, backup, cdrom, template, favorite
		"""
		res = self.get_request("/storage/" + storage_type)
		return Storage._create_storage_objs( res["storages"], cloud_manager = self )

	def get_storage(self, UUID):
		"""
		Returns a Storage object from the API.
		"""
		res = self.get_request("/storage/" + UUID)
		return Storage._create_storage_obj( res["storage"], cloud_manager = self )

	def create_storage(self, size=10, tier="maxiops", title="Storage disk", zone="fi-hel1"):
		"""
		Create a Storage object. Returns an object based on the API's response.
		"""
		body = dict()
		body["storage"] = {
			"size": size,
			"tier": tier,
			"title": title,
			"zone": zone
		}
		res = self.post_request("/storage", body)
		return Storage._create_storage_obj( res["storage"], cloud_manager = self )

	def modify_storage(self, UUID, size, title):
		"""
		Modify a Storage object. Returns an object based on the API's response.
		"""

		body = Storage.prepare_put_body(size, title)
		res = self.request("PUT","/storage/" + UUID, body)
		return Storage._create_storage_obj( res["storage"], cloud_manager = self )

	def delete_storage(self, UUID):
		"""
		Destroy a Storage object.
		"""
		return self.request("DELETE", "/storage/" + UUID)

	def attach_storage(self, server_uuid, storage_uuid, storage_type, address):
		"""
		Attach a Storage object to a Server. Return a list of the server's storages.
		"""
		body = { "storage_device": {} }
		if(storage_uuid): 	body["storage_device"]["storage"] = storage_uuid
		if(storage_type): 	body["storage_device"]["type"] = storage_type
		if(address): 		body["storage_device"]["address"] = address

		res = self.post_request("/server/" + server_uuid + "/storage/attach", body)
		return Storage._create_storage_objs( res["server"]["storage_devices"], cloud_manager = self )

	def detach_storage(self, server_uuid, address):
		"""
		Detach a Storage object to a Server. Return a list of the server's storages.
		"""
		body = { "storage_device": { "address": address } }
		res = self.post_request("/server/" + server_uuid + "/storage/detach", body)
		return Storage._create_storage_objs( res["server"]["storage_devices"], cloud_manager = self )
