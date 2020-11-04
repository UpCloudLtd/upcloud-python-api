The code examples use the following:

```python
import upcloud_api
from upcloud_api import Storage

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

Public templates such as the 01000000-0000-4000-8000-000030060200 can be cloned by anyone to get a pre-installed server image that is immediately ready to go. A user can also create private templates for themselves out of any storage. Storages can be cloned from templates during server creation.

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
									zone='fi-hel1' )

storage2 = manager.create_storage(100, zone='fi-hel1')

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


## Clone

Clone the storage using StorageManager.
Returns an object based on the API's response.
Method requires title and zone to be passed while tier is optional.

```python

storage_clone = storage.clone(title='title of storage clone', zone='fi-hel1', tier=None)

```


## Cancel clone operation

Cancels a running cloning operation and deletes the incomplete copy using StorageManager.
Needs to be called from the cloned storage (object returned by clone operation) and not the storage that is being cloned.

```python

storage_clone.cancel_cloning()

```


## Create backup

Creates a point-in-time backup of a storage resource using StorageManager.
Method requires title to be passed.

```python

storage_backup = storage.create_backup('Backup title')

```


## Restore backup

Restores the origin storage with data from the specified backup storage using StorageManager.
Must be called from a storage object created by create_backup and not the original one.

```python

storage_backup.restore_backup()

```


## Templatize storage

Creates an exact copy of an existing storage resource which can be used as a template for creating new servers using StorageManager.
Method requires title to be passed.

```python

storage.templatize('Template title')

```
