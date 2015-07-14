from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict, object, str
from future import standard_library
standard_library.install_aliases()

from upcloud_api.tools import assignIfExists, OperatingSystems

class Storage(object):

	def __init__(self, **kwargs):
		self.__reset(**kwargs)

	def __reset(self, **kwargs):
		"""
		Reset after repopulating from API.
		"""

		# When creating locally (optional)
		self.os = assignIfExists(["os"], **kwargs)

		# When not creating locally (always injected when populating object from API response)
		self.cloud_manager = assignIfExists(["cloud_manager"], **kwargs)

		# Always present in responses
		self.type = assignIfExists(["type"], **kwargs)
		self.uuid = assignIfExists(["uuid", "storage"], **kwargs) # self.uuid either "uuid" or "storage"
		self.title = assignIfExists(["title", "storage_title"], **kwargs) # self.title either "title" or "storage_title"
		self.size = assignIfExists(["size", "storage_size"], 10,  **kwargs) # self.size either "size" or "storage_size"

		# Present if populated via /storage/ or /storage/uuid
		self.access = assignIfExists(["access"], **kwargs)
		self.license = assignIfExists(["license"], **kwargs)
		self.state = assignIfExists(["state"], **kwargs)

		# Only present when populated via /server/uuid
		self.address = assignIfExists(["address"], **kwargs)

		# Only present when populated via /storage/uuid
		self.tier = assignIfExists(["tier"], **kwargs)
		self.zone = assignIfExists(["zone"], **kwargs)


	def destroy(self):
		self.cloud_manager.delete_storage(self.uuid)

	def update(self, size, title):
		body = Storage.prepare_put_body(size, title)
		data = self.cloud_manager.request("PUT", "/storage/" + self.uuid, body)
		self.__reset(**data["storage"])

	def __str__(self):
		return str(self.title) + ", size: " + str(self.size) + " (" + str(self.tier) + ")"

	@staticmethod
	def prepare_put_body(size, title):
		body = {"storage": {}}
		if(size): 	body["storage"]["size"] = size
		if(title): 	body["storage"]["title"] = title
		return body


	def prepare_post_body(self, storage_title=None, storage_title_id=None):
			body = dict()

			# clone from public template OR create empty storage
			if self.os:
				body["action"] = "clone"
			else:
				body["action"] = "create"

			# default tier is maxiops
			if self.tier:
				body["tier"] = self.tier
			else:
				body["tier"] = "maxiops"

			# reasonable default title
			if self.title:
				body["title"] = self.title
			else:
				if self.os:
					body["title"] = storage_title + " OS disk"
				else:
					body["title"] = storage_title + " storage disk " + str(storage_title_id)

			# don't specify size if attaching CDROM (CDROMS not yet supported)
			if body["action"] == "create" or body["action"] == "clone":
				body["size"] = self.size

			# figure out public template (CDROMS not yet supported)
			if body["action"] == "attach" or body["action"] == "clone":
				body["storage"] = OperatingSystems.get_OS_UUID(self.os)

			# optionals
			if self.type: 		body["type"] = self.type
			if self.address:	body["address"] = self.address
			if self.zone:	body["zone"] = self.zone

			return body

	@staticmethod
	def _create_storage_objs(storages, cloud_manager):
		if "storage" in storages:
			storages = storages["storage"]

		if "storage_device" in storages:
			storages = storages["storage_device"]

		storage_objs = list()
		for storage in storages:
			storage_objs.append( Storage(cloud_manager = cloud_manager, **storage) )
		return storage_objs

	@staticmethod
	def _create_storage_obj(storage, cloud_manager):
		return Storage(cloud_manager = cloud_manager, **storage)
