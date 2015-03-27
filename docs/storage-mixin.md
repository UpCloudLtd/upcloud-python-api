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