from upcloud_api.upcloud_resource import UpCloudResource


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
        'bootable': None,
    }
