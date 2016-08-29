from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from upcloud_api import ZONE, Tag


def create_cluster(manager, cluster):
    """Create all servers in cluster."""
    for server in cluster:
        s = manager.create_server(cluster[server])

    for server in cluster:
        cluster[server].ensure_started()

    return manager.get_servers()


def firewall_test(manager, firewall_rules, server):
    """Run tests on firewall rules."""
    # add 1 rule and remove it
    server.add_firewall_rule(firewall_rules[0])

    fs = server.get_firewall_rules()
    assert len(fs) == 1

    fs[0].destroy()
    fs = server.get_firewall_rules()
    assert len(fs) == 0

    # add several rules and remove them
    server.configure_firewall(firewall_rules)

    fs = server.get_firewall_rules()
    assert len(fs) == 2

    for f in fs:
        manager.delete_firewall_rule(server.uuid, 1)

    fs = server.get_firewall_rules()
    assert len(fs) == 0


def server_test(manager, server):
    """Run tests on a server instance."""
    server.populate()

    server.core_number = '3'
    server.memory_amount = '1024'
    server.save()

    server.add_ip()

    storage = manager.create_storage(size=10, tier='maxiops', zone=ZONE.London)
    server.add_storage(storage)

    server.start()

    #sync new info from API and assert the changes from above have happened
    server.populate()
    assert server.core_number == '3'
    assert server.memory_amount == '1024'
    assert len(server.storage_devices) == 3
    assert len(server.ip_addresses) == 4

    server.ensure_started()


def tag_servers_test(manager, tags, cluster):
    """Run tests on tags."""
    # create tags
    for t in tags:
        manager.create_tag(str(t))

    cluster['web1'].add_tags(['testweb'])
    cluster['web2'].add_tags(['testweb'])
    cluster['lb'].add_tags([tags[1]]) # tags[1] is 'db'
    cluster['db'].add_tags(['testlb'])

    fetched_servers = manager.get_servers(tags_has_one=['testlb'])
    assert len(fetched_servers) == 1
    assert fetched_servers[0].tags[0] == 'testlb'
