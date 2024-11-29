import datetime
from typing import Optional

from upcloud_api.api import API
from upcloud_api.object_storage import ObjectStorage


class ObjectStorageManager:
    """
    Functions for managing Object Storages. Intended to be used as a mixin for CloudManager.
    """

    api: API

    def get_object_storages(self):
        """
        List all Object Storage devices on the account or those which the sub-account has permissions.
        """
        url = '/object-storage'
        res = self.api.get_request(url)
        object_storages = [
            ObjectStorage(**o_s) for o_s in res['object_storages']['object_storage']
        ]
        return object_storages

    def create_object_storage(
        self,
        zone: str,
        access_key: str,
        secret_key: str,
        size: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> ObjectStorage:
        """
        Used to create a new Object Storage device with a given name, size and location.
        """
        url = '/object-storage'
        body = {
            'object_storage': {
                'zone': zone,
                'access_key': access_key,
                'secret_key': secret_key,
                'size': size,
            }
        }
        if name:
            body['object_storage']['name'] = name
        if description:
            body['object_storage']['description'] = description
        res = self.api.post_request(url, body)
        return ObjectStorage(cloud_manager=self, **res['object_storage'])

    def get_object_storage(self, uuid: str) -> ObjectStorage:
        """
        A request to get details about a specific Object Storage device by the given uuid.
        """
        url = f'/object-storage/{uuid}'
        res = self.api.get_request(url)
        return ObjectStorage(cloud_manager=self, **res['object_storage'])

    def modify_object_storage(
        self,
        object_storage: str,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        description: Optional[str] = None,
        size: Optional[int] = None,
    ) -> ObjectStorage:
        """
        Modify requests can be used to update the details of an Object Storage including description, access_key and secret_key.
        """
        url = f'/object-storage/{object_storage}'
        body = {'object_storage': {}}
        if access_key and secret_key:
            body['object_storage']['access_key'] = access_key
            body['object_storage']['secret_key'] = secret_key
        elif access_key or secret_key:
            raise Exception('Both keys must be provided or none')

        if description:
            body['object_storage']['description'] = description
        if size:
            body['object_storage']['size'] = size
        res = self.api.patch_request(url, body)
        return ObjectStorage(cloud_manager=self, **res['object_storage'])

    def delete_object_storage(self, object_storage):
        """
        Object Storage devices can be deleted using the following API request.
        """
        url = f'/object-storage/{object_storage}'
        res = self.api.delete_request(url)
        return res

    def get_object_storage_network_statistics(
        self,
        object_storage,
        datetime_from: datetime.datetime,
        datetime_to: Optional[datetime.datetime] = None,
        interval: Optional[int] = None,
        bucket: Optional[list[str]] = None,
        filename: Optional[list[str]] = None,
        method: Optional[list[str]] = None,
        status: Optional[list[int]] = None,
        group_by: Optional[list[str]] = None,
        order_by: Optional[list[str]] = None,
        limit: Optional[int] = None,
    ):
        """
        The network usage of an Object Storage device is metered and can be reviewed using the statistics request.
        """
        key_dict = {'from': datetime_from.isoformat(timespec='seconds')}
        url = f'/object-storage/{object_storage}/stats/network/?'

        if datetime_to:
            key_dict['to'] = datetime_to.isoformat(timespec='seconds')
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
        res = self.api.get_request(url, params=key_dict)
        return res
