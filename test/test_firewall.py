import json

import responses
from conftest import Mock

from upcloud_api import FirewallRule


def firewall_rule_callback(request):
    """
    Checks that firewall rule contains required fields.
    Returns the same body with 201 Created.
    """
    required_fields = [
        'position',
        'direction',
        'family',
        'protocol',
        'source_address_start',
        'source_address_end',
        'destination_port_start',
        'destination_port_end',
        'action',
    ]

    request_body = json.loads(request.body)

    def check_fields(body):
        """
        Helper for checking a firewall rule body against required_fields.
        """
        for field in required_fields:
            if field not in request_body['firewall_rule']:
                raise Exception(f'missing required field: {field}. Body was:{request_body}')

    if isinstance(request_body, list):
        for body in request_body:
            check_fields(body)
    else:
        check_fields(request_body)

    return (201, {}, json.dumps(request_body))


class TestFirewall:
    @responses.activate
    def test_add_firewall_rule(self, manager):
        Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        responses.add_callback(
            responses.POST,
            Mock.base_url + '/server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule',
            content_type='application/json',
            callback=firewall_rule_callback,
        )

        returned_firewall = server.add_firewall_rule(
            FirewallRule(
                position='1',
                direction='in',
                family='IPv4',
                protocol='tcp',
                source_address_start='192.168.1.1',
                source_address_end='192.168.1.255',
                destination_port_start='22',
                destination_port_end='22',
                action='accept',
            )
        )

        # everything should run without errors, returned created object
        assert returned_firewall.position == '1'
        assert returned_firewall.direction == 'in'
        assert returned_firewall.source_address_end == '192.168.1.255'

    @responses.activate
    def test_remove_firewall_rule(self, manager):
        Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        target = 'server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule'
        Mock.mock_get(target, 'firewall_rules.json')
        firewall_rules = server.get_firewall_rules()

        Mock.mock_delete('server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule/1')
        res = firewall_rules[0].destroy()

        Mock.mock_delete('server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule/1')
        res = server.remove_firewall_rule(firewall_rules[0])

        assert res == {}

    @responses.activate
    def test_list_and_get_firewall_rules(self, manager):
        Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        target = 'server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule'
        Mock.mock_get(target, 'firewall_rules.json')
        firewall_rules = server.get_firewall_rules()

        assert firewall_rules[0].position == '1'

    @responses.activate
    def test_configure_firewall(self, manager):
        Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        responses.add_callback(
            responses.POST,
            Mock.base_url + '/server/00798b85-efdc-41ca-8021-f6ef457b8531/firewall_rule',
            content_type='application/json',
            callback=firewall_rule_callback,
        )

        returned_firewall = server.configure_firewall(
            [
                FirewallRule(
                    position='1',
                    direction='in',
                    family='IPv4',
                    protocol='tcp',
                    source_address_start='192.168.1.1',
                    source_address_end='192.168.1.255',
                    destination_port_start='22',
                    destination_port_end='22',
                    action='accept',
                ),
                FirewallRule(
                    position='2',
                    direction='out',
                    family='IPv4',
                    protocol='tcp',
                    source_address_start='192.168.1.1',
                    source_address_end='192.168.1.255',
                    destination_port_start='22',
                    destination_port_end='22',
                    action='accept',
                ),
            ]
        )

        # everything should run without errors, returned created object
        assert returned_firewall[0].position == '1'
        assert returned_firewall[0].direction == 'in'
        assert returned_firewall[0].source_address_end == '192.168.1.255'
        assert returned_firewall[1].position == '2'
        assert returned_firewall[1].direction == 'out'
        assert returned_firewall[1].source_address_end == '192.168.1.255'
