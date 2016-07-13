from __future__ import unicode_literals


class FirewallRule(object):
    """
    Object representation of the FirewallRule in UpCloud's API.
    """

    attributes = {
        # attribute: default_value
        # if none -> not sent to API unless given as param
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

    def __init__(self, **kwargs):
        """
        Create a FirewallRule object from a dict.

        Validate against FirewallRule.attributes and uses empty string as default
        for all attributes (API wants them at least as empty strings).
        """
        # set object attributes from params
        for key in kwargs:
            setattr(self, key, kwargs[key])

        # set defaults (if need be) where the default is not None
        for attr in self.attributes:
            if not hasattr(self, attr) and self.attributes[attr] is not None:
                setattr(self, attr, self.attributes[attr])

    def prepare_post_body(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.
        """
        body = {}
        for attr in self.attributes:
            if hasattr(self, attr):
                body[attr] = getattr(self, attr)
        return body

    def destroy(self):
        """
        Remove this FirewallRule from the API.

        This instance must be associated with a server for this method to work,
        which is done by instantiating via server.get_firewall_rule(position)
        or server.get_firewall_rules().
        """
        if not hasattr(self, 'server') or not self.server:
            raise Exception(
                """FirewallRule not associated with server;
                please use server.get_firewall_rule(position)
                or server.get_firewall_rules() to get objects
                that are associated with a server.
                """)
        return self.server.cloud_manager.delete_firewall_rule(
            self.server.uuid,
            self.position
        )

    def _associate_with_server(self, server):
        """
        Internal function used by Server to associate itself with the FirewallRule.
        """
        self.server = server
