class Storage():
		
	def __init__(self, **kwargs):
		self.cloud_manager = kwargs.pop("cloud_manager")
		self.__reset(**kwargs)

	def __reset(self, **kwargs):
		"""
		Reset after repopulating from API.
		"""
		
		# Always present
		self.type = kwargs["type"]
		self.uuid = self.assignIfExists(["uuid", "storage"], **kwargs) # self.uuid either "uuid" or "storage"
		self.title = self.assignIfExists(["title", "storage_title"], **kwargs) # self.title either "title" or "storage_title"
		self.size = self.assignIfExists(["size", "storage_size"], **kwargs) # self.size either "size" or "storage_size"
		
		# Present if populated via /storage/ or /storage/uuid
		self.access = self.assignIfExists(["access"], **kwargs)
		self.license = self.assignIfExists(["license"], **kwargs)
		self.state = self.assignIfExists(["state"], **kwargs)

		# Only present when populated via /server/uuid
		self.address = self.assignIfExists(["address"], **kwargs)

		# Only present when populated via /storage/uuid
		self.tier = self.assignIfExists(["tier"], **kwargs)
		self.zone = self.assignIfExists(["zone"], **kwargs)
		

	def assignIfExists(self, opts, **kwargs):
		for opt in opts:
			if(opt in kwargs):
				return kwargs[opt]


	def destroy(self):
		self.cloud_manager.delete_storage(self.uuid)

	def update(self, size, title):
		body = Storage.prepare_put_body(size, title)
		data = self.cloud_manager.request("PUT", "/storage/" + self.uuid, body)
		self.__reset(**data["storage"])

	def __str__(self):
		return self.title + ", size: " + str(self.size) + " (" + self.tier + ")"

	@classmethod
	def prepare_put_body(cls, size, title):
		body = {"storage": {}}
		if(size): 	body["storage"]["size"] = size
		if(title): 	body["storage"]["title"] = title
		return body