from upcloud_api.upcloud_resource import UpCloudResource


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
        'gateway': None,
    }
