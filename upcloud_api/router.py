from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


class Router(UpCloudResource):
    """
    Class representation of UpCloud network.
    """

    ATTRIBUTES = {
        'name': None,
        'type': None,
        'uuid': None,
        'attached_networks': None
    }

    def __str__(self):
        """
        String representation of Router.
        """
        return self.uuid
