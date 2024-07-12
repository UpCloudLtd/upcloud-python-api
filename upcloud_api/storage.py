from enum import Enum

from upcloud_api.upcloud_resource import UpCloudResource

STORAGE_OSES_WHICH_REQUIRE_METADATA = [
    "01000000-0000-4000-8000-000020070100",  # Debian GNU/Linux 12 (Bookworm)
    "01000000-0000-4000-8000-000030220200",  # Ubuntu Server 22.04 LTS (Jammy Jellyfish)
    "01000000-0000-4000-8000-000030240200",  # Ubuntu Server 24.04 LTS (Noble Numbat)
    "01000000-0000-4000-8000-000140020100",  # AlmaLinux 9
    "01000000-0000-4000-8000-000150020100",  # Rocky Linux 9
]


class BackupDeletionPolicy(Enum):
    """
    Class representation of backup deletion policies used on storage deletions.
    """

    KEEP = 'keep'
    KEEP_LATEST = 'keep_latest'
    DELETE = 'delete'


class Storage(UpCloudResource):
    """
    Class representation of UpCloud Storage instance.
    """

    ATTRIBUTES = {
        'access': None,
        'address': None,
        'encrypted': None,
        'labels': None,
        'license': None,
        'state': None,
        'size': 10,
        'tier': 'maxiops',
        'title': '',
        'type': None,
        'uuid': None,
        'zone': None,
    }

    def _reset(self, **kwargs) -> None:
        """
        Reset after repopulating from API.
        """

        # there are some inconsistencies in the API regarding these
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

        if kwargs.get('encrypted') == 'yes':
            self.encrypted = True
        else:
            self.encrypted = False

        # send the rest to super._reset

        filtered_kwargs = {
            key: val
            for key, val in kwargs.items()
            if key
            not in [
                'uuid',
                'storage',
                'title',
                'storage_title',
                'size',
                'storage_size',
                'encrypted',
            ]
        }
        super()._reset(**filtered_kwargs)

    def destroy(self) -> None:
        """
        Destroy the storage via the API.
        """
        self.cloud_manager.delete_storage(self.uuid)

    def save(self) -> None:
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

    def clone(self, title: str, zone: str, tier=None) -> 'Storage':
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

    def create_backup(self, title: str) -> 'Storage':
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

    def templatize(self, title: str) -> 'Storage':
        """
        Creates an exact copy of an existing storage resource which can be used as a template for creating new servers using StorageManager.
        """
        return self.cloud_manager.templatize_storage(self.uuid, title)

    def __str__(self) -> str:
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

        if hasattr(self, 'labels'):
            dict_labels = []
            for label in self.labels:
                dict_labels.append(label.to_dict())
            body['labels'] = dict_labels

        if hasattr(self, 'encrypted') and isinstance(self.encrypted, bool):
            body['encrypted'] = "yes" if self.encrypted else "no"

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

        return [Storage(cloud_manager=cloud_manager, **storage) for storage in storages]
