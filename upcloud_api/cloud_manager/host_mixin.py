from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from upcloud_api import Host


class HostManager(object):
    """
    Functions for managing hosts. Intended to be used as a mixin for CloudManager.
    """

    def get_hosts(self):
        """
        Returns a list of available hosts, along with basic statistics of them when available.
        """
        url = '/host'
        res = self.get_request(url)
        return [Host(**host) for host in res['hosts']['host']]

    def get_host(self, id):
        """
        Returns detailed information about a specific host.
        """
        url = '/host/{0}'.format(id)
        res = self.get_request(url)
        return Host(**res['host'])

    def modify_host(self, host, description):
        """
        Modifies description of a specific host.
        """
        url = '/host/{0}'.format(host)
        body = {'host': {'description': description}}
        res = self.patch_request(url, body)
        return Host(**res['host'])
