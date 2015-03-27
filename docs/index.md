# UpCloud-python-api Documentation

Reading this documentation and using UpCloud-python-api requires that you are familiar with [UpCloud's API v1.1 documentation](https://www.upcloud.com/static/downloads/upcloud-apidoc-1.1.1.pdf). Additionally, the documentation also assumes that the user refers to the source code, which is well commented and documented with Python's docstrings, for more detailed information.

If you haven't used UpCloud's API before, please see [Getting Started With UpCloud’s API](https://www.upcloud.com/support/getting-started-with-upclouds-api/)

The documentation is divided into two parts. Usage describes the basic CRUD functionality for the object representations of Server, Storage and IP-address. The CloudManager describes the API for performing direct API calls.


The code examples use the following:

```python
import upcloud
from upcloud import Storage
from upcloud import Server
from upcloud import ZONE

manager = upcloud.CloudManager("username", "password")
```