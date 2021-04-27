from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


class Network(UpCloudResource):
    """
    Class representation of UpCloud network.
    """

    ATTRIBUTES = {
        'name': None,
        'type': None,
        'uuid': None,
        'zone': None,
        'ip_networks': None,
        'servers': None,
    }

    def __str__(self):
        """
        String representation of Network.
        """
        return self.uuid
