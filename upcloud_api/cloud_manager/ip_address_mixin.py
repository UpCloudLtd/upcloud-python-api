from upcloud_api.api import API
from upcloud_api.ip_address import IPAddress


class IPManager:
    """
    Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
    """

    api: API

    def get_ip(self, address: str) -> IPAddress:
        """
        Get an IPAddress object with the IP address (string) from the API.

        e.g manager.get_ip('80.69.175.210')
        """
        res = self.api.get_request('/ip_address/' + address)
        return IPAddress(cloud_manager=self, **res['ip_address'])

    def get_ips(self, ignore_ips_without_server=False):
        """
        Get all IPAddress objects from the API.
        """
        res = self.api.get_request('/ip_address')
        IPs = IPAddress._create_ip_address_objs(
            res['ip_addresses'], self, ignore_ips_without_server
        )
        return IPs

    def attach_ip(self, server: str, family: str = 'IPv4') -> IPAddress:
        """
        Attach a new (random) IPAddress to the given server (object or UUID).
        """
        body = {'ip_address': {'server': str(server), 'family': family}}

        res = self.api.post_request('/ip_address', body)
        return IPAddress(cloud_manager=self, **res['ip_address'])

    def modify_ip(self, ip_addr: str, ptr_record: str) -> IPAddress:
        """
        Modify an IP address' ptr-record (Reverse DNS).

        Accepts an IPAddress instance (object) or its address (string).
        """
        body = {'ip_address': {'ptr_record': ptr_record}}

        res = self.api.put_request('/ip_address/' + str(ip_addr), body)
        return IPAddress(cloud_manager=self, **res['ip_address'])

    def release_ip(self, ip_addr):
        """
        Destroy an IPAddress. Returns an empty object.

        Accepts an IPAddress instance (object) or its address (string).
        """
        return self.api.delete_request('/ip_address/' + str(ip_addr))

    def create_floating_ip(self, zone: str, mac: str = '', family: str = 'IPv4') -> IPAddress:
        """
        Create a floating IP and returns an IPAddress object.
        Specify MAC address of network interface to attach the floating IP when it is created
        """
        body = {'ip_address': {'family': family, 'floating': 'yes', 'zone': zone}}
        if mac:
            body['ip_address']['mac'] = mac

        res = self.api.post_request('/ip_address', body)
        return IPAddress(cloud_manager=self, **res['ip_address'])
