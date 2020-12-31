from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from upcloud_api import ObjectStorage
from upcloud_api.utils import convert_datetime_string_to_object


class ObjectStorageManager(object):
    """
    Functions for managing Object Storages. Intended to be used as a mixin for CloudManager.
    """

    def get_object_storages(self):
        """
        List all Object Storage devices on the account or those which the subaccount has permissions.
        """
        url = '/object-storage'
        res = self.get_request(url)
        object_storages = [ObjectStorage(**o_s) for o_s in res['object_storages']['object_storage']]
        return object_storages

    def create_object_storage(self, zone, access_key, secret_key, size, name=None, description=None):
        """
        Used to create a new Object Storage device with a given name, size and location.
        """
        url = '/object-storage'
        body = {
            'object_storage': {
                'zone': zone,
                'access_key': access_key,
                'secret_key': secret_key,
                'size': size
            }
        }
        if name:
            body['object_storage']['name'] = name
        if description:
            body['object_storage']['description']= description
        res = self.post_request(url, body)
        return ObjectStorage(cloud_manager=self, **res['object_storage'])

    def get_object_storage(self, uuid):
        """
        A request to get details about a specific Object Storage device by the given uuid.
        """
        url = '/object-storage/{}'.format(uuid)
        res = self.get_request(url)
        return ObjectStorage(cloud_manager=self, **res['object_storage'])

    def modify_object_storage(self, object_storage, access_key=None, secret_key=None, description=None, size=None):
        """
        Modify requests can be used to update the details of an Object Storage including description, access_key and secret_key.
        """
        url = '/object-storage/{}'.format(object_storage)
        body = {
            'object_storage': {}
        }
        if access_key and secret_key:
            body['object_storage']['access_key'] = access_key
            body['object_storage']['secret_key'] = secret_key
        elif access_key or secret_key:
            raise Exception('Both keys must be provided or none')

        if description:
            body['object_storage']['description'] = description
        if size:
            body['object_storage']['size'] = size
        res = self.patch_request(url, body)
        return ObjectStorage(cloud_manager=self, **res['object_storage'])

    def delete_object_storage(self, object_storage):
        """
        Object Storage devices can be deleted using the following API request.
        """
        url = '/object-storage/{}'.format(object_storage)
        res = self.delete_request(url)
        return res

    def get_object_storage_network_statistics(
            self,
            object_storage,
            datetime_from,
            datetime_to=None,
            interval=None,
            bucket=[],
            filename=[],
            method=[],
            status=[],
            group_by=[],
            order_by=[],
            limit=None
            ):
        """
        The network usage of an Object Storage device is metered and can be reviewed using the statistics request.
        """
        key_dict = {'from': convert_datetime_string_to_object(datetime_from)}
        url = '/object-storage/{}/stats/network/?'.format(object_storage)

        if datetime_to:
            key_dict['to'] = convert_datetime_string_to_object(datetime_to)
        if interval:
            key_dict['interval'] = interval
        if bucket:
            key_dict['bucket'] = bucket
        if filename:
            key_dict['filename'] = filename
        if method:
            key_dict['method'] = method
        if status:
            key_dict['status'] = status
        if group_by:
            key_dict['group_by'] = group_by
        if order_by:
            key_dict['order_by'] = order_by
        if limit:
            key_dict['limit'] = limit
        res = self.get_request(url, params=key_dict)
        return res
