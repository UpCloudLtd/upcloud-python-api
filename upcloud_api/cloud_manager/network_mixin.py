from upcloud_api.api import API
from upcloud_api.interface import Interface
from upcloud_api.ip_network import IpNetwork
from upcloud_api.network import Network
from upcloud_api.router import Router


class NetworkManager:
    """
    Functions for managing networks. Intended to be used as a mixin for CloudManager.
    """

    api: API

    def get_networks(self, zone=None):
        """
        Get a list of all networks.
        Zone can be passed to return networks in a specific zone
        """
        url = f'/network/?zone={zone}' if zone else '/network'
        res = self.api.get_request(url)
        networks = [Network(**network) for network in res['networks']['network']]
        for network in networks:
            network.ip_networks = [IpNetwork(**n) for n in network.ip_networks.get('ip_network')]
        return networks

    def get_network(self, uuid: str) -> Network:
        """
        Retrieves the details of a specific network.
        """
        url = f'/network/{uuid}'
        res = self.api.get_request(url)
        network = Network(**res['network'])
        network.ip_networks = [IpNetwork(**n) for n in network.ip_networks.get('ip_network')]
        return network

    def create_network(
        self,
        name,
        zone,
        address,
        dhcp,
        family,
        router=None,
        dhcp_default_route=None,
        dhcp_dns=None,
        dhcp_bootfile_url=None,
        gateway=None,
    ):
        """
        Creates a new SDN private network that cloud servers from the same zone can be attached to.
        """
        url = '/network'
        body = {
            'network': {
                'name': name,
                'zone': zone,
                'ip_networks': {
                    'ip_network': {'address': address, 'dhcp': dhcp, 'family': family}
                },
            }
        }
        # TODO: fix duplication c.f. modify_network
        if router:
            body['network']['router'] = router
        if dhcp_default_route:
            body['network']['ip_networks']['ip_network']['dhcp_default_route'] = dhcp_default_route
        if dhcp_dns:
            body['network']['ip_networks']['ip_network']['dhcp_dns'] = dhcp_dns
        if dhcp_bootfile_url:
            body['network']['ip_networks']['ip_network']['dhcp_bootfile_url'] = dhcp_bootfile_url
        if gateway:
            body['network']['ip_networks']['ip_network']['gateway'] = gateway
        res = self.api.post_request(url, body)
        network = Network(**res['network'])
        network.ip_networks = [IpNetwork(**n) for n in network.ip_networks.get('ip_network')]
        return network

    def modify_network(
        self,
        network,
        dhcp,
        family,
        name=None,
        router=None,
        dhcp_default_route=None,
        dhcp_dns=None,
        dhcp_bootfile_url=None,
        gateway=None,
    ):
        """
        Modifies the details of a specific SDN private network. The Utility and public networks cannot be modified.
        """
        url = f'/network/{network}'
        body = {'network': {'ip_networks': {'ip_network': {'family': family}}}}
        if name:
            body['network']['name'] = name
        if dhcp:
            body['network']['ip_networks']['ip_network']['dhcp'] = dhcp
        if router:
            body['network']['router'] = router
        if dhcp_default_route:
            body['network']['ip_networks']['ip_network']['dhcp_default_route'] = dhcp_default_route
        if dhcp_dns:
            body['network']['ip_networks']['ip_network']['dhcp_dns'] = dhcp_dns
        if dhcp_bootfile_url:
            body['network']['ip_networks']['ip_network']['dhcp_bootfile_url'] = dhcp_bootfile_url
        if gateway:
            body['network']['ip_networks']['ip_network']['gateway'] = gateway
        res = self.api.put_request(url, body)
        network = Network(**res['network'])
        network.ip_networks = [IpNetwork(**n) for n in network.ip_networks.get('ip_network')]
        return network

    def delete_network(self, network):
        """
        Deletes an SDN private network. All attached cloud servers must first be detached before SDN private networks can be deleted.
        """
        url = f'/network/{network}'
        res = self.api.delete_request(url)
        return res

    def get_server_networks(self, server):
        """
        List all networks the specific cloud server is connected to.
        """
        url = f'/server/{server}/networking'
        res = self.api.get_request(url)
        return [
            Interface(**interface) for interface in res['networking']['interfaces']['interface']
        ]

    def create_network_interface(
        self,
        server,
        network,
        type,
        ip_addresses,
        index=None,
        source_ip_filtering=None,
        bootable=None,
    ):
        """
        Creates a new network interface on the specific cloud server and attaches the specified SDN private network to the new interface.
        """
        url = f'/server/{server}/networking/interface'
        body = {
            'interface': {
                'network': network,
                'type': type,
                'ip_addresses': {'ip_address': ip_addresses},
            }
        }
        if index:
            body['interface']['index'] = index
        if source_ip_filtering:
            body['interface']['source_ip_filtering'] = source_ip_filtering
        if bootable:
            body['interface']['bootable'] = bootable
        res = self.api.post_request(url, body)
        return Interface(**res['interface'])

    def modify_network_interface(
        self,
        server,
        index_in_path,
        index_in_body=None,
        ip_addresses=None,
        source_ip_filtering=None,
        bootable=None,
    ):
        """
        Modifies the network interface at the selected index on the specific cloud server.
        """
        url = f'/server/{server}/networking/interface/{str(index_in_path)}'
        body = {'interface': {'ip_addresses': {'ip_address': None}}}
        if index_in_body:
            body['interface']['index'] = index_in_body
        if ip_addresses:
            body['interface']['ip_addresses']['ip_address'] = ip_addresses
        if source_ip_filtering:
            body['interface']['source_ip_filtering'] = source_ip_filtering
        if bootable:
            body['interface']['bootable'] = bootable
        res = self.api.put_request(url, body)
        return Interface(**res['interface'])

    def delete_network_interface(self, server, index):
        """
        Detaches an SDN private network from a cloud server by deleting the network interface at the selected index on the specific cloud server.
        """
        url = f'/server/{server}/networking/interface/{str(index)}'
        res = self.api.delete_request(url)
        return res

    def get_routers(self):
        """
        Returns a list of all available routers associated with the current account.
        """
        url = '/router'
        res = self.api.get_request(url)
        return [Router(**router) for router in res['routers']['router']]

    def get_router(self, uuid: str) -> Router:
        """
        Returns detailed information about a specific router.
        """
        url = f'/router/{uuid}'
        res = self.api.get_request(url)
        return Router(**res['router'])

    def create_router(self, name: str) -> Router:
        """
        Creates a new router.
        """
        url = '/router'
        body = {'router': {'name': name}}
        res = self.api.post_request(url, body)
        return Router(**res['router'])

    def modify_router(self, router: str, name: str) -> Router:
        """
        Modify an existing router.
        """
        url = f'/router/{router}'
        body = {'router': {'name': name}}
        res = self.api.patch_request(url, body)
        return Router(**res['router'])

    def delete_router(self, router):
        """
        Delete an existing router.
        """
        url = f'/router/{router}'
        res = self.api.delete_request(url)
        return res
