# UpCloud-python-api
Python client for [UpCloud's API](https://www.upcloud.com/documentation/api/).

NOTE: This Python client is still work-in-progress and is not considered production ready.

## Features
* OOP based management of Servers, Storages and IP-addresses with full CRUD.
* Clear way to define your infrastructure, emphasis on clear and easy syntax
* Access all the data of the objects ( e.g. ssh credentials )
* Scale horizontally by creating / destroying servers
* Scale vertically by changing the RAM, CPU, storage specs of any server

**TODO:**
* Cloning of storages
* Full management of special storage types:
  * CDROMs, custom OS templates
  * custom templates can already be cloned to a disk via UUID
* Full management of Firewall rules (per server on/off supported at the moment)
  * defining a server's L2 firewall's rules through the API client
* Full management of backups (instant and scheduled)
* IPv6 support



## Examples

Note that operations are not instant, for example a server is not fully shut down when the API responds. 
You must take this into account in your automations.

### Defining and creating Servers

```python
import upcloud
import upcloud.Server
import upcloud.Storage
import upcloud.ZONE

manager = upcloud.CloudManager("api_user", "password")
manager.authenticate() # test credentials

cluster = {
	"web1": Server( core_number = 1, # CPU cores
					memory_amount = 512, # RAM in MB
					hostname = "web1.example.com", 
					zone = ZONE.London, # Zone.Helsinki and Zone.Chicago available also
					storage_devices = [
				        # OS: Ubuntu 14.04 from template
				        # default tier: maxIOPS, the 100k IOPS storage backend
						Storage(os = "Ubuntu 14.04", size=10), 
						# secondary storage, hdd for reduced cost
						Storage(size=100, tier="hdd") 
					]),
	
	"web2": Server( core_number = 1, 
					memory_amount = 512, 
					hostname = "web2.example.com", 
					zone = ZONE.London, 
					storage_devices = [
						Storage(os = "Ubuntu 14.04", size=10), 
						Storage(size=100, tier="hdd"),
					]),

	"db":	Server( core_number = 2, 
					memory_amount = 2048, 
					hostname = "db.example.com", 
					zone = ZONE.London, 
					storage_devices = [
						Storage(os = "Ubuntu 14.04", size=10),
						Storage(size=100),
					]),

	"lb":	Server( core_number = 2, 
					memory_amount = 1024, 
					hostname = "balancer.example.com", 
					zone = ZONE.London, 
					storage_devices = [
						Storage(os = "Ubuntu 14.04", size=10)
					])
}

for server in cluster:
  manager.create_server( server ) # automatically populates the Server objects with data from API

```

### Stop / Start / Destroy Servers
```python

for server in cluster:
	server.shutdown()
	# OR: 
	server.start()
	# OR: 
	server.destroy()
	for storage in server.storage_devices: 
	  storage.destroy()
	  
```

### Upgrade a Server
```python

server = cluster["web1"]
server.shutdown()
server.core_number = 4
server.memory_amount = 4096
server.save()
server.start()

```

### GET resources:
```python

servers     = manager.get_servers()
server1     = manager.get_server(UUID) # e.g servers[0].uuid
storages    = manager.get_storages()
storage1    = manager.get_storage(UUID) # e.g sever1.storage_devices[0].uuid
ip_addrs    = manager.get_IPs()
ip_addr     = manager.get_IP(address) # e.g server1.ip_addresses[0].address

```

## Tests

Tests located in `project_root/tests/` directory. Run with:

```python
py.test tests/
```

## Documentation

Documentation available [here](http://upcloudltd.github.io/upcloud-python-api/)
