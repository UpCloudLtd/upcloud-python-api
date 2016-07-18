from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import os
import pytest

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

@integration_test
def teardown_module(module):
    manager = CloudManager(USERNAME, PASSWORD, timeout=120)

    # if we are at CIRCLECI, clean up everything
    if os.environ.get('CIRCLECI', False):
        for server in manager.get_servers():
            server.stop_and_destroy()

        for tag in manager.get_tags():
            tag.destroy()
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



    test_server = CLUSTER['web1']
    test_server.stop()
    test_server._wait_for_state_change(['stopped'])

    # contain appropriate asserts
    firewall_test(manager, FIREWALL_RULES, test_server)
    server_test(manager, test_server)
    tag_servers_test(manager, TAGS, CLUSTER)
