from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from upcloud_api import Storage, StorageImport
from upcloud_api.utils import get_raw_data_from_file


class StorageManager(object):
    """
    Functions for managing Storage disks. Intended to be used as a mixin for CloudManager.
    """

    def get_storages(self, storage_type='normal'):
        """
        Return a list of Storage objects from the API.

        Storage types: public, private, normal, backup, cdrom, template, favorite
        """
        res = self.get_request('/storage/' + storage_type)
        return Storage._create_storage_objs(res['storages'], cloud_manager=self)

    def get_templates(self):
        """
        Return a list of Storages that are templates in a dict with title as key and uuid as value.
        """
        templates = []
        res = self.get_request('/storage/template')
        for item in res.get('storages').get('storage'):
            templates.append({item.get('title'): item.get('uuid')})
        return templates

    def get_storage(self, storage):
        """
        Return a Storage object from the API.
        """
        res = self.get_request('/storage/' + str(storage))
        return Storage(cloud_manager=self, **res['storage'])

    def create_storage(self, size=10, tier='maxiops', title='Storage disk', zone='fi-hel1', backup_rule={}):
        """
        Create a Storage object. Returns an object based on the API's response.
        """
        body = {
            'storage': {
                'size': size,
                'tier': tier,
                'title': title,
                'zone': zone,
                'backup_rule': backup_rule
            }
        }
        res = self.post_request('/storage', body)
        return Storage(cloud_manager=self, **res['storage'])

    def _modify_storage(self, storage, size, title, backup_rule={}):
        body = {'storage': {}}
        if size:
            body['storage']['size'] = size
        if title:
            body['storage']['title'] = title
        if backup_rule:
            body['storage']['backup_rule'] = backup_rule
        return self.put_request('/storage/' + str(storage), body)

    def modify_storage(self, storage, size, title, backup_rule={}):
        """
        Modify a Storage object. Returns an object based on the API's response.
        """
        res = self._modify_storage(str(storage), size, title, backup_rule)
        return Storage(cloud_manager=self, **res['storage'])

    def delete_storage(self, UUID):
        """
        Destroy a Storage object.
        """
        return self.delete_request('/storage/' + UUID)

    def clone_storage(self, storage, title, zone, tier=None):
        """
        Clones a Storage object. Returns an object based on the API's response.
        """
        body = {'storage': {'title': title, 'zone': zone}}
        if tier:
            body['storage']['tier'] = tier
        res = self.post_request('/storage/{0}/clone'.format(str(storage)), body)
        return Storage(cloud_manager=self, **res['storage'])

    def cancel_clone_storage(self, storage):
        """
        Cancels a running cloning operation and deletes the incomplete copy.
        """
        return self.post_request('/storage/{0}/cancel'.format(str(storage)))

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

        url = '/server/{0}/storage/attach'.format(server)
        res = self.post_request(url, body)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def detach_storage(self, server, address):
        """
        Detach a Storage object to a Server. Return a list of the server's storages.
        """
        body = {'storage_device': {'address': address}}
        url = '/server/{0}/storage/detach'.format(server)
        res = self.post_request(url, body)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def load_cd_rom(self, server, address):
        """
        Loads a storage as a CD-ROM in the CD-ROM device of a server.
        """
        body = {'storage_device': {'storage': address}}
        url = '/server/{0}/cdrom/load'.format(server)
        res = self.post_request(url, body)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def eject_cd_rom(self, server):
        """
        Ejects the storage from the CD-ROM device of a server.
        """
        url = '/server/{0}/cdrom/eject'.format(server)
        res = self.post_request(url)
        return Storage._create_storage_objs(res['server']['storage_devices'], cloud_manager=self)

    def create_storage_backup(self, storage, title):
        """
        Creates a point-in-time backup of a storage resource.
        """
        url = '/storage/{0}/backup'.format(storage)
        body = {'storage': {'title': title}}
        res = self.post_request(url, body)
        return Storage(cloud_manager=self, **res['storage'])

    def restore_storage_backup(self, storage):
        """
        Restores the origin storage with data from the specified backup storage.
        """
        url = '/storage/{0}/restore'.format(storage)
        return self.post_request(url)

    def templatize_storage(self, storage, title):
        """
        Creates an exact copy of an existing storage resource which can be used as a template for creating new servers.
        """
        url = '/storage/{0}/templatize'.format(storage)
        body = {'storage': {'title': title}}
        res = self.post_request(url, body)
        return Storage(cloud_manager=self, **res['storage'])

    def create_storage_import(self, storage, source, source_location=None):
        """
        Creates an import task to import data into an existing storage.
        Source types: http_import or direct_upload.
        """
        url = '/storage/{0}/import'.format(storage)
        body = {'storage_import': {'source': source}}
        if source_location:
            body['storage_import']['source_location'] = source_location
        res = self.post_request(url, body)
        return StorageImport(**res['storage_import'])

    def upload_file_for_storage_import(self, storage_import, file):
        """
        Uploads a file directly to UpCloud's uploader session.
        """
        url = storage_import.direct_upload_url
        data = get_raw_data_from_file(file)
        body = {'data': data}
        return self.put_request(url, body, timeout=600, request_to_api=False)

    def get_storage_import_details(self, storage):
        """
        Returns detailed information of an ongoing or finished import task.
        """
        url = '/storage/{0}/import'.format(storage)
        res = self.get_request(url)
        return StorageImport(**res['storage_import'])

    def cancel_storage_import(self, storage):
        """
        Cancels an ongoing import task.
        """
        url = '/storage/{0}/import/cancel'.format(storage)
        res = self.post_request(url)
        return StorageImport(**res['storage_import'])
