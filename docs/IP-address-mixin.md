## About

```python
class IPManager():
	"""
	Functions for managing IP-addresses.
	Intended to be used as a mixin for CloudManager.
	"""
```

`IPManager` is a mixed into `CloudManager` and the following methods are available by

```python
manager = CloudManager("api-username", "password")
manager.method()
```

## Methods


```python
def get_ip(self, address):
	"""
	Get an IPAddress object with the IP address (string) from the API.
	e.g manager.get_ip("80.69.175.210")
	"""
```

```python
def get_ips(self):
	"""
	Get all IPAddress objects from the API.
	"""
```

```python
def attach_ip(self, server, family="IPv4"):
	"""
	Attach a new (random) IPAddress to the given server (object or UUID)
	"""
```
```python
def modify_ip(self, ip_addr, ptr_record):
	"""
	Modify an IP address' ptr-record (Reverse DNS).
	Accepts an IPAddress instance (object) or its address (string).
	"""
```

```python
def release_ip(self, ip_addr):
	"""
	Destroy an IPAddress. Returns an empty object.
	Accepts an IPAddress instance (object) or its address (string).
	"""
```
