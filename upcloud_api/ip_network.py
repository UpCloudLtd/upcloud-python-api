from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


class IpNetwork(UpCloudResource):
    """
    Class representation of UpCloud Ip Network.
    """

    ATTRIBUTES = {
        'address': None,
        'dhcp': None,
        'dhcp_default_route': None,
        'dhcp_dns': [],
        'family': None,
        'gateway': None
    }
