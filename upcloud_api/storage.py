from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


class Storage(UpCloudResource):
    """
    Class representation of UpCloud Storage instance.
    """

    ATTRIBUTES = {
        'uuid': None,
        'tier': 'maxiops',
        'size': 10,
        'access': None,
        'license': None,
        'state': None,
        'title': '',
        'type': None,
        'address': None,
        'zone': None,
    }


    def _reset(self, **kwargs):
        """
        Reset after repopulating from API.
        """

        # there are some inconsistenciens in the API regarding these
        # note: this could be written in fancier ways, but this way is simpler

        if 'uuid' in kwargs:
            self.uuid = kwargs['uuid']
        elif 'storage' in kwargs:  # let's never use storage.storage internally
            self.uuid = kwargs['storage']

        if 'title' in kwargs:
            self.title = kwargs['title']
        elif 'storage_title' in kwargs:
            self.title = kwargs['storage_title']

        if 'size' in kwargs:
            self.size = kwargs['size']
        elif 'storage_size' in kwargs:
            self.size = kwargs['storage_size']

        # send the rest to super._reset

        filtered_kwargs = dict(
            (key, val)
            for key, val in kwargs.items()
            if key not in ['uuid', 'storage', 'title', 'storage_title', 'size', 'storage_size']
        )
        super(Storage, self)._reset(**filtered_kwargs)

    def destroy(self):
        """
        Destroy the storage via the API.
        """
        self.cloud_manager.delete_storage(self.uuid)

    def save(self):
        """
        Save (modify) the storage to the API.
        Note: only size and title are updateable fields.
        """
        res = self.cloud_manager._modify_storage(self, self.size, self.title)
        self._reset(**res['storage'])

    def update(self, size, title):
        """
        Update the storage to the API.
        """
        self.size = size
        self.title = title
        self.save()

    def clone(self, title, zone, tier=None):
        """
        Clone the storage using StorageManager.
        Returns an object based on the API's response.
        """
        return self.cloud_manager.clone_storage(self.uuid, title, zone, tier)

    def cancel_cloning(self):
        """
        Cancels a running cloning operation and deletes the incomplete copy using StorageManager.
        Needs to be called from the cloned storage and not the storage that is being cloned.
        """
        return self.cloud_manager.cancel_clone_storage(self.uuid)

    def create_backup(self, title):
        """
        Creates a point-in-time backup of a storage resource using StorageManager.
        """
        return self.cloud_manager.create_storage_backup(self.uuid, title)

    def restore_backup(self):
        """
        Restores the origin storage with data from the specified backup storage using StorageManager.
        Must be called from a storage object created by create_backup and not the original one.
        """
        return self.cloud_manager.restore_storage_backup(self.uuid)

    def templatize(self, title):
        """
        Creates an exact copy of an existing storage resource which can be used as a template for creating new servers using StorageManager.
        """
        return self.cloud_manager.templatize_storage(self.uuid, title)

    def __str__(self):
        """
        String representation of Storage.
        Can be used to add tags into API requests: str(storage).
        """
        return self.uuid

    def to_dict(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.

        Uses the convenience attribute `os` for determining `action` and `storage`
        fields.
        """
        body = {
            'tier': self.tier,
            'title': self.title,
            'size': self.size,
        }

        # optionals

        if hasattr(self, 'address') and self.address:
            body['address'] = self.address

        if hasattr(self, 'zone') and self.zone:
            body['zone'] = self.zone

        return body

    @staticmethod
    def _create_storage_objs(storages, cloud_manager):

        # storages might be provided as a flat array or as a following dict:
        # {'storage_devices': {'storage_device': [...]}} || {'storage_device': [...]}

        if 'storage_devices' in storages:
            storages = storages['storage_devices']
        if 'storage_device' in storages:
            storages = storages['storage_device']

        # or {'storages': {'storage': [...]}} || {'storage': [...]}

        if 'storages' in storages:
            storages = storages['storages']
        if 'storage' in storages:
            storages = storages['storage']

        return [
            Storage(cloud_manager=cloud_manager, **storage)
            for storage in storages
        ]
