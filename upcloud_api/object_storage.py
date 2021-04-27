from upcloud_api.upcloud_resource import UpCloudResource


class ObjectStorage(UpCloudResource):
    """
    Class representation of UpCloud Object Storage.
    """

    ATTRIBUTES = {
        'uuid': None,
        'name': None,
        'description': None,
        'size': None,
        'state': None,
        'url': None,
        'zone': None,
    }

    def __str__(self):
        """
        String representation of Object Storage.
        """
        return self.uuid
