from __future__ import unicode_literals
from upcloud_api import UpCloudResource

class IPAddress(UpCloudResource):
    """
    Object representation of the IP-address.

    Attributes:
    access -- "public" or "private"
    address -- the actual IPAddress (string)
    ptr_record -- the reverse DNS name (string)
    server -- the UUID of the server this IP is attached to (string)

    The only updateable field is the ptr_record.
    ptr_record and server are present only if /server/uuid endpoint was used.
    """

    ATTRIBUTES = {
        'family': 'IPv4',
        'access': None,
        'address': None,
        'ptr_record': None
    }

    def save(self):
        """
        IPAddress can only change its PTR record. Saves the current state, PUT /ip_address/uuid.
        """
        body = {'ip_address': {'ptr_record': self.ptr_record}}
        data = self.cloud_manager.request('PUT', '/ip_address/' + self.address, body)
        self._reset(**data['ip_address'])

    def destroy(self):
        """
        Release the IPAddress. DELETE /ip_address/uuid.
        """
        self.cloud_manager.release_ip(self.address)

    def __str__(self):  # noqa
        return 'IP-address: ' + self.address

    @staticmethod
    def _create_ip_address_objs(ip_addresses, cloud_manager):

        # ip-addresses might be provided as a flat array or as a following dict:
        # {'ip_addresses': {'ip_address': [...]}} || {'ip_address': [...]}

        if 'ip_addresses' in ip_addresses:
            ip_addresses = ip_addresses['ip_addresses']

        if 'ip_address' in ip_addresses:
            ip_addresses = ip_addresses['ip_address']

        return [
            IPAddress(cloud_manager=cloud_manager, **ip_addr)
            for ip_addr in ip_addresses
        ]
