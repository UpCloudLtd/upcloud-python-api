## About
```python
class ObjectStorageManager():
	"""
	Functions for managing Object Storages. Intended to be used as a mixin for CloudManager.
	"""
```
`ObjectStorageManager` is a mixed into `CloudManager` and the following methods are available through it.

```python
manager = CloudManager("api-username", "password")
manager.method()
```

## Methods

```python
def get_object_storages(self):
	"""
	List all Object Storage devices on the account or those which the subaccount has permissions.
	Returns a list of ObjectStorage objects.
	"""
```

```python
def create_object_storage(self, zone, access_key, secret_key, size, name=None, description=None):
	"""
	Used to create a new Object Storage device with a given name, size and location.
	Zone, access_key, secret_key and size are mandatory while name and description are optional.
	"""
```

```python
def modify_object_storage(self, object_storage, access_key=None, secret_key=None, description=None, size=None):
	"""
	Modify requests can be used to update the details of an Object Storage including description, access_key and secret_key.
	Object_storage is mandatory and can be a uuid or a ObjectStorage object.
	Access_key, secret_key, description and size are optional.
  If passed access_key needs to be provided with secret_key and vice-versa.
	"""
```

```python
def delete_object_storage(self, object_storage):
	"""
	Object Storage devices can be deleted using the following API request.
	Object_storage is mandatory and can be a uuid or a ObjectStorage object.
	"""
```

```python
def get_object_storage_network_statistics(
        self,
        object_storage,
        datetime_from,
        datetime_to=None,
        interval=None,
        bucket=[],
        filename=[],
        method=[],
        status=[],
        group_by=[],
        order_by=[],
        limit=None
        ):
	"""
	The network usage of an Object Storage device is metered and can be reviewed using the statistics request.
	Object_storage is mandatory and can be a uuid or a ObjectStorage object.
  Datetime_from is mandatory and needs to be a Datetime.
  Datetime_to is optional and needs to be a Datetime.
  Interval is optional and needs to be an integer
  Bucket is optional and needs to be a list of bucket name strings
  Filename is optional and needs to be a list of filename strings
  Method is optional and needs to be a list of method name strings
  Status is optional and needs to be a list of http status codes as integers
  Group_by is optional and needs to be a list of specified properties as strings
  Order_by is optional and needs to be a list of specified properties as strings
  Limit is optional and needs to be an integer
	"""
```
