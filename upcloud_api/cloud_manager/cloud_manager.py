from __future__ import unicode_literals
from __future__ import absolute_import
import base64

from upcloud_api.cloud_manager import (
    BaseAPI,
    ServerManager,
    IPManager,
    StorageManager,
    FirewallManager,
    TagManager,
    NetworkManager,
    HostManager,
    ObjectStorageManager
)


class CloudManager(BaseAPI, ServerManager, IPManager, StorageManager, FirewallManager, TagManager, NetworkManager, HostManager, ObjectStorageManager):
    """
    CloudManager contains the core functionality of the upcloud API library.

    All other managers are mixed in so code can be organized in corresponding submanager classes.
    """

    def __init__(self, username, password, timeout=60):
        """
        Initiates CloudManager that handles all HTTP conections with UpCloud's API.

        Optionally determine a timeout for API connections (in seconds). A timeout with the value
        `None` means that there is no timeout.
        """
        if not username or not password:
            raise Exception(
                'Invalid credentials, please provide a username and password')

        credentials = '{0}:{1}'.format(username, password).encode()
        encoded_credentials = base64.b64encode(credentials).decode()

        self.token = 'Basic {0}'.format(encoded_credentials)
        self.timeout = timeout

    def authenticate(self):
        return self.get_account()

    def get_account(self):
        return self.get_request('/account')

    def get_zones(self):
        return self.get_request('/zone')

    def get_timezones(self):
        return self.get_request('/timezone')

    def get_prices(self):
        return self.get_request('/price')

    def get_server_sizes(self):
        return self.get_request('/server_size')
