import json

import responses
from conftest import Mock

from upcloud_api import Tag


def tag_post_callback(request):
    print(request.body)
    request_body = json.loads(request.body)

    if 'name' not in request_body['tag']:
        raise Exception('required field missing')

    if 'servers' in request_body['tag']:
        assert isinstance(request_body['tag']['servers'], dict)
        assert isinstance(request_body['tag']['servers']['server'], list)
        if len(request_body['tag']['servers']['server']) > 0:
            assert isinstance(request_body['tag']['servers']['server'][0], str)

    if 'description' in request_body['tag']:
        assert isinstance(request_body['tag']['description'], str)

    return (201, {}, json.dumps(request_body))


class TestTags:
    @responses.activate
    def test_get_tag(self, manager):
        Mock.mock_get('tag/TheTestTag')
        tag = manager.get_tag('TheTestTag')

        assert tag.name == 'TheTestTag'
        assert tag.description == 'Description of TheTestTag'
        assert len(tag.servers) == 2
        assert tag.servers[0].uuid == '0057e20a-6878-43a7-b2b3-530c4a4bdc55'

    @responses.activate
    def test_get_tags(self, manager):
        Mock.mock_get('tag')
        tags = manager.get_tags()

        assert len(tags) == 2
        assert tags[0].name == 'TheTestTag1'
        assert tags[1].name == 'TheTestTag2'
        assert tags[0].servers[0].uuid == '0057e20a-6878-43a7-b2b3-530c4a4bdc55'

    @responses.activate
    def test_create_new_tag(self, manager):
        for _ in range(1, 4):
            responses.add_callback(
                responses.POST,
                Mock.base_url + '/tag',
                content_type='application/json',
                callback=tag_post_callback,
            )

        tag1 = manager.create_tag('Tag1')
        tag2 = manager.create_tag('Tag2', 'a nice tag')
        tag3 = manager.create_tag('Tag3', 'a nicer tag', ['00798b85-efdc-41ca-8021-f6ef457b8531'])

        assert tag1.name == 'Tag1'
        assert tag2.name == 'Tag2'
        assert tag3.name == 'Tag3'
        assert isinstance(tag3.servers, list)
        assert tag3.servers[0].uuid == '00798b85-efdc-41ca-8021-f6ef457b8531'

    @responses.activate
    def test_edit_tag(self, manager):
        Mock.mock_get('tag/TheTestTag')
        tag = manager.get_tag('TheTestTag')

        responses.add_callback(
            responses.PUT,
            Mock.base_url + '/tag/TheTestTag',
            content_type='application/json',
            callback=tag_post_callback,
        )

        tag.name = 'AnotherTestTag'
        assert tag._api_name == 'TheTestTag'

        tag.save()

        assert tag.name == 'AnotherTestTag'
        assert tag._api_name == 'AnotherTestTag'

    @responses.activate
    def test_assign_tags_to_server(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        responses.add(
            responses.POST,
            Mock.base_url + '/server/00798b85-efdc-41ca-8021-f6ef457b8531/tag/tag1,tag2',
            body=json.dumps({'foo': 'bar'}),
            content_type='application/json',
            status=200,
        )
        server.add_tags(['tag1', Tag('tag2')])

        for tag in ['web1', 'tag1', 'tag2']:
            assert tag in server.tags

    @responses.activate
    def test_remove_tags_from_server(self, manager):
        data = Mock.mock_get('server/00798b85-efdc-41ca-8021-f6ef457b8531')
        server = manager.get_server('00798b85-efdc-41ca-8021-f6ef457b8531')

        responses.add(
            responses.POST,
            Mock.base_url + '/server/00798b85-efdc-41ca-8021-f6ef457b8531/untag/tag1,tag2',
            body=json.dumps({'foo': 'bar'}),
            content_type='application/json',
            status=200,
        )
        server.remove_tags(['tag1', Tag('tag2')])

        for tag in ['tag1', 'tag2']:
            assert tag not in server.tags
        assert 'web1' in server.tags
