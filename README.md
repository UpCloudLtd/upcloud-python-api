# UpCloud's Python API Client
OOP-based api client for [UpCloud's API](https://www.upcloud.com/documentation/api/). Features most of the API's functionality and some convenience functions that combine several API endpoints and logic.

NOTE: This Python client is still evolving. Please test all of your use cases thoroughly before actual production use. Using a separate UpCloud account for testing / developing the client is recommended.

## Installation

```
pip install upcloud-api
```

Alternatively, if you want the newest master or a devel branch - clone the project and run:
```
python setup.py install
```

**!! SSL security update for python 2 !!**
* short story: `pip install requests[security]` should solve all of your problems.
* long story:
	* upcloud-python-api uses [requests](http://docs.python-requests.org/en/latest/)
	  for HTTP(S) that in turn uses [urllib3](https://urllib3.readthedocs.org/en/latest/)
	* urllib3 may detect that your python2.x's SSL is lacking as described
	  [here](https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning) and
	  [here](https://urllib3.readthedocs.org/en/latest/security.html#pyopenssl).
	* you may also be interested in (especially if `requests[security]` did not work for you on Ubuntu)
	  [http://stackoverflow.com/questions/29099404/ssl-insecureplatform-error-when-using-requests-package]
	  (http://stackoverflow.com/questions/29099404/ssl-insecureplatform-error-when-using-requests-package)


**Supported versions as of 0.3.3** (offline tests pass with tox):

* python 2.6
* python 2.7
* <del>python 3.2</del> removed due to python2/3 support
* python 3.3
* python 3.4
* python 3.5
* pypi3  2.4.0

## Features
* OOP based management of Servers, Storages and IP-addresses with full CRUD.
	* since 0.2: manage both IPv4 and IPv6 addresses
	* since 0.1.1: can use custom storage templates in addition to public templates
* Clear way to define your infrastructure, emphasis on clear and easy syntax
* Access all the data of the objects ( e.g. ssh credentials )
* Scale horizontally by creating / destroying servers
* Scale vertically by changing the RAM, CPU, storage specs of any server
* Manage firewall (on/off and individual rules)
	* since 0.2: full management of firewall rules

**TODO:**
* Cloning of storages
* Full management of special storage types:
  * CDROMs, custom OS templates
  * (custom templates can already be cloned to a disk via UUID)
* Full management of backups (instant and scheduled)

**Changelog:**
* See the [Releases page](https://github.com/UpCloudLtd/upcloud-python-api/releases)

**Documentation:**
* Available [here](http://upcloudltd.github.io/upcloud-python-api/)



## Examples

Note that some operations are not instant, for example a server is not fully shut down when the API responds.
You must take this into account in your automations.

### Defining and creating Servers

```python

import upcloud_api
from upcloud_api import Server, Storage, ZONE

manager = upcloud_api.CloudManager('api_user', 'password')
manager.authenticate() # test credentials

cluster = {
    'web1': Server(
        core_number = 1, # CPU cores
        memory_amount = 512, # RAM in MB
        hostname = 'web1.example.com',
        zone = ZONE.London, # ZONE.Helsinki and ZONE.Chicago available also
        storage_devices = [
            # OS: Ubuntu 14.04 from template
            # default tier: maxIOPS, the 100k IOPS storage backend
            Storage(os = 'Ubuntu 14.04', size = 10),
            # secondary storage, hdd for reduced cost
            Storage(size = 100, tier = 'hdd')
        ]
    ),
    'web2': Server(
        core_number = 1,
        memory_amount = 512,
        hostname = 'web2.example.com',
        zone = ZONE.London,
        storage_devices = [
            Storage(os = 'Ubuntu 14.04', size = 10),
            Storage(size = 100, tier = 'hdd'),
        ]
    ),
    'db': Server(
        plan = '2xCPU-2GB' # use a preconfigured plan, instead of custom
        hostname = 'db.example.com',
        zone = ZONE.London,
        storage_devices = [
            Storage(os = 'Ubuntu 14.04', size = 10),
            Storage(size = 100),
        ]
    ),
    'lb': Server(
        core_number = 2,
        memory_amount = 1024,
        hostname = 'balancer.example.com',
        zone = ZONE.London,
        storage_devices = [
            Storage(os = 'Ubuntu 14.04', size = 10)
        ]
    )
}

for server in cluster:
  manager.create_server(cluster[server]) # automatically populates the Server objects with data from API

```

New in 0.3.0: servers can now be defined as dicts without using Server or Storage classes.
The syntax/attributes are exactly like above and under the hood they are converted to Server and Storage classes.
This feature is mainly for easier usage of the module from Ansible, but may provide useful elsewhere.


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

New in 0.3.0: as the success of server.start() or server.destroy() and storage.destroy()
depend on the Server's `state`, new helpers have been added. The helpers may be called regardless of
the server's current state.

```python
# makes sure that the server is stopped (blocking wait) and then destroys the server and its storages
server.stop_and_destroy()

# makes sure that the server is started (blocking wait)
server.ensure_started()
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

### Easy access to servers and their information:

New in 0.3.0.

```python

# returns a public IPv4 (preferred) IPv6 (no public IPv4 was attached) address
server.get_public_ip()

# returns a JSON serializable dict with the server's information (storages and ip-addresses included)
server.to_dict()

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

To test against all supported python versions, run:

```python
tox
```

The project also supplies a small test suite to test against the live API at `test/live_test.py`. This suite is NOT run with `py.test` as it will permanently remove all resources related to an account. It should only be run with a throwaway dev-only account when preparing for a new release. It is not shipped with PyPI releases. See source code on how to run the live tests.

## Bugs, Issues, Problems, Ideas

Feel free to open a new issue : )

## Documentation

Documentation available [here](http://upcloudltd.github.io/upcloud-python-api/)
