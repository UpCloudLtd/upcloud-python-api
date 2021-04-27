from upcloud_api.upcloud_resource import UpCloudResource


class Router(UpCloudResource):
    """
    Class representation of UpCloud network.
    """

    ATTRIBUTES = {'name': None, 'type': None, 'uuid': None, 'attached_networks': None}

    def __str__(self):
        """
        String representation of Router.
        """
        return self.uuid
