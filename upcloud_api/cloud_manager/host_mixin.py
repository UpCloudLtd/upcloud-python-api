from upcloud_api.api import API
from upcloud_api.host import Host


class HostManager:
    """
    Functions for managing hosts. Intended to be used as a mixin for CloudManager.
    """

    api: API

    def get_hosts(self):
        """
        Returns a list of available hosts, along with basic statistics of them when available.
        """
        url = '/host'
        res = self.api.get_request(url)
        return [Host(**host) for host in res['hosts']['host']]

    def get_host(self, id: str) -> Host:
        """
        Returns detailed information about a specific host.
        """
        url = f'/host/{id}'
        res = self.api.get_request(url)
        return Host(**res['host'])

    def modify_host(self, host: str, description: str) -> Host:
        """
        Modifies description of a specific host.
        """
        url = f'/host/{host}'
        body = {'host': {'description': description}}
        res = self.api.patch_request(url, body)
        return Host(**res['host'])
