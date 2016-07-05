from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from upcloud_api import CloudManager, Storage, FirewallRule, ZONE, Tag
from upcloud_api.server import Server, login_user_block


CLUSTER = {
    'web1': Server(
        core_number = 1,
        memory_amount = 512,
        hostname = 'web1.example.com',
        zone = ZONE.London,
        password_delivery = 'none',
        storage_devices = [
            Storage(os = 'Ubuntu 14.04', size=10),
            Storage(size=10, tier='maxiops')
        ]),

    'web2': Server(
        core_number = 1,
        memory_amount = 512,
        hostname = 'web2.example.com',
        zone = ZONE.London,
        password_delivery = 'none',
        storage_devices = [
            Storage(os = 'Ubuntu 14.04', size=10),
            Storage(size=10, tier='maxiops'),
        ]),

    'db':   Server(
        core_number = 1,
        memory_amount = 512,
        hostname = 'db.example.com',
        zone = ZONE.London,
        password_delivery = 'none',
        storage_devices = [
            Storage(os = 'CentOS 7.0', size=10),
            Storage(size=10),
        ],
        login_user = login_user_block('testuser', ['ssh-rsa AAAAB3NzaC1yc2EAA[...]ptshi44x user@some.host'], True),
        ),


    'lb':   Server(
        plan= '1xCPU-1GB',
        hostname = 'balancer.example.com',
        zone = ZONE.London,
        password_delivery = 'none',
        storage_devices = [
            Storage(os = 'Debian 7.8', size=30)
        ],
        login_user = login_user_block('testuser', ['ssh-rsa AAAAB3NzaC1yc2EAA[...]ptshi44x user@some.host'], True),
        )
}


FIREWALL_RULES = [
    FirewallRule(
        position = '1',
        direction = 'in',
        family = 'IPv4',
        protocol = 'tcp',
        source_address_start = '192.168.1.1',
        source_address_end = '192.168.1.255',
        destination_port_start = '22',
        destination_port_end = '22',
        action = 'accept'
    ),
    FirewallRule(
        position = '2',
        direction = 'in',
        family = 'IPv4',
        protocol = 'tcp',
        source_address_start = '192.168.1.1',
        source_address_end = '192.168.1.255',
        destination_port_start = '21',
        destination_port_end = '21',
        action = 'accept'
    )
]


TAGS = [
    Tag('testlb'),
    Tag('testdb'),
    Tag('testweb')
]
