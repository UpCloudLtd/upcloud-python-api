The examples use the following:
```python
import upcloud_api
from upcloud_api import Server
from upcloud_api import Storage
from upcloud_api import ZONE

manager = upcloud_api.CloudManager("username", "password")
```

# Start / Stop / Restart

```python

server.stop()
server.start()
server.restart()

# populate the object with updated information from API
server.populate()

```

Please note that the server might not be stopped/started/restarted immediately when the API responds. The `.populate()` method updates the object's fields from the API and is thus useful for checking `server.state`.

```
Server states:
	"started","stopped" -- server is shut down or running
	"maintenance" 		-- when shutting down or (re)starting
	"error" 			-- erronous state in UpCloud's backend
```



## List / Get

The CloudManager returns Server instances.

```python

servers = manager.get_servers()
server = manager.get_server(servers[0].uuid)

```

## Create

Creation of servers in the API is handled by the CloudManager. It accepts a Server instance, forms the correct POST request and populates the Server instance's fields from the POST response.

```python

server = Server(
			core_number = 1,
			memory_amount = 512,
			hostname = "web1.example.com",
			zone = ZONE.London,
			storage_devices = [
				Storage(os = "Ubuntu 14.04", size=10),
				Storage(size=10, tier="hdd")
			])

manager.create_server( server )

```

Currently available Storage operating systems are the following UpCloud public templates:

```python
# upcloud_api/tools.py

Operating Systems:
	"CentOS 6.5", "CentOS 7.0",
	"Debian 7.8", "Ubuntu 12.04", "Ubuntu 14.04",
	"Windows 2003", "Windows 2008", "Windows 2012"

```


Please refer to the [API documentation](https://www.upcloud.com/static/downloads/upcloud-apidoc-1.1.1.pdf) for the allowed Server attributes.

## Update

### Attributes

Updating a Server's attributes is done with its `.save()` method that does a PUT request. If you want to manage the Server's Storages or IP-addresses, see below.

```python

server = manager.get_server( uuid )
server.core_number = 4
server.memory_amount = 4096
server.save()

```

The following fields of Server instance may be updated, all other fields are read-only. Trying to assign values to other fields leads to an error.

```python
Updateable attributes:
	"boot_order", "core_number", "firewall", "hostname", "memory_amount",
	"nic_model", "title", "timezone", "video_model", "vnc", "vnc_password"
```

Please refer to the [API documentation](https://www.upcloud.com/static/downloads/upcloud-apidoc-1.1.1.pdf) for the allowed values.

### Storages

A Server's Storages can be attached and detached with `.add_storage()` and `.remove_storage()`. Both requests issue an API request instantly.

```python

# attach
storage = manager.create_storage( size=100, zone=ZONE.Helsinki )
server.add_storage(storage)

# detach
storage = server.storage_devices[1]
server.remove_storage(storage)

```

### IP-addresses

A Server's Storages can be attached and detached with `.add_IP()` and `.remove_IP()`. Both requests issue an API request instantly. Note that the attached IP is allocated randomly as UpCloud's does not (yet) support floating IPs.

```python

# attach
IP = server.add_IP()

# detach
server.remove_IP(IP)

```

## Destroy

Destroys the Server instance and its IP-addresses. However, does not destroy the Storages.

```python

server.destroy()

```
