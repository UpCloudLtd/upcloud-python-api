from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import input
from future import standard_library
standard_library.install_aliases()

from upcloud_api import CloudManager, Server, Storage, FirewallRule, ZONE

from time import sleep
import sys

# cluster to be used in live tests
cluster = {
    "web1": Server(
        core_number = 1,
        memory_amount = 512,
        hostname = "web1.example.com",
        zone = ZONE.London,
        password_delivery = "none",
        storage_devices = [
            Storage(os = "Ubuntu 14.04", size=10),
            Storage(size=100, tier="hdd")
        ]),

    "web2": Server(
        core_number = 1,
        memory_amount = 512,
        hostname = "web2.example.com",
        zone = ZONE.London,
        password_delivery = "none",
        storage_devices = [
            Storage(os = "Ubuntu 14.04", size=10),
            Storage(size=100, tier="hdd"),
        ]),

    "db":   Server(
        core_number = 2,
        memory_amount = 2048,
        hostname = "db.example.com",
        zone = ZONE.London,
        password_delivery = "none",
        storage_devices = [
            Storage(os = "CentOS 7.0", size=10),
            Storage(size=100),
        ]),

    "lb":   Server(
        core_number = 2,
        memory_amount = 1024,
        hostname = "balancer.example.com",
        zone = ZONE.London,
        password_delivery = "none",
        storage_devices = [
            Storage(os = "Debian 7.8", size=10)
        ])
}

firewall_rules = [
    FirewallRule(
        position = "1",
        direction = "in",
        family = "IPv4",
        protocol = "tcp",
        source_address_start = "192.168.1.1",
        source_address_end = "192.168.1.255",
        destination_port_start = "22",
        destination_port_end = "22",
        action = "accept"
    ),
    FirewallRule(
        position = "2",
        direction = "in",
        family = "IPv4",
        protocol = "tcp",
        source_address_start = "192.168.1.1",
        source_address_end = "192.168.1.255",
        destination_port_start = "21",
        destination_port_end = "21",
        action = "accept"
    )

]


def wait_until_change_state(manager, target_state):
    print('- wait until all servers are at state "{0}"'.format(target_state))

    all_servers_have_state = False
    while not all_servers_have_state:

        # assume state has changed
        all_servers_have_state = True

        # check assumption
        servers = manager.get_servers()
        for server in servers:
            if server.state != target_state:
                # assumption did not hold true
                all_servers_have_state = False

        if not all_servers_have_state:
            print(
                '-- all servers were not in "{0}" state, wait for 20 sec and retry...'
                .format(target_state)
            )
            sleep(20)

    print('- all servers at "{0}" starte'.format(target_state))

def stop_servers_and_wait(manager):
    print("- stopping servers")
    servers = manager.get_servers()

    for server in servers:
        if server.state == "started":
            server.stop()

    wait_until_change_state(manager, "stopped")

    print("- all stopped, continue")


def change_server_properties_test(manager, server):
    print("|---- server properties ----|")
    server.populate()

    print("- update RAM and CPU")
    server.core_number = '3'
    server.memory_amount = '1024'
    server.save()

    print("- add an IP address")
    server.add_IP()

    print("- create and attach a Storage")
    storage = manager.create_storage(size=10, tier='hdd', zone=ZONE.London)
    server.add_storage(storage)

    print("- start the server")
    server.start()

    #sync new info from API and assert the changes from above have happened
    print("- check the changes from the API")
    server.populate()
    assert server.core_number == '3'
    assert server.memory_amount == '1024'
    assert len(server.storage_devices) == 3
    assert len(server.ip_addresses) == 4

    # make sure servers[3] has had time to start
    print('- wait for state "started"')
    while(server.state != 'started'):
        sleep(10)
        server.populate()

    print("- succesfully tested server properties, continue")
    print("-----------------------------")


def firewall_test(manager):
    print("|--------- firewall --------|")
    server = manager.get_servers()[0]

    # add 1 rule and remove it
    print("- add 1 firewall rule and then remove it")
    server.add_firewall_rule(firewall_rules[0])

    fs = server.get_firewall_rules()
    assert len(fs) == 1

    fs[0].destroy()
    fs = server.get_firewall_rules()
    assert len(fs) == 0

    # add several rules and remove them
    print("- add several firewall rules and then remove them")
    server.configure_firewall(firewall_rules)

    fs = server.get_firewall_rules()
    assert len(fs) == 2

    for f in fs:
        manager.delete_firewall_rule(server.uuid, 1)

    fs = server.get_firewall_rules()
    assert len(fs) == 0

    print("-----------------------------")

def create_cluster(manager):
    print("|----- creating cluster -----|")
    for server in cluster:
        s = manager.create_server(cluster[server])
        print("- created", s.title)


    wait_until_change_state(manager, 'started')

    servers = manager.get_servers()
    assert len(servers) == 4

    print("all servers started, continue")
    print("-----------------------------")

    return servers


def destroy_servers(manager):
    print("|----- destroy servers -----|")

    stop_servers_and_wait(manager)

    servers = manager.get_servers()
    for server in servers:
        server.destroy()
        print("- destroyed", server.title)

    print("all servers destroyed, continue")
    print("-----------------------------")

def destroy_storages(manager):
    print("|---- destroy storages -----|")

    stop_servers_and_wait(manager)

    storages = manager.get_storages()
    for s in storages:
        s.destroy()
        print("- destroyed", s.title)

    print("all storages destroyed, continue")
    print("-----------------------------")


def live_test(username, password):
    print("|----- begin live_test -----|")
    manager = CloudManager(username, password)
    auth = manager.authenticate()

    print("- auth: ", auth)

    # set up cluster
    servers = create_cluster(manager)

    # stop one server for server properties test
    servers[3].stop()
    print("- stopped server {} for stopped-server tests".format(servers[3].title))

    # firewall tests while servers[3] is stopping
    firewall_test(manager)

    # make sure servers[3] has had time to stop
    while(servers[3].state != 'stopped'):
        print("-- waiting for {0} to stop...".format(servers[3].title))
        sleep(10)
        servers[3].populate()


    servers = manager.get_servers()
    server = None
    for s in servers:
        if s.state=='stopped':
            server = s

    change_server_properties_test(manager, server)

    # clean up
    destroy_servers(manager)
    destroy_storages(manager)


if __name__ == "__main__":

    print("""
        WARNING! This live test suite will permanently destroy all
        resources of the account it is ran with. It is meant for developers
        of upcloud-python-api and to be used with a throwaway dev account
        that is not being used to host anything important.

        This script is not packaged with releases in PyPI.

        Please type in "yes" to continue, or anything else to exit.
        """
    )
    user_input = input()
    if user_input != "yes":
        exit(sys.exit())

    if len(sys.argv) == 3:
        uname = sys.argv[1]
        passwd = sys.argv[2]
        print(uname, passwd)
        live_test(uname, passwd)

    print(
        """please give username and password as command line arguments;
        'python test/live_test.py username password'"""
    )
