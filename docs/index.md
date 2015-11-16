# UpCloud-python-api Documentation

This is the documentation for the newest version of the client. For older versions,
please download the correct source from [here](https://github.com/UpCloudLtd/upcloud-python-api/releases) and use `mkdocs` to build the documentation.

Reading this documentation and using UpCloud-python-api requires that you are familiar with [UpCloud's API v1.2 documentation](https://www.upcloud.com/api/). Additionally, the documentation also assumes that the user refers to the source code, which is well commented and documented with Python's docstrings, for more detailed information.

If you haven't used UpCloud's API before, please see [Getting Started With UpCloud’s API](https://www.upcloud.com/support/getting-started-with-upclouds-api/)

The documentation is divided into two parts. Usage describes the basic CRUD functionality for the object representations of Server, Storage and IP-address. The CloudManager describes the API for performing direct API calls.


The code examples use the following:

```python
import upcloud_api
from upcloud_api import Storage
from upcloud_api import Server
from upcloud_api import ZONE

manager = upcloud_api.CloudManager("username", "password")
```
