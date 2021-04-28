from typing import Optional, Union

from upcloud_api.api import API
from upcloud_api.storage import Storage
from upcloud_api.storage_import import StorageImport
from upcloud_api.utils import get_raw_data_from_file


class StorageManager:
    """
    Functions for managing Storage disks. Intended to be used as a mixin for CloudManager.
    """

    api: API

    def get_storages(self, storage_type='normal'):
        """
        Return a list of Storage objects from the API.

        Storage types: public, private, normal, backup, cdrom, template, favorite
        """
        res = self.api.get_request('/storage/' + storage_type)
        return Storage._create_storage_objs(res['storages'], cloud_manager=self)

    def get_templates(self):
        """
        Return a list of Storages that are templates in a dict with title as key and uuid as value.
        """
        templates = []
        res = self.api.get_request('/storage/template')
        for item in res.get('storages').get('storage'):
            templates.append({item.get('title'): item.get('uuid')})
        return templates

    def get_storage(self, storage: str) -> Storage:
        """
        Return a Storage object from the API.
        """
        res = self.api.get_request('/storage/' + str(storage))
        return Storage(cloud_manager=self, **res['storage'])

    def create_storage(
        self,
        size: int = 10,
        tier: str = 'maxiops',
        title: str = 'Storage disk',
        zone: str = 'fi-hel1',
        backup_rule: Optional[dict] = None,
    ) -> Storage:
        """
        Create a Storage object. Returns an object based on the API's response.
        """
        if backup_rule is None:
            backup_rule = {}
        body = {
            'storage': {
                'size': size,
                'tier': tier,
                'title': title,
                'zone': zone,
                'backup_rule': backup_rule,
            }
        }
        res = self.api.post_request('/storage', body)
        return Storage(cloud_manager=self, **res['storage'])

    def _modify_storage(self, storage, size, title, backup_rule: Optional[dict] = None):
        body = {'storage': {}}
        if size:
            body['storage']['size'] = size
        if title:
            body['storage']['title'] = title
        if backup_rule:
            body['storage']['backup_rule'] = backup_rule
        return self.api.put_request('/storage/' + str(storage), body)

    def modify_storage(
        self, storage: str, size: int, title: str, backup_rule: Optional[dict] = None
    ) -> Storage:
        """
        Modify a Storage object. Returns an object based on the API's response.
        """
        res = self._modify_storage(str(storage), size, title, backup_rule)
        return Storage(cloud_manager=self, **res['storage'])

    def delete_storage(self, UUID):
        """
        Destroy a Storage object.
        """
        return self.api.delete_request('/storage/' + UUID)

    def clone_storage(
        self, storage: Union[Storage, str], title: str, zone: str, tier=None
    ) -> Storage:
        """
        Clones a Storage object. Returns an object based on the API's response.
        """
        body = {'storage': {'title': title, 'zone': zone}}
        if tier:
            body['storage']['tier'] = tier
        # TODO: `str(storage)` seems unsafe
        res = self.api.post_request(f'/storage/{str(storage)}/clone', body)
        return Storage(cloud_manager=self, **res['storage'])

    def cancel_clone_storage(self, storage):
        """
        Cancels a running cloning operation and deletes the incomplete copy.
        """
        return self.api.post_request(f'/storage/{str(storage)}/cancel')

    def attach_storage(self, server, storage, storage_type, address):
        """
        Attach a Storage object to a Server. Return a list of the server's storages.
        """
        body = {'storage_device': {}}
        if storage:
            body['storage_device']['storage'] = str(storage)

        if storage_type:
            body['storage_device']['type'] = storage_type

        if address:
            body['storage_device']['address'] = address

        url = f'/server/{server}/storage/attach'
        res = self.api.post_request(url, body)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def detach_storage(self, server, address):
        """
        Detach a Storage object to a Server. Return a list of the server's storages.
        """
        body = {'storage_device': {'address': address}}
        url = f'/server/{server}/storage/detach'
        res = self.api.post_request(url, body)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def load_cd_rom(self, server, address):
        """
        Loads a storage as a CD-ROM in the CD-ROM device of a server.
        """
        body = {'storage_device': {'storage': address}}
        url = f'/server/{server}/cdrom/load'
        res = self.api.post_request(url, body)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def eject_cd_rom(self, server):
        """
        Ejects the storage from the CD-ROM device of a server.
        """
        url = f'/server/{server}/cdrom/eject'
        res = self.api.post_request(url)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def create_storage_backup(self, storage: str, title: str) -> Storage:
        """
        Creates a point-in-time backup of a storage resource.
        """
        url = f'/storage/{storage}/backup'
        body = {'storage': {'title': title}}
        res = self.api.post_request(url, body)
        return Storage(cloud_manager=self, **res['storage'])

    def restore_storage_backup(self, storage):
        """
        Restores the origin storage with data from the specified backup storage.
        """
        url = f'/storage/{storage}/restore'
        return self.api.post_request(url)

    def templatize_storage(self, storage: str, title: str) -> Storage:
        """
        Creates an exact copy of an existing storage resource which can be used as a template for creating new servers.
        """
        url = f'/storage/{storage}/templatize'
        body = {'storage': {'title': title}}
        res = self.api.post_request(url, body)
        return Storage(cloud_manager=self, **res['storage'])

    def create_storage_import(
        self, storage: str, source: str, source_location=None
    ) -> StorageImport:
        """
        Creates an import task to import data into an existing storage.
        Source types: http_import or direct_upload.
        """
        url = f'/storage/{storage}/import'
        body = {'storage_import': {'source': source}}
        if source_location:
            body['storage_import']['source_location'] = source_location
        res = self.api.post_request(url, body)
        return StorageImport(**res['storage_import'])

    def upload_file_for_storage_import(self, storage_import, file):
        """
        Uploads a file directly to UpCloud's uploader session.
        """
        # TODO: this should not buffer the entire `file` into memory

        # This is importing and using `requests` directly since there doesn't
        # seem to be a point in adding a `.api.raw_request()` call to the `API` class.
        # That could be changed.

        import requests

        resp = requests.put(
            url=storage_import.direct_upload_url,
            data=get_raw_data_from_file(file),
            headers={'Content-type': 'application/octet-stream'},
            timeout=600,
        )
        resp.raise_for_status()
        return resp.json()

    def get_storage_import_details(self, storage: str) -> StorageImport:
        """
        Returns detailed information of an ongoing or finished import task.
        """
        url = f'/storage/{storage}/import'
        res = self.api.get_request(url)
        return StorageImport(**res['storage_import'])

    def cancel_storage_import(self, storage: str) -> StorageImport:
        """
        Cancels an ongoing import task.
        """
        url = f'/storage/{storage}/import/cancel'
        res = self.api.post_request(url)
        return StorageImport(**res['storage_import'])
