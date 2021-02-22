from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import


from upcloud_api import IPAddress, Server
from conftest import read_from_file
import json


class TestIP(object):

    def test_ip_in_server_creation(self):
        """IPAddress in server creation.

        https://www.upcloud.com/api/8-servers/#create-server
        """
        ip1 = IPAddress(family='IPv4', access='public')
        ip2 = IPAddress(family='IPv6', access='private')
        assert ip1.to_dict() == {'family': 'IPv4', 'access': 'public'}
        assert ip2.to_dict() == {'family': 'IPv6', 'access': 'private'}

    def test_ip_in_server_details(self):
        """IPAddress in server details.

        https://www.upcloud.com/api/8-servers/#get-server-details
        """
        ip = IPAddress(access='private', address='10.0.0.0', family='IPv4')
        assert ip.to_dict() == {
            'access': 'private',
            'address': '10.0.0.0',
            'family': 'IPv4'
        }

        data = read_from_file('server_00798b85-efdc-41ca-8021-f6ef457b8531.json')
        s = Server(**json.loads(data))
        for ip in s.ip_addresses:
            assert set(ip.to_dict().keys()) == set(['address', 'family', 'access'])

    def test_ip_details(self):
        """IPAdress LIST/GET.

        https://www.upcloud.com/api/10-ip-addresses/#list-ip-addresses
        """
        ip = IPAddress(**json.loads(read_from_file('ip_address_10.1.0.101.json'))['ip_address'])
        assert ip.to_dict() == {
            'access': 'private',
            'address': '10.1.0.101',
            'family': 'IPv4',
            'part_of_plan': 'yes',
            'ptr_record': 'a.ptr.record',
            'server': '008c365d-d307-4501-8efc-cd6d3bb0e494'
        }
