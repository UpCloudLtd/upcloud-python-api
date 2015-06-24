from .. import FirewallRule

class FirewallManager():

    def get_firewall_rule(self, server_uuid, firewall_rule_position):
        url = "/server/" + server_uuid + "/firewall_rule/" + str(firewall_rule_position)
        res = self.get_request(url)
        return FirewallRule(**res['firewall_rule'])

    def get_firewall_rules(self, server_uuid):
        url = "/server/" + server_uuid + "/firewall_rule"

        res = self.get_request(url)


        firewall_rules = []
        for firewall_rule in res['firewall_rules']['firewall_rule']:
            firewall_rules.append(FirewallRule(**firewall_rule))

        return firewall_rules

    def create_firewall_rule(self, server_uuid, firewall_rule_body):
        url = "/server/" + server_uuid + "/firewall_rule"
        res = self.post_request(url, firewall_rule_body)
        return FirewallRule(**res['firewall_rule'])

    def delete_firewall_rule(self, server_uuid, firewall_rule_position):
        url = "/server/" + server_uuid + "/firewall_rule/" + str(firewall_rule_position)
        return self.request('DELETE', url)
