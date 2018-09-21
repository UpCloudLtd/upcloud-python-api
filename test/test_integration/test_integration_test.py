from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import os
import pytest
import multiprocessing

from upcloud_api import CloudManager

from infra import CLUSTER, TAGS, FIREWALL_RULES
from infra_helpers import (
    create_cluster,
    firewall_test,
    server_test,
    tag_servers_test
)


USERNAME = os.environ.get('UPCLOUD_API_USER')
PASSWORD = os.environ.get('UPCLOUD_API_PASSWD')


integration_test = pytest.mark.skipif(
    not pytest.config.getoption('--integration-tests'),
    reason='need --integration-tests option to run'
)


# globals to store created resources so we can cleanup after tests
CREATED_SERVERS = []
CREATED_TAGS = []


def destroy_server(server):
    """Destroy a server and it's storages."""
    server.stop_and_destroy()


def delete_tag(tag):
    """Destroy a tag (only works if the tag is not in use)."""
    tag.destroy()


@integration_test
def teardown_module(module):
    manager = CloudManager(USERNAME, PASSWORD, timeout=160)

    # if we are at CIRCLECI, clean up everything
    if os.environ.get('CIRCLECI', False):
        pool = multiprocessing.Pool()
        pool.map(destroy_server, manager.get_servers())
        pool.map(delete_tag, manager.get_tags())
    else:
        print('removing {}'.format(CREATED_SERVERS))
        for server in CREATED_SERVERS:
            server.stop_and_destroy()

        print('removing {}'.format(CREATED_TAGS))
        for tag in CREATED_TAGS:
            manager.delete_tag(tag)


@integration_test
def test_infra_ops():
    global CREATED_SERVERS
    global CREATED_TAGS

    CREATED_TAGS = TAGS

    manager = CloudManager(USERNAME, PASSWORD, timeout=120)

    try:
        auth = manager.authenticate()
        assert True
    except Exception:
        assert False

    all_servers = create_cluster(manager, CLUSTER)

    # collect & populate servers from CLUSTER
    cluster_servers = []
    for name in CLUSTER:
        server = CLUSTER[name]
        server.populate()
        cluster_servers.append(server)

    CREATED_SERVERS = cluster_servers

    # assert all_servers contain cluster_servers
    for cs in cluster_servers:
        assert cs.state == 'started'

        found = False
        for server in all_servers:
            if server.uuid == cs.uuid:
                found = True

        if not found:
            raise Exception('server {} not found in all_servers'.format(cs.uuid))

    # assert servers' states
    # TODO(elnygren): add more assertions here

    # web2 non default IP configuration
    web2 = CLUSTER['web2']
    assert len(web2.ip_addresses) == 1
    assert web2.ip_addresses[0].family == 'IPv6'

    test_server = CLUSTER['web1']

    test_server.populate()
    test_server._wait_for_state_change(['started'])
    test_server.stop()
    test_server._wait_for_state_change(['stopped'])

    # contain appropriate asserts
    firewall_test(manager, FIREWALL_RULES, test_server)
    server_test(manager, test_server)
    tag_servers_test(manager, TAGS, CLUSTER)
