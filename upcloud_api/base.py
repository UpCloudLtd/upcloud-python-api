from __future__ import unicode_literals

import json
import requests

from upcloud_api import UpCloudAPIError


class BaseAPI(object):
    """
    CloudManager base that handles basic HTTP communication with API.
    """

    api = 'api.upcloud.com'
    api_v = '1.2'

    def __init__(self, token, timeout=None):  # noqa
        self.token = token
        self.timeout = timeout

    def request(self, method, endpoint, body=None):
        """
        Perform a request with a given body to a given endpoint in UpCloud's API.

        Handles errors with __error_middleware.
        """
        if method not in set(['GET', 'POST', 'PUT', 'DELETE']):
            raise Exception('Invalid/Forbidden HTTP method')

        url = '/' + self.api_v + endpoint
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        if body:
            json_body_or_None = json.dumps(body)
        else:
            json_body_or_None = None

        APIcall = getattr(requests, method.lower())
        res = APIcall('https://api.upcloud.com' + url,
                      data=json_body_or_None,
                      headers=headers,
                      timeout=self.timeout)

        if res.text:
            res_json = res.json()
        else:
            res_json = {}

        return self.__error_middleware(res, res_json)

    def get_request(self, endpoint):
        """
        Perform a GET request to a given endpoint in UpCloud's API.
        """
        return self.request('GET', endpoint)

    def post_request(self, endpoint, body=None):
        """
        Perform a POST request to a given endpoint in UpCloud's API.
        """
        return self.request('POST', endpoint, body)

    def __error_middleware(self, res, res_json):
        """
        Middleware that raises an exception when HTTP statuscode is an error code.
        """
        if(res.status_code in [400, 401, 402, 403, 404, 405, 406, 409]):
            err_dict = res_json.get('error', {})
            raise UpCloudAPIError(error_code=err_dict.get('error_code'),
                                  error_message=err_dict.get('error_message'))

        return res_json
