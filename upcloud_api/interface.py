from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


class Interface(UpCloudResource):
    """
    Class representation of UpCloud network interface.
    """

    ATTRIBUTES = {
        'index': None,
        'ip_addresses': None,
        'mac': None,
        'network': None,
        'source_ip_filtering': None,
        'type': None,
        'bootable': None
    }
