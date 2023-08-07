import base64

from upcloud_api.api import API
from upcloud_api.cloud_manager.firewall_mixin import FirewallManager
from upcloud_api.cloud_manager.host_mixin import HostManager
from upcloud_api.cloud_manager.ip_address_mixin import IPManager
from upcloud_api.cloud_manager.lb_mixin import LoadBalancerManager
from upcloud_api.cloud_manager.network_mixin import NetworkManager
from upcloud_api.cloud_manager.object_storage_mixin import ObjectStorageManager
from upcloud_api.cloud_manager.server_mixin import ServerManager
from upcloud_api.cloud_manager.storage_mixin import StorageManager
from upcloud_api.cloud_manager.tag_mixin import TagManager


class CloudManager(
    FirewallManager,
    HostManager,
    IPManager,
    LoadBalancerManager,
    NetworkManager,
    ObjectStorageManager,
    ServerManager,
    StorageManager,
    TagManager,
):
    """
    CloudManager contains the core functionality of the upcloud API library.

    All other managers are mixed in so code can be organized in corresponding sub-manager classes.
    """

    api: API

    def __init__(self, username: str, password: str, timeout: int = 60) -> None:
        """
        Initiates CloudManager that handles all HTTP connections with UpCloud's API.

        Optionally determine a timeout for API connections (in seconds). A timeout with the value
        `None` means that there is no timeout.
        """
        if not username or not password:
            raise Exception('Invalid credentials, please provide a username and password')

        credentials = f'{username}:{password}'.encode()
        encoded_credentials = base64.b64encode(credentials).decode()

        self.api = API(
            token=f'Basic {encoded_credentials}',
            timeout=timeout,
        )

    def authenticate(self):
        """
        Authenticate.
        """
        return self.get_account()

    def get_account(self):
        """
        Returns information on the user's account and resource limits.
        """
        return self.api.get_request('/account')

    def get_zones(self):
        """
        Returns a list of available zones.
        """
        return self.api.get_request('/zone')

    def get_timezones(self):
        """
        Returns a list of available timezones.
        """
        return self.api.get_request('/timezone')

    def get_prices(self):
        """
        Returns a list of resource prices.
        """
        return self.api.get_request('/price')

    def get_server_sizes(self):
        """
        Returns a list of available server configurations.
        """
        return self.api.get_request('/server_size')

    def get_server_plans(self):
        """
        Returns a list of available server plans
        :return:
        """
        return self.api.get_request('/plan')
