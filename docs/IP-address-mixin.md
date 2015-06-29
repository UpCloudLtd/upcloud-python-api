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
def get_IP(self, address):
	"""
	Get an IP_address object with the IP address (string) from the API.
	e.g manager.get_IP("80.69.175.210")
	"""
```

```python
def get_IPs(self):
	"""
	Get all IP_address objects from the API.
	"""
```

```python
def attach_IP(self, server, family="IPv4"):
	"""
	Attach a new (random) IP_address to the given server (object or UUID)
	"""
```
```python
def modify_IP(self, IP_addr, ptr_record):
	"""
	Modify an IP address' ptr-record (Reverse DNS).
	Accepts an IP_address instance (object) or its address (string).
	"""
```

```python
def release_IP(self, IP_addr):
	"""
	Destroy an IP_address. Returns an empty object.
	Accepts an IP_address instance (object) or its address (string).
	"""
```
