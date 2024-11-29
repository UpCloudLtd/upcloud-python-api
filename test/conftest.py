import json
import os
import sys

import pytest
import responses

# make files under helpers available for import
HELPERS_PATH = os.path.join(os.path.dirname(__file__), 'helpers')
sys.path.append(HELPERS_PATH)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration_tests: mark test to run only on if --integration-tests is passed"
    )


def pytest_addoption(parser):
    parser.addoption(
        '--integration-tests', action='store_true', default=False, help='run integration tests'
    )


def pytest_runtest_setup(item):
    if 'integration_tests' in item.keywords and not item.config.getoption("--integration-tests"):
        pytest.skip("need --integration-tests option to run this test")


@pytest.fixture(scope='module')
def manager():
    import upcloud_api

    return upcloud_api.CloudManager("testuser", "mock-api-password")


def read_from_file(filename):
    filename = filename.replace("/", "_")
    cwd = os.path.dirname(__file__)
    f = open(cwd + '/json_data/' + filename)
    return f.read()


class Mock:
    base_url = 'https://api.upcloud.com/1.3'

    @staticmethod
    def read_from_file(filename):
        return read_from_file(filename)

    @staticmethod
    def mock_get(target, response_file=None):
        if not response_file:
            response_file = target + '.json'

        data = Mock.read_from_file(response_file)
        responses.add(
            responses.GET,
            Mock.base_url + '/' + target,
            body=data,
            status=200,
            content_type='application/json',
        )
        return data

    @staticmethod
    def __put_patch_post_callback(
        request, target, data, ignore_data_field=False, empty_payload=False
    ):
        data_field = target.split("/")[0]

        if not empty_payload:
            payload = json.loads(request.body)

        if not ignore_data_field:
            for field in data[data_field]:
                if field in payload[data_field]:
                    data[data_field][field] = payload[data_field][field]
        return (200, {}, json.dumps(data))

    @staticmethod
    def mock_post(target, empty_content=False, ignore_data_field=False, empty_payload=False):
        def callback(request):
            if not empty_content:
                data = json.loads(Mock.read_from_file(target + '_post.json'))
                return Mock.__put_patch_post_callback(
                    request, target, data, ignore_data_field, empty_payload
                )
            else:
                return (200, {}, '{}')

        responses.add_callback(
            responses.POST,
            Mock.base_url + '/' + target,
            callback=callback,
            content_type='application/json',
        )

    @staticmethod
    def mock_put(target, ignore_data_field=False, empty_payload=False, call_api=True):
        data = json.loads(Mock.read_from_file(target + '.json'))

        def callback(request):
            return Mock.__put_patch_post_callback(
                request, target, data, ignore_data_field, empty_payload
            )

        url = Mock.base_url + '/' + target if call_api else target
        responses.add_callback(
            responses.PUT, url, callback=callback, content_type='application/json'
        )

    @staticmethod
    def mock_patch(target, ignore_data_field=False, empty_payload=False, call_api=True):
        data = json.loads(Mock.read_from_file(target + '.json'))

        def callback(request):
            return Mock.__put_patch_post_callback(
                request, target, data, ignore_data_field, empty_payload
            )

        url = Mock.base_url + '/' + target if call_api else target
        responses.add_callback(
            responses.PATCH, url, callback=callback, content_type='application/json'
        )

    @staticmethod
    def mock_delete(target):
        responses.add(responses.DELETE, Mock.base_url + '/' + target, status=204)

    @staticmethod
    def mock_server_operation(target):
        # drop third (last) part of a string divided by two slashes ("/"); e.g "this/is/string" -> "this/is"
        targetsplit = target.split('/')
        targetfile = '/'.join(targetsplit[:2])

        data = json.loads(Mock.read_from_file(targetfile + '.json'))

        # API will always respond state: "started", see: Server.stop, Server.start, Server,restart
        data['server']['state'] = 'started'

        data = json.dumps(data)
        responses.add(
            responses.POST,
            Mock.base_url + "/" + target,
            status=200,
            body=data,
            content_type='application/json',
        )
