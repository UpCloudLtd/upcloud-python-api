from .base import BaseAPI

class FirewallRule(object):
    """
    Object representation of the FirewallRule in UpCloud's API.
    """

    attributes = set([
        'action',
        'destination_address_end',
        'destination_address_start',
        'destination_port_end',
        'destination_port_start',
        'direction',
        'family',
        'icmp_type',
        'position',
        'protocol',
        'source_address_end',
        'source_address_start',
        'source_port_end',
        'source_port_start',
    ])

    def __init__(self, **kwargs):
        """
        Creates a FirewallRule object from a dict.
        Validates against FirewallRule.attributes and uses empty string as default
        for all attributes (API wants them at least as empty strings).
        """

        # set object attributes from params
        for key in kwargs:
            if key not in self.attributes:
                self._invalid_key_err(key)

            setattr(self, key, kwargs[key])

        # set attributes that were not given as empty strings ("defaults")
        for attr in self.attributes:
            if not hasattr(self, attr):
                setattr(self, attr, '')

    def prepare_post_body(self):
        """
        Returns a dict that can be serialised to JSON and sent to UpCloud's API.
        """

        body = {}
        for attr in self.attributes:
            body[attr] = getattr(self, attr)
        return body

    def destroy(self):
        """
        Removes this FirewallRule from the API.

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


    def _invalid_key_err(self, key):
        """
        Raise exception on invalid parameters given to __init__.
        """
        attr_list = list(self.attributes)
        raise Exception(
            "invalid parameter to FirewallRule, '{key}' is not in {attributes}"
            .format(key=key, attributes=attr_list)
        )

    def _associate_with_server(self, server):
        """
        Internal function used by Server to associate itself with the FirewallRule.
        """

        self.server = server
