# Changelog

All notable changes to this project will be documented in this file.

Changelog was added with version 2.0.0.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2021-05-05

Python 2 is no longer supported. This is a maintenance release without
that many added features. It was mostly done to make future development easier.

### Added

- Storage upload accepts filenames in strings and PathLike or BinaryIO variables.
- Code style is now guarded by Black, flake8, isort etc.
- Improved documentation and its examples, especially regarding server creation and storage uploads.

### Changed

- Huge amount of fixups in project tests, style and imports by [akx](https://github.com/akx). Thank you! :heart:
- Zone default from storage creation has been removed, making zone a required variable with `create_storage()`.
- Passwords for server user are not created by default if SSH keys are provided.
- Tests and deployments moved fully from CircleCI to GitHub Actions.
- Fixed storage upload not reading the file into memory before uploading.
- Moved to fully using setup.cfg instead of requirements.txt.

### Removed

- Python 2 support.

----

## [1.0.1] - 11 Feb 2021

### Fixed

- long description for PyPi

----

## [1.0.0] - 11 Feb 2021

### Added

- Features: Object Storage, Network, router, hosts
- user-agent to follow usage trend
- Storage methods clone #6 , templatize, import, favorite and backup #5
- tests

### Changed

- Breaking: Update to UpCloud API 1.3
- Breaking: Update supported Python versions
- Python 2.7 and Python >3.6
- Breaking: Update dependencies
- Move from travis to github actions

### Fixed

- Fetch Zones and templates from API
- Refactoring
- Update Readme

----

## [0.4.6] - 28 Aug 2020

- Support for new templates: CentOS 8.0 and Ubuntu 20.04
- Removed obsolete templates
- Added US-NYC1 zone constant

----

## [0.4.5] - 3 Dec 2019

Template updates.

----

## [0.4.3] - 3 Dec 2018

- Python 3.3 deprecated
- Zone San Jose added
- Template Ubuntu 18.04 added

----

## [0.4.2] - 22 Feb 2018

- Added missing zones and missing templates.
- Also removed old template windows 2008, which is not supported any more.

----

## [0.4.1] - 2 Feb 2018

- CI fixes
- Small bug fix

----

## [0.4.0] - 1 Feb 2018

...

----

## [0.3.9] - 16 Nov 2016

Note: 0.3.8 was never released at pip / github releases.

- numerous improvements from the 0.4.0 branch #29
- support for creating a server from template

<https://www.upcloud.com/api/8-servers/#creating-from-a-template>

``` python
manager.create_server(
    Server(
        core_number=2,
        memory_amount=1024,
        hostname='my.example.com',
        zone=ZONE.Frankfurt,
        storage_devices=[
            Storage(uuid=UUID, size=10),  # we also support Storage(storage=UUID, size=10)
        ],
    )
)
```

----

## [0.3.7] - 4 Aug 2016

- support for Server.user_data
- improve Server.stop_and_destroy
  - automatically populates server data from api unless sync=False param is given
  - wraps stop and destroy operations in an error handling loop that tries the operations several times in case of API errors related to the resource being in "maintenance" state (servers sometimes go to "maintenance" state when destroying several servers in a row)

----

## [0.3.6] - 18 Jul 2016

- remove `future` dependency
- loosely declare dependencies (`six` and `requests`) with `>=`
- improve `Server.stop_and_destroy` to be more stable
- add Circle-CI integration tests (more work needed though)
- add flake8 and improve code style

----

## [0.3.5] - 1 Jul 2016

Bugfix: allow new Firewall attributes, add comment attribute default

The above fix is necessary for upcloud's firewall ansible module to work.

----

## [0.3.4] - 21 Jun 2016

**Support `avoid_host` and `login_user` features of UpCloud's Servers API.**

```
from upcloud_api.server import Server, login_user_block

Server.avoid_host = <host_id>
Server.login_user = login_user_block(username : String, ssh_keys : List[String], create_password : Bool)
```

Note: username is optional (defaults to `root` in API)

**Improve `Server.get_public_ip(self, addr_family='IPv4', strict=False`)**

