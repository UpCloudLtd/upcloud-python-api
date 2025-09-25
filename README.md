# UpCloud's Python API Client

[![test](https://github.com/UpCloudLtd/upcloud-python-api/actions/workflows/main.yml/badge.svg)](https://github.com/UpCloudLtd/upcloud-python-api/actions/workflows/main.yml)
[![PyPI version](https://badge.fury.io/py/upcloud-api.svg)](https://badge.fury.io/py/upcloud-api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/UpCloudLtd/upcloud-python-api/blob/main/LICENSE.txt)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/UpCloudLtd/upcloud-python-api/badge)](https://scorecard.dev/viewer/?uri=github.com%2FUpCloudLtd%2Fupcloud-python-api)

OOP-based API client for [UpCloud's API](https://developers.upcloud.com/1.3/). Includes most of the API
functionality and some convenience functions that combine several API endpoints and logic.

Please test all of your use cases thoroughly before actual production use. Using a separate UpCloud account for
testing / developing the client is recommended.

## Installation

``` bash
pip install upcloud-api
```

Alternatively, if you want the newest (possibly not yet released) stuff, clone the project and run:

``` bash
python setup.py install
```

### Supported Python versions

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- PyPy3

**Python 2 has been deprecated**

- Python 2.7 is no longer supported, but available in older API versions (< v2.0.0).

## Changelog

- Changelog is available [in its own file](CHANGELOG.md)

## Usage

More usage examples are available under [docs/]. If there's a specific thing you're interested in,
but are not able to get working, please [contact UpCloud support](https://upcloud.com/contact/).

### Load credentials from environment

```python
from upcloud_api import CloudManager, Credentials

credentials = Credentials.parse()
c = CloudManager(**credentials.dict)
c.get_account()
```

### Defining and creating servers

```python

import upcloud_api
from upcloud_api import CloudManager, Server, Storage, login_user_block

manager = CloudManager('api_user', 'password')
manager.authenticate()


login_user = login_user_block(
    username='theuser',
    ssh_keys=['ssh-rsa AAAAB3NzaC1yc2EAA[...]ptshi44x user@some.host'],
    create_password=False
)

cluster = {
    'web1': Server(
        plan='2xCPU-4GB',
        hostname='web1.example.com',
        zone='uk-lon1', # All available zones with ids can be retrieved by using manager.get_zones()
        storage_devices=[
            # OS: template storage UUID, all available os templates can be retrieved by calling manager.get_templates()
            # Note: the storage os template uuid:s will change when OS is updated. So check that the UUID is correct
            # default tier: maxIOPS, the 100k IOPS storage backend
            Storage(os='01000000-0000-4000-8000-000030240200', size=10),
            # secondary storage, hdd for reduced speed & cost
            Storage(size=100, tier='hdd')
        ],
        login_user=login_user  # user and ssh-keys
    ),
    'web2': Server(
        plan='2xCPU-4GB',
        hostname='web2.example.com',
        zone='uk-lon1',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030240200', size=10),
            Storage(size=100, tier='hdd'),
        ],
        login_user=login_user
    ),
    'db': Server(
        # use custom resources, instead of a plan
        core_number=12, # CPU cores
        memory_amount=49152, # RAM in MB
        hostname='db.example.com',
        zone='uk-lon1',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030240200', size=10),
            Storage(size=100),
        ],
        login_user=login_user
    ),
    'lb': Server(
        plan='2xCPU-4GB',
        hostname='balancer.example.com',
        zone='uk-lon1',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030240200', size=10)
        ],
        login_user=login_user
    )
}

for server in cluster:
    manager.create_server(cluster[server]) # creates all server objects defined in cluster

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

CloudManager offers mode fine-grained deletion options for servers as you can choose to delete storages and
choose what happens to their backups when deleting the server. By default the storage and their backups are
always preserved.

Following example would delete all storages attached to a server, but would keep the latest backup
of each storage if backups exist.

```python

from upcloud_api.storage import BackupDeletionPolicy

manager.delete_server(uuid, delete_storages=True, backups=BackupDeletionPolicy.KEEP_LATEST)

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

### Clone a new server from existing storage

Cloning is done by giving existing storage uuid to storage_devices. Note that size of the storage
must be defined and must be at least the same size as the storage being cloned.

```python
clone = Server(
    plan='2xCPU-4GB',
    hostname='cloned.server',
    zone='fi-hel1',
    storage_devices=[
        Storage(
            uuid='012bea57-0f70-4154-84d0-b3d25f4a018b',
            size=50  # size must be defined and it has to be at least same size than storage being cloned
        ),
    ]
)

manager.create_server(clone)
```

### Easy access to servers and their information

```python

# returns a public IPv4 (preferred) IPv6 (no public IPv4 was attached) address
server.get_public_ip()

# returns a JSON serializable dict with the server's information (storages and ip-addresses included)
server.to_dict()

```

### Get resources

```python

servers     = manager.get_servers()
server1     = manager.get_server(uuid) # e.g servers[0].uuid
storages    = manager.get_storages()
storage1    = manager.get_storage(uuid) # e.g server1.storage_devices[0].uuid
ip_addrs    = manager.get_ips()
ip_addr     = manager.get_ip(address) # e.g server1.ip_addresses[0].address

```

## Testing

Set up environment and install dependencies:

``` bash
# run at project root, python3 and virtualenv must be installed
virtualenv venv
source venv/bin/activate
```

Install the package in editable mode.

```bash
# run at project root
pip install -e .
```

Tests are located under `test/`. Run with:

```bash
py.test test/
```

To test against all supported python versions, run:

```bash
tox
```


The project also supplies a small test suite to test against the live API in `test/test_integration`.
This suite is NOT run with `py.test` dy default as it will permanently remove all resources related to an account.
It should only be run with a throwaway dev-only account when preparing for a new release. It is not shipped with
PyPI releases. To run the integration tests, append `--integration-tests` flag to the `py.test` command.

## Bugs, Issues, Problems, Ideas

Please report issues and features requests through
[the issues page](https://github.com/UpCloudLtd/upcloud-python-api/issues).
