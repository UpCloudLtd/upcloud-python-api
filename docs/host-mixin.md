## About

Server hosts are only available for private cloud users. To get access, [contact UpCloud sales](https://upcloud.com/contact/).

```python
class HostManager():
	"""
	Functions for managing hosts. Intended to be used as a mixin for CloudManager.
	"""
```
`HostManager` is a mixed into `CloudManager` and the following methods are available by

```python
manager = CloudManager("api-username", "password")
manager.method()
```

## Methods

```python
def get_hosts(self):
	"""
	Returns a list of available hosts, along with basic statistics of them when available.
	Returns a list of Host objects.
	"""
```

```python
def get_host(self, id):
	"""
	Returns detailed information about a specific host in a Host object.
	Id argument must be passed (can be the id of a host or a Host object).
	"""
```

```python
def modify_host(self, host, description='new description'):
	"""
	Modifies description of a specific host.
	Host argument must be provided (can be an id or a Host object).
	Returns a Host object.
	"""
```
