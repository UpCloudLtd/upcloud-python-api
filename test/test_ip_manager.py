from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from conftest import Mock
import responses

class TestIP(object):
    @responses.activate
    def test_get_ip(self, manager):
        data = Mock.mock_get('ip_address/10.1.0.101')
        ip_addr = manager.get_ip('10.1.0.101')

        assert type(ip_addr).__name__ == 'IPAddress'
        assert ip_addr.address == '10.1.0.101'
        assert ip_addr.ptr_record == 'a.ptr.record'

    @responses.activate
    def test_get_ips(self, manager):
        data = Mock.mock_get('ip_address')
        ip_addrs = manager.get_ips()

        for ip_addr in ip_addrs:
            assert type(ip_addr).__name__ == 'IPAddress'

    @responses.activate
    def test_modify_ip_oop(self, manager):
        # get ip
        data = Mock.mock_get('ip_address/10.1.0.101')
        ip_addr = manager.get_ip('10.1.0.101')

        # put ip
        data = Mock.mock_put('ip_address/10.1.0.101')
        ip_addr.ptr_record = 'my.ptr.record'
        ip_addr.save()

        assert ip_addr.ptr_record == 'my.ptr.record'

    @responses.activate
    def test_modify_ip(self, manager):
        data = Mock.mock_put('ip_address/10.1.0.101')
        ip_addr = manager.modify_ip('10.1.0.101', ptr_record='my.ptr.record')

        assert ip_addr.ptr_record == 'my.ptr.record'

    @responses.activate
    def test_modify_ip(self, manager):
        data = Mock.mock_put('ip_address/10.1.0.101')
        ip_addr = manager.modify_ip('10.1.0.101', ptr_record='my.ptr.record')
        assert ip_addr.ptr_record == 'my.ptr.record'

    @responses.activate
    def test_ip_delete(self, manager):
        Mock.mock_delete('ip_address/10.1.0.101')
        res = manager.release_ip('10.1.0.101')
        assert res == {}
