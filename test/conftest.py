from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object, open
from future import standard_library
standard_library.install_aliases()

import json, os, pytest, responses

@pytest.fixture(scope='module')
def manager():
    import upcloud_api
    return upcloud_api.CloudManager("testuser", "mock-api-password")


class Mock(object):
	base_url = 'https://api.upcloud.com/1.2'

	@staticmethod
	def read_from_file(filename):

		filename = filename.replace("/", "_")

		cwd = os.path.dirname(__file__)
		f = open(cwd + '/json_data/'+filename, 'r')
		return f.read()

	@staticmethod
	def mock_get(target, response_file=None):
		if not response_file:
			response_file = target + '.json'

		data = Mock.read_from_file(response_file)
		responses.add(responses.GET, Mock.base_url + '/' + target,
						body=data,
						status=200,
						content_type='application/json')
		return data

	@staticmethod
	def __put_post_callback(request, target, data):
		data_field = target.split("/")[0]
		payload = json.loads(request.body)

		for field in data[data_field]:
			if field in payload[data_field]:
				data[data_field][field] = payload[data_field][field]
		return(200, {}, json.dumps(data))

	@staticmethod
	def mock_post(target):
		data = json.loads( Mock.read_from_file(target + '_post.json') )

		def callback(request):
			return Mock.__put_post_callback(request, target, data)

		responses.add_callback(responses.POST, Mock.base_url + '/' + target,
								callback=callback,
								content_type='application/json')

	@staticmethod
	def mock_put(target):
		data = json.loads( Mock.read_from_file(target + '.json') )

		def callback(request):
			return Mock.__put_post_callback(request, target, data)

		responses.add_callback(responses.PUT, Mock.base_url + '/' + target,
								callback=callback,
								content_type='application/json')
	@staticmethod
	def mock_delete(target):
		# print(Mock.base_url + "/" + target)
		responses.add(responses.DELETE, Mock.base_url + "/" + target,
						status = 204 )

	@staticmethod
	def mock_server_operation(target):
		# drop third (last) part of a string divided by two slashes ("/"); e.g "this/is/string" -> "this/is"
		targetsplit = target.split("/")
		targetfile = "/".join( targetsplit[:2] )

		data = json.loads( Mock.read_from_file(targetfile + '.json') )

		# API will always respond state: "started", see: Server.stop, Server.start, Server,restart
		data["server"]["state"] = "started"

		data = json.dumps( data )
		responses.add(responses.POST, Mock.base_url + "/" + target, status=200, body = data, content_type='application/json')