<https://github.com/UpCloudLtd/upcloud-python-api/commit/ec16d0ce05b605c8e6e44e1ed57e309020797fa4>

----

## [0.3.3] - 8 Feb 2016

Allow setting timeout via

`manager = upcloud_api.CloudManager('username', 'password', timeout)`

or

`manager.timeout = timeout` (although this should probably be avoided)

where timeout is an integer (seconds) or `None` (forever) or anything accepted by `requests` library as described [here](http://docs.python-requests.org/en/master/user/advanced/?highlight=timeout#timeouts)

----

## [0.3.2] - 30 Nov 2015

Small update, adds functionality to manage preconfigured servers ("fixed plan", see upcloud.com/pricing/)

- `plan` attribute for Server
- `Server.save()` works even if the instance has not been populated from API

----

## [0.3.1] - 20 Jul 2015

Small update introducing Tags

- `Tag` class and `TagManager` mixin for `CloudManager`
- see `upcloud_api/cloud_manager/tag_mixin.py` and `upcloud_api/tag.py`

----

## [0.3.0] - 15 Jul 2015

Major release introducing python2/3 support and several features for Ansible inventory/modules

- **PyPi relase renamed to `upcloud-api`** (`pip install upcloud-api`)
- **Package renamed to `upcloud_api`** (`import upcloud_api`)
- versions supported: 2.6, 2.7, 3.3+
  - drop 3.2 support ([future](https://pypi.python.org/pypi/future) does not support it)
- new convenience functions for Server:
  - server.stop_and_destroy() - wait for server to stop, then destroy it and its storages
  - server.ensure_started() - wait for server to be started
  - server.to_dict()  - JSON serialisable dict including storages an IP-addresses
- password delivery `"none"` by default. (no annoying emails about new servers)
- some code quality improvements, like using strictly absolute imports within the codebase

----

## [0.2.0] - 29 Jun 2015

Major update with new features related to UpCloud's API v1.2

- major change: use UpCloud's API v1.2
- add FirewallRule management (see [documentation](http://upcloudltd.github.io/upcloud-python-api/Firewall/))
- add option to add IPv6 addresses (`server.add_IP("IPv6")`)
- ship files required for running tests with the [PyPI release](https://pypi.python.org/pypi/upcloud-api-python/0.2.0)
- updates to documentation and README.md
- live tests against UpCloud's API - these are NOT shipped with PyPI release as they are extremely dangerous. `py.test` will not run these tests and they require extra confirmation / cloud credentials. This version has been tested manually and automatically against the UpCloud v1.2 API.

----

## [0.1.1] - 23 Jun 2015

Move to X.Y.Z versioning and bump version from 0.1(.0) to 0.1.1

- minor enchancement: Storage OS param can now take a UUID of a OS template. Useful if using custom OS templates.
- bugfix: add cloud_manager to Server object during create_server. 
- added MANIFEST.in, tox.in, setup.cfg and removed docs/html from git (built by mkdocs from md sources)
- sublime project file and some readme.md improvements

----

## [0.1] - 23 Jun 2015

First release, available at https://pypi.python.org/pypi/upcloud-api-python

[Unreleased]: https://github.com/UpCloudLtd/upcloud-python-api/compare/v2.0.0...HEAD
[0.1]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.1
[0.1.1]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.1.1
[0.2.0]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.2.0
[0.3.0]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.0
[0.3.1]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.1
[0.3.2]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.2
[0.3.3]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.3
[0.3.4]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.4
[0.3.5]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.5
[0.3.6]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.6
[0.3.7]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.7
[0.3.8]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.8
[0.3.9]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.3.9
[0.4.0]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.4.0
[0.4.1]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.4.1
[0.4.2]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.4.2
[0.4.3]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v0.4.3
[0.4.5]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/0.4.5
[0.4.6]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/0.4.6
[1.0.0]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v1.0.0
[1.0.1]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v1.0.1
[2.0.0]: https://github.com/UpCloudLtd/upcloud-python-api/releases/tag/v2.0.0
