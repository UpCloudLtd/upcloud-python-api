from __future__ import unicode_literals

import json
import requests

from upcloud_api import UpCloudAPIError


class BaseAPI(object):
    """
    CloudManager base that handles basic HTTP communication with API.
    """

    api = 'api.upcloud.com'
    api_v = '1.3'

    def __init__(self, token, timeout=None):  # noqa
        self.token = token
        self.timeout = timeout

    def request(self, method, endpoint, body=None, timeout=-1, request_to_api=True):
        """
        Perform a request with a given body to a given endpoint in UpCloud's API or UpCloud's uploader session.

        Handles errors with __error_middleware.
        """
        if method not in set(['GET', 'POST', 'PUT', 'DELETE']):
            raise Exception('Invalid/Forbidden HTTP method')

        url = 'https://api.upcloud.com/' + self.api_v + endpoint if request_to_api else endpoint
        headers = {
            'Authorization': self.token
        }

        headers['Content-Type'] = 'application/json' if request_to_api else 'application/octet-stream'

        if body and request_to_api:
            data = json.dumps(body)
        elif body and not request_to_api:
            data = body
        else:
            data = None

        call_timeout = timeout if timeout != -1 else self.timeout

        APIcall = getattr(requests, method.lower())
        res = APIcall(url,
                      data=data,
                      headers=headers,
                      timeout=call_timeout)

        if res.text:
            res_json = res.json()
        else:
            res_json = {}

        return self.__error_middleware(res, res_json)

    def get_request(self, endpoint, timeout=-1):
        """
        Perform a GET request to a given endpoint in UpCloud's API.
        """
        return self.request('GET', endpoint, timeout=timeout)

    def post_request(self, endpoint, body=None, timeout=-1):
        """
        Perform a POST request to a given endpoint in UpCloud's API.
        """
        return self.request('POST', endpoint, body, timeout)

    def put_request(self, endpoint, body=None, timeout=-1, request_to_api=True):
        """
        Perform a PUT request to a given endpoint in UpCloud's API or UpCloud's uploader session.
        """
        return self.request('PUT', endpoint, body, timeout, request_to_api=request_to_api)

    def __error_middleware(self, res, res_json):
        """
        Middleware that raises an exception when HTTP statuscode is an error code.
        """
        if(res.status_code in [400, 401, 402, 403, 404, 405, 406, 409]):
            err_dict = res_json.get('error', {})
            raise UpCloudAPIError(error_code=err_dict.get('error_code'),
                                  error_message=err_dict.get('error_message'))

        return res_json
