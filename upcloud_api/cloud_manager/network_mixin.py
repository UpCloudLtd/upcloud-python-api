from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from upcloud_api import Network, Interface, Router, IpNetwork


class NetworkManager(object):
    """
    Functions for managing networks. Intended to be used as a mixin for CloudManager.
    """

    def get_networks(self, zone=None):
        """
        Get a list of all networks.
        Zone can be passed to return networks in a specific zone
        """
        url = '/network/?zone={0}'.format(zone) if zone else '/network'
        res = self.get_request(url)
        networks = [Network(**network) for network in res['networks']['network']]
        for network in networks:
            network.ip_networks = [IpNetwork(**n) for n in network.ip_networks.get('ip_network')]
        return networks

    def get_network(self, uuid):
        """
        Retrieves the details of a specific network.
        """
        url = '/network/{0}'.format(uuid)
        res = self.get_request(url)
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
        gateway=None
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
                    'ip_network': {
                        'address': address,
                        'dhcp': dhcp,
                        'family': family
                    }
                }
            }
        }

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
        res = self.post_request(url, body)
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
        gateway=None
    ):
        """
        Modifies the details of a specific SDN private network.
        The Utility and public networks cannot be modified.
        """
        url = '/network/{}'.format(network)
        body = {
            'network': {
                'ip_networks': {
                    'ip_network': {'family': family}
                }
            }
        }
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
        res = self.put_request(url, body)
        network = Network(**res['network'])
        network.ip_networks = [IpNetwork(**n) for n in network.ip_networks.get('ip_network')]
        return network

    def delete_network(self, network):
        """
        Deletes an SDN private network.
        All attached cloud servers must first be detached
        before SDN private networks can be deleted.
        """
        url = '/network/{0}'.format(network)
        res = self.delete_request(url)
        return res

    def get_server_networks(self, server):
        """
        List all networks the specific cloud server is connected to.
        """
        url = '/server/{0}/networking'.format(server)
        res = self.get_request(url)
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
        bootable=None
    ):
        """
        Creates a new network interface on the specific cloud server.
        Also attaches the specified SDN private network to the new interface.
        """
        url = '/server/{0}/networking/interface'.format(server)
        body = {
            'interface': {
                'network': network,
                'type': type,
                'ip_addresses': {'ip_address': ip_addresses}
            }
        }
        if index:
            body['interface']['index'] = index
        if source_ip_filtering:
            body['interface']['source_ip_filtering'] = source_ip_filtering
        if bootable:
            body['interface']['bootable'] = bootable
        res = self.post_request(url, body)
        return Interface(**res['interface'])

    def modify_network_interface(
        self,
        server,
        index_in_path,
        index_in_body=None,
        ip_addresses=None,
        source_ip_filtering=None,
        bootable=None
    ):
        """
        Modifies the network interface at the selected index on the specific cloud server.
        """
        url = '/server/{0}/networking/interface/{1}'.format(server, str(index_in_path))
        body = {'interface': {'ip_addresses': {'ip_address': None}}}
        if index_in_body:
            body['interface']['index'] = index_in_body
        if ip_addresses:
            body['interface']['ip_addresses']['ip_address'] = ip_addresses
        if source_ip_filtering:
            body['interface']['source_ip_filtering'] = source_ip_filtering
        if bootable:
            body['interface']['bootable'] = bootable
        res = self.put_request(url, body)
        return Interface(**res['interface'])

    def delete_network_interface(self, server, index):
        """
        Detaches an SDN private network from a cloud server by deleting the network interface.
        Deleted network is selected by the index on the specific cloud server.
        """
        url = '/server/{0}/networking/interface/{1}'.format(server, str(index))
        res = self.delete_request(url)
        return res

    def get_routers(self):
        """
        Returns a list of all available routers associated with the current account.
        """
        url = '/router'
        res = self.get_request(url)
        return [Router(**router) for router in res['routers']['router']]

    def get_router(self, uuid):
        """
        Returns detailed information about a specific router.
        """
        url = '/router/{0}'.format(uuid)
        res = self.get_request(url)
        return Router(**res['router'])

    def create_router(self, name):
        """
        Creates a new router.
        """
        url = '/router'
        body = {'router': {'name': name}}
        res = self.post_request(url, body)
        return Router(**res['router'])

    def modify_router(self, router, name):
        """
        Modify an existing router.
        """
        url = '/router/{0}'.format(router)
        body = {'router': {'name': name}}
        res = self.patch_request(url, body)
        return Router(**res['router'])

    def delete_router(self, router):
        """
        Delete an existing router.
        """
        url = '/router/{0}'.format(router)
        res = self.delete_request(url)
        return res
