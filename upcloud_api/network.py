from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

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
        'servers': None
    }

    def __str__(self):
        """
        String representation of Network.
        """
        return self.uuid
