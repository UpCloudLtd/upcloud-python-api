from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import six

from upcloud_api import IPAddress


class IPManager(object):
    """
    Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
    """

    def get_ip(self, address):
        """
        Get an IPAddress object with the IP address (string) from the API.

        e.g manager.get_ip('80.69.175.210')
        """
        res = self.get_request('/ip_address/' + address)
        return IPAddress(cloud_manager=self, **res['ip_address'])

    def get_ips(self):
        """
        Get all IPAddress objects from the API.
        """
        res = self.get_request('/ip_address')
        IPs = IPAddress._create_ip_address_objs(res['ip_addresses'], cloud_manager=self)
        return IPs

    def attach_ip(self, server, family='IPv4'):
        """
        Attach a new (random) IPAddress to the given server (object or UUID).
        """
        body = {
            'ip_address': {
                'server': str(server),
                'family': family
            }
        }

        res = self.post_request('/ip_address', body)
        return IPAddress(cloud_manager=self, **res['ip_address'])

    def modify_ip(self, ip_addr, ptr_record):
        """
        Modify an IP address' ptr-record (Reverse DNS).

        Accepts an IPAddress instance (object) or its address (string).
        """
        body = {
            'ip_address': {
                'ptr_record': ptr_record
            }
        }

        res = self.put_request('/ip_address/' + str(ip_addr), body)
        return IPAddress(cloud_manager=self, **res['ip_address'])

    def release_ip(self, ip_addr):
        """
        Destroy an IPAddress. Returns an empty object.

        Accepts an IPAddress instance (object) or its address (string).
        """
        return self.delete_request('/ip_address/' + str(ip_addr))
