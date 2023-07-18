from upcloud_api.upcloud_resource import UpCloudResource


class IPAddress(UpCloudResource):
    """
    Class representation of the API's IP address. Extends UpCloudResource.

    Attributes
    ----------
    access -- "public" or "private"
    address -- the actual IPAddress (string)
    family -- IPv4 or IPv6
    part_of_plan -- yes/no string indicating whether this belongs to a preconfigured plan or not
    ptr_record -- the reverse DNS name (string)
    server -- the UUID of the server this IP is attached to (string)

    The only updatable field is the ptr_record.

    Note that all of the fields are not always available depending on the API call,
    consult the official API docs for details.
    """

    ATTRIBUTES = {
        'access': None,
        'address': None,
        'family': 'IPv4',
        'part_of_plan': None,
        'ptr_record': None,
        'server': None,
    }

    def save(self) -> None:
        """
        IPAddress can only change its PTR record. Saves the current state, PUT /ip_address/uuid.
        """
        body = {'ip_address': {'ptr_record': self.ptr_record}}
        data = self.cloud_manager.api.put_request('/ip_address/' + self.address, body)
        self._reset(**data['ip_address'])

    def destroy(self):
        """
        Release the IPAddress. DELETE /ip_address/uuid.
        """
        self.cloud_manager.release_ip(self.address)

    def __str__(self):
        """
        String representation of IPAddress.
        Can be used to add tags into API requests: str(ip_addr).
        """
        return self.address

    @staticmethod
    def _create_ip_address_objs(ip_addresses, cloud_manager, ignore_ips_without_server=False):
        """
        Create IPAddress objects from API response data.
        Also associates CloudManager with the objects.
        """
        # ip-addresses might be provided as a flat array or as a following dict:
        # {'ip_addresses': {'ip_address': [...]}} || {'ip_address': [...]}

        if 'ip_addresses' in ip_addresses:
            ip_addresses = ip_addresses['ip_addresses']

        if 'ip_address' in ip_addresses:
            ip_addresses = ip_addresses['ip_address']

        filtered_ip_addresses = [] if ignore_ips_without_server else ip_addresses

        if ignore_ips_without_server:
            for ip_addr in ip_addresses:
                if ip_addr.get('server'):
                    filtered_ip_addresses.append(ip_addr)

        return [
            IPAddress(cloud_manager=cloud_manager, **ip_addr) for ip_addr in filtered_ip_addresses
        ]
