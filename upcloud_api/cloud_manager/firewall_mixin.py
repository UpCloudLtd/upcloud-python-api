from __future__ import unicode_literals
from __future__ import absolute_import

from upcloud_api import FirewallRule, Server

def uuid_and_instance(server):
    """server => uuid, instance"""
    if isinstance(server, Server):
        return server.uuid, server
    return server, None

class FirewallManager(object):
    """
    Provides get / list / create / delete functionality for firewall rules.

    These functions are used by the FirewallRule class but may also be used
    directly.
    """

    def get_firewall_rule(self, server_uuid, firewall_rule_position, server_instance=None):
        """
        Return a FirewallRule object based on server uuid and rule position.
        """
        url = '/server/{0}/firewall_rule/{1}'.format(server_uuid, firewall_rule_position)
        res = self.get_request(url)
        return FirewallRule(**res['firewall_rule'])

    def get_firewall_rules(self, server):
        """
        Return all FirewallRule objects based on a server instance or uuid.
        """
        server_uuid, server_instance = uuid_and_instance(server)

        url = '/server/{0}/firewall_rule'.format(server_uuid)
        res = self.get_request(url)

        return [
            FirewallRule(server=server_instance, **firewall_rule)
            for firewall_rule in res['firewall_rules']['firewall_rule']
        ]

    def create_firewall_rule(self, server, firewall_rule_body):
        """
        Create a new firewall rule for a given server uuid.

        The rule can begiven as a dict or with FirewallRule.prepare_post_body().
        Returns a FirewallRule object.
        """
        server_uuid, server_instance = uuid_and_instance(server)

        url = '/server/{0}/firewall_rule'.format(server_uuid)
        body = {'firewall_rule': firewall_rule_body}
        res = self.post_request(url, body)

        return FirewallRule(server=server_instance, **res['firewall_rule'])

    def delete_firewall_rule(self, server_uuid, firewall_rule_position):
        """
        Delete a firewall rule based on a server uuid and rule position.
        """
        url = '/server/{0}/firewall_rule/{1}'.format(server_uuid, firewall_rule_position)
        return self.delete_request(url)

    def configure_firewall(self, server, firewall_rule_bodies):
        """
        Helper for calling create_firewall_rule in series for a list of firewall_rule_bodies.
        """
        server_uuid, server_instance = uuid_and_instance(server)

        return [
            self.create_firewall_rule(server_uuid, rule)
            for rule in firewall_rule_bodies
        ]
