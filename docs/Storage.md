The code examples use the following:

```python
import upcloud_api
from upcloud_api import Storage
from upcloud_api import ZONE

manager = upcloud_api.CloudManager("username", "password")
```

# About

Storages are entirely separate from Servers and can be attached/detached from them. Storages can be created, updated and destroyed separately from servers. They can be loaded as CDROMs or disks and they can be cloned to create a new Storage that is a 1:1 clone of another one.


### Tiers

UpCloud offers MaxIOPS (Extremely fast 100k IOPS Storage) and HDD storages. Older disks may still be on our SSD but can be moved to MaxIOPS by cloning.

```
Tiers:
	"maxiops", "hdd", ( "ssd" )
```

### Templates

Public templates such as the Ubuntu 14.04 can be cloned by anyone to get a pre-installed server image that is immediately ready to go. A user can also create private templates for themselves out of any storage. Storages can be cloned from templates during server creation.

## List / Get

CloudManager returns Storage instances.

```python

manager.get_storages()
manager.get_storage(storage.uuid)

```

`get_storages()` accepts one of the following parameters to filter the query:
```
Storages list filters:
	"normal" (default), "public", "private",
	"backup", "cdrom", "template", "favorite"
```

## Create

Storage can be created with the CloudManager's `.create_storage(size=10, tier="maxiops", title="Storage disk", zone="fi-hel1")`


```python

storage1 = manager.create_storage(	size=10,
									tier="maxiops",
									title="my storage disk",
									zone=ZONE.Helsinki )

storage2 = manager.create_storage(100, zone=ZONE.Helsinki)

```


## Update

Only the size and title of a storage can be updated. Please note that size can not be reduced and that OS level actions are required to account for the increased size.

```python

storage = manager.get_storage(uuid)
storage.update(size=100, title="new title")

```

## Destroy

Warning: data loss is permanent.

```python

storage.destroy()

```
