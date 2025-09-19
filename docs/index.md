# UpCloud's Python API Documentation

This is the documentation for the newest version of the library. For older versions,
please download the correct source from [releases](https://github.com/UpCloudLtd/upcloud-python-api/releases)
and use `mkdocs` to build the documentation.

This documentation includes many code examples for administrating resources on top of UpCloud.
In some cases it can help to be familiar with [UpCloud's API v1.3 documentation](https://www.upcloud.com/api/).
The code itself also has commentary & examples and is structured similarly to this documentation.

The documentation is divided into two parts. Usage describes the basic CRUD functionality for the object
representations of different UpCloud resources (servers, storages, networks etc). The CloudManager describes
the API for performing direct API calls.

Python package `upcloud_api` must be installed before any code examples can be tried.

```bash
pip3 install upcloud-api
```

NOTE: Support for Python 2.7 ended with version 1.0.1. If you need to use it, a supporting version can be
installed with `pip install upcloud-api==1.0.1`.

Many code examples assume that CloudManager object has already been initialized.
In addition to CloudManager, some resources might be needed to be imported.
Full example of imports is below.

```python
import upcloud_api
from upcloud_api import Storage
from upcloud_api import Server
from upcloud_api import FirewallRule
from upcloud_api import Network
from upcloud_api import IPAddress

manager = upcloud_api.CloudManager("username", "password")
```
