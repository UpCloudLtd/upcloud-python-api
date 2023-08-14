import json

import responses
from conftest import Mock

from upcloud_api import IPAddress, Server, Storage, login_user_block


class TestCreateServer:
    def test_storage_prepare_post_body(self, manager):
        s1 = Storage(os='01000000-0000-4000-8000-000030200200', size=10)
        body1 = s1.to_dict()
        assert body1['tier'] == 'maxiops'
        assert body1['size'] == 10

        s2 = Storage(size=100)
        body2 = s2.to_dict()
        assert body2['tier'] == 'maxiops'
        assert body2['size'] == 100

    def test_storage_prepare_post_body_optional_attributes(self, manager):
        s2 = Storage(size=100, address='virtio:0')
        body2 = s2.to_dict()

        assert body2['tier'] == 'maxiops'
        assert body2['size'] == 100
        assert body2['address'] == 'virtio:0'

    def test_server_init(self, manager):
        server1 = Server(
            core_number=2,
            memory_amount=1024,
            hostname='my.example.com',
            zone='us-chi1',
            storage_devices=[
                Storage(os='01000000-0000-4000-8000-000030200200', size=10),
                Storage(size=100, title='storage disk 1'),
            ],
            simple_backup='0430,monthlies',
        )

        assert server1.title == 'my.example.com'
        assert server1.core_number == 2
        assert server1.memory_amount == 1024
        assert server1.hostname == server1.title
        assert server1.zone == 'us-chi1'
        assert server1.simple_backup == '0430,monthlies'

    def test_server_prepare_post_body(self):
        server = Server(
            core_number=2,
            memory_amount=1024,
            hostname='my.example.com',
            zone='us-chi1',
            storage_devices=[
                Storage(os='01000000-0000-4000-8000-000030200200', size=10),
                Storage(),
            ],
        )
        body = server.prepare_post_body()

        s1 = body['server']['storage_devices']['storage_device'][0]
        assert s1['title'] == 'my.example.com OS disk'
        assert s1['tier'] == 'maxiops'
        assert s1['size'] == 10
        assert s1['storage'] == '01000000-0000-4000-8000-000030200200'
        assert s1['action'] == 'clone'
        s2 = body['server']['storage_devices']['storage_device'][1]
        assert s2['title'] == 'my.example.com storage disk 1'
        assert s2['tier'] == 'maxiops'
        assert s2['action'] == 'create'
        assert s2['size'] == 10

        assert body['server']['title'] == 'my.example.com'
        assert body['server']['core_number'] == 2
        assert body['server']['memory_amount'] == 1024
        assert body['server']['hostname'] == server.title
        assert body['server']['zone'] == 'us-chi1'

    def test_server_prepare_post_body_optional_attributes(self):
        server1 = Server(
            core_number=2,
            memory_amount=1024,
            hostname='my.example.com',
            zone='us-chi1',
            storage_devices=[Storage(os='01000000-0000-4000-8000-000030200200', size=10)],
            vnc_password='my-passwd',
            password_delivery='email',
            login_user=login_user_block('upclouduser', ['this-is-a-SSH-key']),
            avoid_host='12345678',
            user_data='https://my.script.com/some_script.py',
            ip_addresses=[
                IPAddress(family='IPv4', access='public'),
                IPAddress(family='IPv6', access='public'),
            ],
        )

        server2_dict = {
            'core_number': 2,
            'memory_amount': 1024,
            'hostname': 'my.example.com',
            'zone': 'us-chi1',
            'storage_devices': [{'os': '01000000-0000-4000-8000-000030200200', 'size': 10}],
            'vnc_password': 'my-passwd',
            'password_delivery': 'email',
            'login_user': login_user_block('upclouduser', ['this-is-a-SSH-key']),
            'avoid_host': '12345678',
            'user_data': 'https://my.script.com/some_script.py',
            'ip_addresses': [
                {'family': 'IPv4', 'access': 'public'},
                {'family': 'IPv6', 'access': 'public'},
            ],
        }
        server2 = Server._create_server_obj(server2_dict, cloud_manager=self)

        body1 = server1.prepare_post_body()
        body2 = server2.prepare_post_body()

        for body in [body1, body2]:
            assert body['server']['title'] == 'my.example.com'
            assert body['server']['core_number'] == 2
            assert body['server']['memory_amount'] == 1024
            assert body['server']['hostname'] == server1.title
            assert body['server']['zone'] == 'us-chi1'
            assert body['server']['vnc_password'] == 'my-passwd'
            assert body['server']['password_delivery'] == 'email'
            assert body['server']['login_user'] == {
                'username': 'upclouduser',
                'create_password': 'no',
                'ssh_keys': {'ssh_key': ['this-is-a-SSH-key']},
            }
            assert body['server']['avoid_host'] == '12345678'
            assert body['server']['user_data'] == 'https://my.script.com/some_script.py'
            assert body['server']['ip_addresses'] == {
                'ip_address': [
                    {'family': 'IPv4', 'access': 'public'},
                    {'family': 'IPv6', 'access': 'public'},
                ]
            }

    @responses.activate
    def test_create_server(self, manager):
        responses.add(
            responses.POST,
            Mock.base_url + '/server',
            body=Mock.read_from_file('server_create.json'),
            status=202,
            content_type='application/json',
        )

        server1 = Server(
            core_number=2,
            memory_amount=1024,
            hostname='my.example.com',
            zone='us-chi1',
            storage_devices=[
                Storage(os='01000000-0000-4000-8000-000030200200', size=10),
                Storage(size=100, title='storage disk 1'),
            ],
        )

        manager.create_server(server1)

        # assert correct values in response
        assert type(server1).__name__ == 'Server'
        assert server1.core_number == '2'
        assert server1.memory_amount == '1024'

        # assert ips and storages have correct types
        assert type(server1.storage_devices[0]).__name__ == 'Storage'
        assert type(server1.ip_addresses[0]).__name__ == 'IPAddress'

        # assert new data was populated
        assert server1.video_model == 'cirrus'
        assert server1.vnc == 'off'
        assert server1.vnc_password == 'aabbccdd'

    @responses.activate
    def test_create_server_with_dict(self, manager):
        responses.add(
            responses.POST,
            Mock.base_url + '/server',
            body=Mock.read_from_file('server_create.json'),
            status=202,
            content_type='application/json',
        )

        server1 = {
            'core_number': 2,
            'memory_amount': 1024,
            'hostname': 'my.example.com',
            'zone': 'us-chi1',
            'simple_backup': '0430,monthlies',
            'storage_devices': [
                {'os': '01000000-0000-4000-8000-000030200200', 'size': 10},
                {'size': 100, 'title': 'storage disk 1'},
            ],
        }

        server1 = manager.create_server(server1)

        # assert correct values in response
        assert type(server1).__name__ == 'Server'
        assert server1.core_number == '2'
        assert server1.memory_amount == '1024'

        # assert ips and storages have correct types
        assert type(server1.storage_devices[0]).__name__ == 'Storage'
        assert type(server1.ip_addresses[0]).__name__ == 'IPAddress'

        # assert new data was populated
        assert server1.video_model == 'cirrus'
        assert server1.vnc == 'off'
        assert server1.vnc_password == 'aabbccdd'

        assert server1.simple_backup == '0430,monthlies'

    @responses.activate
    def test_create_server_from_template(self, manager):
        UUID = '01215a5a-c330-4565-81ca-0e0e22eac672'

        def _from_template_callback(request):
            request_body = json.loads(request.body)
            storage = request_body['server']['storage_devices']['storage_device'][0]

            # https://www.upcloud.com/api/8-servers/#creating-from-a-template
            assert storage['action'] == 'clone'
            assert storage['storage'] == UUID
            return (201, {}, Mock.read_from_file('server_create.json'))

        responses.add_callback(
            responses.POST,
            Mock.base_url + '/server',
            content_type='application/json',
            callback=_from_template_callback,
        )

        manager.create_server(
            Server(
                core_number=2,
                memory_amount=1024,
                hostname='my.example.com',
                zone='us-chi1',
                storage_devices=[
                    Storage(storage=UUID, size=10),
                ],
            )
        )
