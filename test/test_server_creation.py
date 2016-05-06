from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from future import standard_library
standard_library.install_aliases()

from upcloud_api import ZONE, Server, Storage, login_user_block

from conftest import Mock
import json, pytest, responses


class TestCreateServer(object):

  def test_storage_prepare_post_body(self, manager):
    s1 = Storage(os='Ubuntu 14.04', size=10)
    body1 = s1.prepare_post_body('my.example.com', 1)

    assert body1['title'] == 'my.example.com OS disk'
    assert body1['tier'] == 'maxiops'
    assert body1['size'] == 10
    assert body1['storage'] == '01000000-0000-4000-8000-000030040200'
    assert body1['action'] == 'clone'

    s2 = Storage(size=100)
    body2 = s2.prepare_post_body('my.example.com', 1)

    assert body2['title'] == 'my.example.com storage disk 1'
    assert body2['tier'] == 'maxiops'
    assert body2['action'] == 'create'
    assert body2['size'] == 100

  def test_storage_prepare_post_body_optional_attributes(self, manager):
    s2 = Storage(size=100, address='virtio:0', type='disk')
    body2 = s2.prepare_post_body('my.example.com', 1)

    assert body2['title'] == 'my.example.com storage disk 1'
    assert body2['tier'] == 'maxiops'
    assert body2['action'] == 'create'
    assert body2['size'] == 100
    assert body2['address'] == 'virtio:0'
    assert body2['type'] == 'disk'

  def test_server_init(self, manager):
    server1 = Server(core_number=2, memory_amount=1024, hostname='my.example.com',zone=ZONE.Chicago, storage_devices=[
        Storage(os='Ubuntu 14.04', size=10),
        Storage(size=100, title='storage disk 1')
      ])

    assert server1.title == 'my.example.com'
    assert server1.core_number == 2
    assert server1.memory_amount == 1024
    assert server1.hostname == server1.title
    assert server1.zone == 'us-chi1'


  def test_server_prepare_post_body(self):
    server = Server(
        core_number=2,
        memory_amount=1024,
        hostname='my.example.com',
        zone=ZONE.Chicago,
        storage_devices=[
            Storage(os='Ubuntu 14.04', size=10),
            Storage()
        ]
    )
    body = server.prepare_post_body()

    s1 = body['server']['storage_devices']['storage_device'][0]
    assert s1['title'] == 'my.example.com OS disk'
    assert s1['tier'] == 'maxiops'
    assert s1['size'] == 10
    assert s1['storage'] == '01000000-0000-4000-8000-000030040200'
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
    server = Server(
        core_number=2,
        memory_amount=1024,
        hostname='my.example.com',
        zone=ZONE.Chicago,
        storage_devices=[
            Storage(
                os='Ubuntu 14.04',
                size=10
            )
        ],
        vnc_password='my-passwd',
        password_delivery='email',
        login_user=login_user_block('upclouduser', ['this-is-a-SSH-key']),
        avoid_host='12345678'
    )

    body = server.prepare_post_body()
    assert body['server']['title'] == 'my.example.com'
    assert body['server']['core_number'] == 2
    assert body['server']['memory_amount'] == 1024
    assert body['server']['hostname'] == server.title
    assert body['server']['zone'] == 'us-chi1'
    assert body['server']['vnc_password'] == 'my-passwd'
    assert body['server']['password_delivery'] == 'email'
    assert body['server']['login_user'] == {
        'username': 'upclouduser',
        'create_password': 'yes',
        'ssh_keys': {
            'ssh_key': [ 'this-is-a-SSH-key' ]
        }
    }
    assert body['server']['avoid_host'] == '12345678'

  @responses.activate
  def test_create_server(self, manager):

    responses.add(
      responses.POST,
      Mock.base_url + '/server',
      body = Mock.read_from_file('server_create.json'),
      status = 202,
      content_type='application/json'
    )

    server1 = Server(core_number=2, memory_amount=1024, hostname='my.example.com',zone=ZONE.Chicago, storage_devices=[
        Storage(os='Ubuntu 14.04', size=10),
        Storage(size=100, title='storage disk 1')
      ])

    manager.create_server(server1)

    # assert correct values in response
    assert type(server1).__name__ == 'Server'
    assert server1.core_number == '2'
    assert server1.memory_amount == '1024'

    # assert ips and storages have correct types
    assert type(server1.storage_devices[0]).__name__ == 'Storage'
    assert type(server1.ip_addresses[0]).__name__ == 'IP_address'

    # assert new data was populated
    assert server1.video_model ==  'cirrus'
    assert server1.vnc ==  'off'
    assert server1.vnc_password ==  'aabbccdd'

  @responses.activate
  def test_create_server_with_dict(self, manager):
    responses.add(
      responses.POST,
      Mock.base_url + '/server',
      body = Mock.read_from_file('server_create.json'),
      status = 202,
      content_type='application/json'
    )

    server1 = {
      'core_number': 2, 'memory_amount': 1024, 'hostname': 'my.example.com', 'zone': ZONE.Chicago,
      'storage_devices': [
        { 'os': 'Ubuntu 14.04', 'size': 10 },
        { 'size': 100, 'title': 'storage disk 1' },
      ]}

    server1 = manager.create_server(server1)

    # assert correct values in response
    assert type(server1).__name__ == 'Server'
    assert server1.core_number == '2'
    assert server1.memory_amount == '1024'

    # assert ips and storages have correct types
    assert type(server1.storage_devices[0]).__name__ == 'Storage'
    assert type(server1.ip_addresses[0]).__name__ == 'IP_address'

    # assert new data was populated
    assert server1.video_model ==  'cirrus'
    assert server1.vnc ==  'off'
    assert server1.vnc_password ==  'aabbccdd'
