from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from upcloud_api import Storage


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

    def get_storage(self, storage):
        """
        Return a Storage object from the API.
        """
        res = self.get_request('/storage/' + str(storage))
        return Storage(cloud_manager=self, **res['storage'])

    def create_storage(self, size=10, tier='maxiops', title='Storage disk', zone='fi-hel1'):
        """
        Create a Storage object. Returns an object based on the API's response.
        """
        body = {
            'storage': {
                'size': size,
                'tier': tier,
                'title': title,
                'zone': zone
            }
        }
        res = self.post_request('/storage', body)
        return Storage(cloud_manager=self, **res['storage'])

    def _modify_storage(self, storage, size, title):
        body = {'storage': {}}
        if size:
            body['storage']['size'] = size
        if title:
            body['storage']['title'] = title
        return self.request('PUT', '/storage/' + str(storage), body)

    def modify_storage(self, storage, size, title):
        """
        Modify a Storage object. Returns an object based on the API's response.
        """
        res = self._modify_storage(str(storage), size, title)
        return Storage(cloud_manager=self, **res['storage'])

    def delete_storage(self, UUID):
        """
        Destroy a Storage object.
        """
        return self.request('DELETE', '/storage/' + UUID)

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
