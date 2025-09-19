from upcloud_api.api import API
from upcloud_api.cloud_manager.firewall_mixin import FirewallManager
from upcloud_api.cloud_manager.host_mixin import HostManager
from upcloud_api.cloud_manager.ip_address_mixin import IPManager
from upcloud_api.cloud_manager.lb_mixin import LoadBalancerManager
from upcloud_api.cloud_manager.network_mixin import NetworkManager
from upcloud_api.cloud_manager.server_mixin import ServerManager
from upcloud_api.cloud_manager.storage_mixin import StorageManager
from upcloud_api.cloud_manager.tag_mixin import TagManager
from upcloud_api.credentials import Credentials
from upcloud_api.errors import UpCloudClientError


class CloudManager(
    FirewallManager,
    HostManager,
    IPManager,
    LoadBalancerManager,
    NetworkManager,
    ServerManager,
    StorageManager,
    TagManager,
):
    """
    CloudManager contains the core functionality of the upcloud API library.

    All other managers are mixed in so code can be organized in corresponding sub-manager classes.
    """

    api: API

    def __init__(
        self, username: str = None, password: str = None, timeout: int = 60, token: str = None
    ) -> None:
        """
        Initiates CloudManager that handles all HTTP connections with UpCloud's API.

        Optionally determine a timeout for API connections (in seconds). A timeout with the value
        `None` means that there is no timeout.
        """
        credentials = Credentials(username, password, token)
        if not credentials.is_defined:
            raise UpCloudClientError(
                "Credentials are not defined. Please provide username and password or an API token."
            )

        self.api = API(
            token=credentials.authorization,
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
