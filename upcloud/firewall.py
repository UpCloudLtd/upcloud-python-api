#GET /1.1/server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule

from .base import BaseAPI

class Firewall(BaseAPI):

	def rules(self, UUID, rule=""):
		res = self.get("/server/" + UUID + "/firewall_rule/" + rule)
		return res


class FirewallRule(object):

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
        # set object attributes from params
        for key in kwargs:
            if key not in self.attributes:
                self._invalid_key_err(key)

            setattr(self, key, kwargs[key])

        # set attributes that were not given as empty strings
        for attr in self.attributes:
            if not hasattr(self, attr):
                setattr(self, attr, '')

    def prepare_post_body(self):
        body = {}
        for attr in self.attributes:
            body[attr] = getattr(self, attr)
        return body

    def destroy(self):
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
        attr_list = list(self.attributes.keys())
        raise Exception(
            "invalid parameter to FirewallRule, '{key}' is not in {attributes}"
            .format(key=key, attributes=attr_list)
        )

    def _associate_with_server(self, server):
        self.server = server
