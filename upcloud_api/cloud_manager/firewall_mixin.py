from __future__ import unicode_literals
from __future__ import absolute_import

from upcloud_api import FirewallRule


class FirewallManager(object):
    """
    Provides get / list / create / delete functionality for firewall rules.

    These functions are used by the FirewallRule class but may also be used
    directly.
    """

    def get_firewall_rule(self, server_uuid, firewall_rule_position):
        """
        Return a FirewallRule object based on server uuid and rule position.
        """
        url = '/server/{0}/firewall_rule/{1}'.format(server_uuid, firewall_rule_position)
        res = self.get_request(url)
        return FirewallRule(**res['firewall_rule'])

    def get_firewall_rules(self, server_uuid):
        """
        Return all FirewallRule objects based on a server uuid.
        """
        url = '/server/{0}/firewall_rule'.format(server_uuid)

        res = self.get_request(url)

        firewall_rules = []
        for firewall_rule in res['firewall_rules']['firewall_rule']:
            firewall_rules.append(FirewallRule(**firewall_rule))

        return firewall_rules

    def create_firewall_rule(self, server_uuid, firewall_rule_body):
        """
        Create a new firewall rule for a given server uuid.

        The rule can begiven as a dict or with FirewallRule.prepare_post_body().
        Returns a FirewallRule object.
        """
        url = '/server/{0}/firewall_rule'.format(server_uuid)

        body = {'firewall_rule': firewall_rule_body}
        res = self.post_request(url, body)
        return FirewallRule(**res['firewall_rule'])

    def delete_firewall_rule(self, server_uuid, firewall_rule_position):
        """
        Delete a firewall rule based on a server uuid and rule position.
        """
        url = '/server/{0}/firewall_rule/{1}'.format(server_uuid, firewall_rule_position)
        return self.request('DELETE', url)

    def configure_firewall(self, UUID, firewall_rule_bodies):
        """
        Helper for calling create_firewall_rule in series for a list of firewall_rule_bodies.
        """
        FirewallRules = []
        for rule in firewall_rule_bodies:
            FirewallRule = self.create_firewall_rule(UUID, rule)
            FirewallRules.append(FirewallRule)

        return FirewallRules
