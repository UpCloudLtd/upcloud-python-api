from upcloud_api.api import API
from upcloud_api.firewall import FirewallRule
from upcloud_api.server import Server


def uuid_and_instance(server):
    """server => uuid, instance"""
    if isinstance(server, Server):
        return server.uuid, server
    return server, None


class FirewallManager:
    """
    Provides get / list / create / delete functionality for firewall rules.

    These functions are used by the FirewallRule class but may also be used
    directly.
    """

    api: API

    # TODO: server_instance is unused?
    def get_firewall_rule(self, server_uuid, firewall_rule_position, server_instance=None):
        """
        Return a FirewallRule object based on server uuid and rule position.
        """
        url = f'/server/{server_uuid}/firewall_rule/{firewall_rule_position}'
        res = self.api.get_request(url)
        return FirewallRule(**res['firewall_rule'])

    def get_firewall_rules(self, server):
        """
        Return all FirewallRule objects based on a server instance or uuid.
        """
        server_uuid, server_instance = uuid_and_instance(server)

        url = f'/server/{server_uuid}/firewall_rule'
        res = self.api.get_request(url)

        return [
            FirewallRule(server=server_instance, **firewall_rule)
            for firewall_rule in res['firewall_rules']['firewall_rule']
        ]

    def create_firewall_rule(self, server, firewall_rule_body):
        """
        Create a new firewall rule for a given server uuid.

        The rule can be given as a dict or with FirewallRule.prepare_post_body().
        Returns a FirewallRule object.
        """
        server_uuid, server_instance = uuid_and_instance(server)

        url = f'/server/{server_uuid}/firewall_rule'
        body = {'firewall_rule': firewall_rule_body}
        res = self.api.post_request(url, body)

        return FirewallRule(server=server_instance, **res['firewall_rule'])

    def delete_firewall_rule(self, server_uuid, firewall_rule_position):
        """
        Delete a firewall rule based on a server uuid and rule position.
        """
        url = f'/server/{server_uuid}/firewall_rule/{firewall_rule_position}'
        return self.api.delete_request(url)

    def configure_firewall(self, server, firewall_rule_bodies):
        """
        Helper for calling create_firewall_rule in series for a list of firewall_rule_bodies.
        """
        server_uuid, server_instance = uuid_and_instance(server)

        return [self.create_firewall_rule(server_uuid, rule) for rule in firewall_rule_bodies]
