# UpCloud-python-api
Python client for [UpCloud's API](https://www.upcloud.com/documentation/api/).

NOTE: This Python client is still work-in-progress and is not considered production ready.

## Installation

```
pip install --pre upcloud-api-python

# with older pip:
pip install upcloud-api-python
```

Alternatively, clone the project and run
```
python setup.py install
```

**Supported versions** (offline tests pass with tox):

* python 3.2
* python 3.3 
* python 3.4
* python 3.5
* pypi3  2.4.0

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
from upcloud import Server, Storage, ZONE

manager = upcloud.CloudManager("api_user", "password")
manager.authenticate() # test credentials

cluster = {
	"web1": Server( core_number = 1, # CPU cores
					memory_amount = 512, # RAM in MB
					hostname = "web1.example.com",
					zone = ZONE.London, # ZONE.Helsinki and ZONE.Chicago available also
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
  manager.create_server( cluster[server] ) # automatically populates the Server objects with data from API

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

Set up environment and install dependencies:

```
# run at project root, python3 and virtualenv must be installed
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Install the package in editable mode, as mentioned in
[https://pytest.org/latest/goodpractises.html](https://pytest.org/latest/goodpractises.html)

```python
# run at project root
pip install -e .
```

Tests located in `project_root/tests/` directory. Run with:

```python
py.test tests/
```

To test against python3.2=< and pypy3-2.4.0, run:

```python
tox
``` 

The project also supplies a small test suite to test against the live API at `test/live_test.py`. This suite is NOT run with `py.test` as it will permanently remove all resources related to an account. It should only be run with a throwaway dev-only account when preparing for a new release. It is not shipped with PyPI releases. See source code on how to run the live tests.

## Bugs, Issues, Problems, Ideas

Feel free to open a new issue : )

## Documentation

Documentation available [here](http://upcloudltd.github.io/upcloud-python-api/)
