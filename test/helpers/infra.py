from upcloud_api.firewall import FirewallRule
from upcloud_api.ip_address import IPAddress
from upcloud_api.server import Server, login_user_block
from upcloud_api.storage import Storage
from upcloud_api.tag import Tag

CLUSTER = {
    'web1': Server(
        core_number=1,
        memory_amount=1024,
        hostname='web1.example.com',
        zone='uk-lon1',
        password_delivery='none',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030240200', size=10),
            Storage(size=10, tier='maxiops'),
        ],
    ),
    'web2': Server(
        core_number=1,
        memory_amount=1024,
        hostname='web2.example.com',
        zone='uk-lon1',
        password_delivery='none',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000030240200', size=10),
            Storage(size=10, tier='maxiops'),
        ],
        ip_addresses=[IPAddress(family='IPv6', access='public')],
    ),
    'db': Server(
        core_number=1,
        memory_amount=1024,
        hostname='db.example.com',
        zone='uk-lon1',
        password_delivery='none',
        storage_devices=[
            Storage(os='01000000-0000-4000-8000-000150020100', size=10),
            Storage(size=10, tier='standard'),
        ],
        login_user=login_user_block('testuser', ['ssh-ed25519 AAAA'], False),
    ),
    'lb': Server(
        plan='1xCPU-1GB',
        hostname='balancer.example.com',
        zone='uk-lon1',
        password_delivery='none',
        storage_devices=[Storage(os='01000000-0000-4000-8000-000020070100', size=30)],
        login_user=login_user_block('testuser', ['ssh-ed25519 AAAA'], False),
    ),
}


FIREWALL_RULES = [
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
        direction='in',
        family='IPv4',
        protocol='tcp',
        source_address_start='192.168.1.1',
        source_address_end='192.168.1.255',
        destination_port_start='21',
        destination_port_end='21',
        action='accept',
    ),
]


TAGS = [Tag('testlb'), Tag('testdb'), Tag('testweb')]
