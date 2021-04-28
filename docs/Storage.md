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

storage1 = manager.create_storage(
    zone='fi-hel1',
    size=10,
	tier="maxiops",
	title="my storage disk"
)

storage2 = manager.create_storage(zone='de-fra1', size=100)

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

## Import

Storages can be imported either by passing a URL or by uploading the file. Currently .iso, .raw and .img formats
are supported. Other formats like qcow2 or vmdk should be converted before uploading.

Uploaded storage is expected to be uncompressed. It is possible to upload zip (`application/gzip`)
or gzip (`application/x-xz`) compressed files, but you need to specify a separate `content_type`
when calling the `upload_file_for_storage_import` function.

Warning: size of the import cannot exceed the size of the storage. The data will be written starting from
the beginning of the storage, and the storage will not be truncated before starting to write.

Storages can be uploaded by providing a URL.
```python

new_storage = manager.create_storage(size=20, zone='nl-ams1')
storage_import = manager.create_storage_import(
    storage=new_storage.uuid,
    source='http_import',
    source_location='https://username:password@example.server/path/to/data.raw',
)

import_details = manager.get_storage_import_details(new_storage.uuid)

```

Other way is to upload a storage directly. Note that unlike with URLs, file upload will block until it has been
fully uploaded.
```python

new_storage = manager.create_storage(size=20, zone='de-fra1', title='New imported storage')
storage_import = manager.create_storage_import(storage=new_storage.uuid, source='direct_upload')

manager.upload_file_for_storage_import(
    storage_import=storage_import,
    file='/path/to/your/storage.img',
)

import_details = manager.get_storage_import_details(new_storage.uuid)

```

Ongoing imports can also be cancelled:
```python

manager.cancel_storage_import(new_storage.uuid)

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
