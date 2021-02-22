[![Build Status](https://travis-ci.org/UpCloudLtd/upcloud-python-api.svg?branch=master)](https://travis-ci.org/UpCloudLtd/upcloud-python-api) [![Code Health](https://landscape.io/github/UpCloudLtd/upcloud-python-api/master/landscape.svg?style=flat)](https://landscape.io/github/UpCloudLtd/upcloud-python-api/master) [![PyPI version](https://badge.fury.io/py/upcloud-api.svg)](https://badge.fury.io/py/upcloud-api) [![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/UpCloudLtd/upcloud-python-api/blob/master/LICENSE)

# UpCloud's Python API Client
OOP-based api client for [UpCloud's API](https://developers.upcloud.com/1.3/). Features most of the API's functionality and some convenience functions that combine several API endpoints and logic.

Please test all of your use cases thoroughly before actual production use. Using a separate UpCloud account for testing / developing the client is recommended.

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


**Supported versions in the next release** (offline tests pass with tox):

* <del>python 2.6</del> removed due to deprecation
* python 2.7 supported but not recommended, especially when upcloud-ansible will be ported to python3
* <del>python 3.2</del> removed due to python2/3 support
* <del>python 3.3</del> removed due to python2/3 support
* <del>python 3.4</del> removed due to python2/3 support
* <del>python 3.5</del> removed due to python2/3 support
* python 3.6
* python 3.7
* python 3.8
* python 3.9
* pypi3

**Changelog:**
* See the [Releases page](https://github.com/UpCloudLtd/upcloud-python-api/releases)

## Examples

Note that the API finishes the request before the server is shutdown. Poll the server details to monitor server status.
You must take this into account in your automations.

### Defining and creating Servers

```python

import upcloud_api
from upcloud_api import Server, Storage, login_user_block

manager = upcloud_api.CloudManager('api_user', 'password')
manager.authenticate()


login_user = login_user_block(
    username='theuser',
    ssh_keys=['ssh-rsa AAAAB3NzaC1yc2EAA[...]ptshi44x user@some.host'],
    create_password=False
)

cluster = {
    'web1': Server(
        core_number=1, # CPU cores
        memory_amount=1024, # RAM in MB
        hostname='web1.example.com',
        zone='uk-lon1', # All available zones with ids can be retrieved by using manager.get_zones()
        storage_devices=[
            # OS: 01000000-0000-4000-8000-000030060200, all available os templates can be retrieved by calling manager.get_templates()
            # default tier: maxIOPS, the 100k IOPS storage backend
            Storage(os='01000000-0000-4000-8000-000030060200', size=10),
            # secondary storage, hdd for reduced cost
            Storage(size=100, tier='hdd')
        ],
        login_user=login_user  # user and ssh-keys
    ),
    'web2': Server(
        core_number=1,
        memory_amount=1024,
        hostname='web2.example.com',
        zone='uk-lon1',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030060200', size=10),
            Storage(size=100, tier='hdd'),
        ],
        login_user=login_user
    ),
    'db': Server(
        plan='2xCPU-4GB', # use a preconfigured plan, instead of custom
        hostname='db.example.com',
        zone='uk-lon1',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030060200', size=10),
            Storage(size=100),
        ],
        login_user=login_user
    ),
    'lb': Server(
        core_number=2,
        memory_amount=1024,
        hostname='balancer.example.com',
        zone='uk-lon1',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030060200', size=10)
        ],
        login_user=login_user
    )
}

for server in cluster:
    manager.create_server(cluster[server]) # automatically populates the Server objects with data from API

```

Servers can be defined as dicts without using Server or Storage classes.
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

As the success of server.start() or server.destroy() and storage.destroy()
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

server = cluster['web1']
server.shutdown()
server.core_number = 4
server.memory_amount = 4096
server.save()
server.start()

```


### Clone a server

Cloning is done by giving existing storage uuid to storage_devices. Note that size of the storage
must be defined and must be at least same size than storage being cloned.

```python
clone = Server(
    core_number=1,
    memory_amount=1024,
    hostname='cloned.server',
    zone='fi-hel1',
    storage_devices=[
        Storage(
            uuid='012bea57-0f70-4194-82d0-b3d25f4a018b',
            size=50  # size must be defined and it has to be at least same size than storage being cloned
        ),
    ]
)

manager.create_server(clone)
```

### Easy access to servers and their information:
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
ip_addrs    = manager.get_ips()
ip_addr     = manager.get_ip(address) # e.g server1.ip_addresses[0].address

```

## Tests

Set up environment and install dependencies:

```
# run at project root, python3 and virtualenv must be installed
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt && pip install -r requirements-dev.txt
```

Install the package in editable mode, as mentioned in
[https://docs.pytest.org/en/stable/goodpractices.html](https://docs.pytest.org/en/stable/goodpractices.html)

```python
# run at project root
pip install -e .
```

Tests located in `project_root/test/` directory. Run with:

```python
py.test test/
```

To test against all supported python versions, run:

```python
tox
```

To check for possible vulnerabilities in python packages, run:

```python
safety check
```

The project also supplies a small test suite to test against the live API at `test/live_test.py`. This suite is NOT run with `py.test` as it will permanently remove all resources related to an account. It should only be run with a throwaway dev-only account when preparing for a new release. It is not shipped with PyPI releases. See source code on how to run the live tests.

## Bugs, Issues, Problems, Ideas

Feel free to open a new issue : )
