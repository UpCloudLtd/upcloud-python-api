from upcloud_api.upcloud_resource import UpCloudResource


class FirewallRule(UpCloudResource):
    """
    Class representation of the API's firewall rule. Extends UpCloudResource.
    """

    ATTRIBUTES = {
        'action': 'drop',
        'direction': 'in',
        'family': 'IPv4',
        'comment': '',
        'destination_address_end': None,
        'destination_address_start': None,
        'destination_port_end': None,
        'destination_port_start': None,
        'icmp_type': None,
        'position': None,
        'protocol': None,
        'source_address_end': None,
        'source_address_start': None,
        'source_port_end': None,
        'source_port_start': None,
    }

    def destroy(self):
        """
        Remove this FirewallRule from the API.

        This instance must be associated with a server for this method to work,
        which is done by instantiating via server.get_firewall_rules().
        """
        if not hasattr(self, 'server') or not self.server:
            raise Exception(
                """FirewallRule not associated with server;
                please use or server.get_firewall_rules() to get objects
                that are associated with a server.
                """
            )
        return self.server.cloud_manager.delete_firewall_rule(self.server.uuid, self.position)
