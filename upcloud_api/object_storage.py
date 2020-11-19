from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


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
        'zone': None
    }

    def __str__(self):
        """
        String representation of Object Storage.
        """
        return self.uuid
