## About
```python
class StorageManager():
	"""
	Functions for managing Storage disks. Intended to be used as a mixin for CloudManager.
	"""
```
`StorageManager` is a mixed into `CloudManager` and the following methods are available by

```python
manager = CloudManager("api-username", "password")
manager.method()
```

`BackupDeletionPolicy` describes wanted action on backups when deleting a storage or a server with its storages.
Available policies are `KEEP`, `KEEP_LATEST` and `DELETE`.

## Methods

```python
def get_storages(self, storage_type="normal"):
	"""
	Returns a list of Storage objects from the API.
	Storage types: public, private, normal, backup, cdrom, template, favorite
	"""
```

```python
def get_storage(self, UUID):
	"""
	Returns a Storage object from the API.
	"""
```

```python
def get_templates(self):
	"""
	Return a list of Storages that are templates in a dict with title as key and uuid as value.
	"""
```

```python
def create_storage(self, size=10, tier="maxiops", title="Storage disk", zone="fi-hel1"):
	"""
	Create a Storage object. Returns an object based on the API's response.
	"""
```

```python
def modify_storage(self, UUID, size, title):
	"""
	Modify a Storage object. Returns an object based on the API's response.
	"""
```

```python
def delete_storage(self, UUID):
	"""
	Destroy a Storage object.
	"""
```

```python
def attach_storage(self, server_uuid, storage_uuid, storage_type, address):
	"""
	Attach a Storage object to a Server. Return a list of the server's storages.
	"""
```

```python
def detach_storage(self, server_uuid, address):
	"""
	Detach a Storage object to a Server. Return a list of the server's storages.
	"""
```

```python
def load_cd_rom(self, server, address):
	"""
	Loads a storage as a CD-ROM in the CD-ROM device of a server. Returns a list of the server's storages.
	"""
```

```python
def eject_cd_rom(self, server):
	"""
Ejects the storage from the CD-ROM device of a server. Returns a list of the server's storages.
	"""
```

```python
def create_storage_backup(self, storage, title):
	"""
Creates a point-in-time backup of a storage resource. Returns a storage object.
	"""
```

```python
def restore_storage_backup(self, storage):
	"""
Restores the origin storage with data from the specified backup storage. Returns a storage object.
	"""
```

```python
def templatize_storage(self, storage, title):
	"""
Creates an exact copy of an existing storage resource which can be used as a template for creating new servers. Returns a storage object.
	"""
```

```python
def create_storage_import(self, storage, source, source_location=None):
	"""
	Creates an import task to import data into an existing storage and returns a storage import object.
	Source types: http_import or direct_upload.
	"""
```

```python
def upload_file_for_storage_import(self, storage_import, file):
	"""
	Uploads a file directly to UpCloud's uploader session. Returns written bytes, md5sum and sha256sum.
	"""
```

```python
def get_storage_import_details(self, storage):
	"""
	Returns detailed information of an ongoing or finished import task within a storage import object.
	"""
```

```python
def cancel_storage_import(self, storage):
	"""
	Cancels an ongoing import task. Returns a storage import object.
	"""
```
