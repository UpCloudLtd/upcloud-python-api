import json

import requests

from upcloud_api import __version__
from upcloud_api.errors import UpCloudAPIError


class API:
    """
    Handles basic HTTP communication with API.
    """

    api_root = 'https://api.upcloud.com/1.3'
    user_agent = f'upcloud-python-api/{__version__}'

    def __init__(self, token, timeout=None):
        """
        Initialize the API with a given Authorization token and default timeout.
        """
        self.token = token
        self.timeout = timeout

    def api_request(self, method, endpoint, body=None, params=None, timeout=-1):
        """
        Perform a request with a given JSON body to a given endpoint in UpCloud's API.

        Handles errors with __error_middleware.
        """
        if method not in {'GET', 'POST', 'PUT', 'PATCH', 'DELETE'}:
            raise Exception('Invalid/Forbidden HTTP method')

        url = f'{self.api_root}{endpoint}'
        headers = {'Authorization': self.token, 'User-Agent': self.user_agent}

        if body:
            data = json.dumps(body)
            headers['Content-Type'] = 'application/json'
        else:
            data = None

        call_timeout = timeout if timeout != -1 else self.timeout

        res = requests.request(
            method=method, url=url, data=data, params=params, headers=headers, timeout=call_timeout
        )

        if res.text:
            res_json = res.json()
        else:
            res_json = {}

        return self.__error_middleware(res, res_json)

    def get_request(self, endpoint, params=None, timeout=-1):
        """
        Perform a GET request to a given endpoint in UpCloud's API.
        """
        return self.api_request('GET', endpoint, params=params, timeout=timeout)

    def post_request(self, endpoint, body=None, timeout=-1):
        """
        Perform a POST request to a given endpoint in UpCloud's API.
        """
        return self.api_request('POST', endpoint, body=body, timeout=timeout)

    def put_request(self, endpoint, body=None, timeout=-1):
        """
        Perform a PUT request to a given endpoint in UpCloud's API.
        """
        return self.api_request('PUT', endpoint, body=body, timeout=timeout)

    def patch_request(self, endpoint, body=None, timeout=-1):
        """
        Perform a PATCH request to a given endpoint in UpCloud's API.
        """
        return self.api_request('PATCH', endpoint, body=body, timeout=timeout)

    def delete_request(self, endpoint, timeout=-1):
        """
        Perform a DELETE request to a given endpoint in UpCloud's API.
        """
        return self.api_request('DELETE', endpoint, timeout=timeout)

    def __error_middleware(self, res, res_json):
        """
        Middleware that raises an exception when HTTP statuscode is an error code.
        """
        if res.status_code >= 400:
            if res_json.get('type'):
                raise UpCloudAPIError(
                    error_code=res_json.get('title'),
                    error_message=f'Details: {json.dumps(res_json)}',
                )

            err_dict = res_json.get('error', {})
            raise UpCloudAPIError(
                error_code=err_dict.get('error_code'), error_message=err_dict.get('error_message')
            )

        return res_json
