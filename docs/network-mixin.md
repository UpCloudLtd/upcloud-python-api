## About
```python
class NetworkManager():
	"""
	Functions for managing networks. Intended to be used as a mixin for CloudManager.
	"""
```
`NetworkManager` is a mixed into `CloudManager` and the following methods are available through it.

```python
manager = CloudManager("api-username", "password")
manager.method()
```

## Methods

```python
def get_networks(self, zone="fi-hel1"):
	"""
  Get a list of all networks.
  Zone can be passed to return networks in a specific zone but is not mandatory.
	"""
```

```python
def get_network(self, uuid):
	"""
	Retrieves the details of a specific network.
	"""
```

```python
def create_network(
        name='test network',
        zone='fi-hel1',
        address='172.16.0.0/22',
        dhcp='yes',
        family='IPv4',
    ):
	"""
	Creates a new SDN private network that cloud servers from the same zone can be attached to.
  Name, zone, address, dhcp and family arguments are required.
  Router, dhcp_default_route, dhcp_dns, dhcp_bootfile_url and gateway arguments are optional.
  Dhcp and dhcp_default_route accept yes or no (string) as a value.
  Dhcp_dns accepts an array of addresses.
  Returns a Network object.
	"""
```

```python
def modify_network(
        network='036df3d0-8629-4549-984e-dc86fc3fa1b0',
        dhcp='yes',
        family='IPv4',
        router='04b65749-61e2-4f08-a259-c75afbe81abf',
    ):
	"""
	Modifies the details of a specific SDN private network. The Utility and public networks cannot be modified.
  Network, dhcp, family and router arguments are required (router can be an id of a router or a router object, same goes for network).
  Name, router, dhcp_default_route, dhcp_dns, dhcp_bootfile_url and gateway arguments are optional.
  Dhcp and dhcp_default_route accept yes or no (string) as a value.
  Dhcp_dns accepts an array of addresses.
  Returns a Network object.
	"""
```

```python
def delete_network(self, network):
	"""
	Deletes an SDN private network. All attached cloud servers must first be detached before SDN private networks can be deleted.
  Network argument must be provided (can be an id or a Network object).
  Returns an empty response.
	"""
```

```python
def get_server_networks(self, server):
	"""
	List all networks the specific cloud server is connected to.
  Server argument must be passed (can be an id or a Server object).
  Returns a list of Interface objects.

	"""
```

```python
def create_network_interface(
        server='0082c083-9847-4f9f-ae04-811251309b35',
        network='036df3d0-8629-4549-984e-dc86fc3fa1b0',
        type='private',
        ip_addresses=[{'family': 'IPv4', 'address': '172.16.1.10'}]
    ):
	"""
	Creates a new network interface on the specific cloud server and attaches the specified SDN private network to the new interface.
  Server, network, type and ip_addresses arguments must be passed.
  Index, source_ip_filtering and bootable arguments are optional.
  Server and network arguments can be ids or objects.
  Ip_addresses argument must be a list of dicts which contain family and address.
  Index must be an integer.
  Source_ip_filtering and bootable arguments accept a yes or a no string.
  Returns an Interface object.
	"""
```

```python
def modify_network_interface(
        server='0082c083-9847-4f9f-ae04-811251309b35',
        index_in_path=7
    ):
	"""
	Modifies the network interface at the selected index on the specific cloud server.
  Server and index_in_path arguments are mandatory.
  Index_in_body, ip_addresses, source_ip_filtering and bootable arguments are optional.
  Server argument can be an id or an object.
  Index arguments must be integers.
  Ip_addresses argument must be a list of dicts which contain family and address.
  Source_ip_filtering and bootable arguments accept a yes or a no string.
  Returns an Interface object.
	"""
```

```python
def delete_network_interface(self, server, index):
	"""
  Detaches an SDN private network from a cloud server by deleting the network interface at the selected index on the specific cloud server.
  Server and index arguments are mandatory.
  Server argument can be an id or an object.
  Index argument must be an integer.
  Returns an empty response
	"""
```

```python
def get_routers(self):
	"""
  Returns a list of all available routers associated with the current account (list of Router objects).
	"""
```

```python
def get_router(self, uuid):
	"""
  Returns detailed information about a specific router (router object).
  UUID argument is mandatory
	"""
```

```python
def create_router(self, name):
	"""
  Creates a new router.
  Name is a mandatory argument.
  Returns a Router object.
	"""
```

```python
def modify_router(self, router, name):
	"""
	Modify an existing router.
	Router and name arguments are mandatory.
  Router can be an id or a Router object.
  Returns a Router object.
	"""
```

```python
def delete_router(self, router):
	"""
	Delete an existing router.
  Router argument is mandatory.
  Router can be an id or a Router object.
  Returns a Router object.
	"""
```
