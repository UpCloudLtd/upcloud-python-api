from upcloud_api import UpCloudResource


class Host(UpCloudResource):
    """
    Class representation of UpCloud network.
    """

    ATTRIBUTES = {
        'id': None,
        'description': None,
        'zone': None,
        'windows_enabled': None,
        'stats': None,
    }

    def __str__(self):
        """
        String representation of Host.
        """
        return self.id
