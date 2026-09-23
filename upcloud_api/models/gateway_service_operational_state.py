from enum import StrEnum


class GatewayServiceOperationalState(StrEnum):
    CHECKUP = "checkup"
    DELETE_DNS = "delete-dns"
    DELETE_GW = "delete-gw"
    DELETE_LINK_NETWORK = "delete-link-network"
    DELETE_NETWORK = "delete-network"
    DELETE_SERVER = "delete-server"
    DELETE_SERVICE = "delete-service"
    DETACH_LINK_NETWORK = "detach-link-network"
    PENDING = "pending"
    RUNNING = "running"
    SETUP_AGENT = "setup-agent"
    SETUP_DNS = "setup-dns"
    SETUP_GW = "setup-gw"
    SETUP_LINK_NETWORK = "setup-link-network"
    SETUP_NETWORK = "setup-network"
    SETUP_SERVICE = "setup-service"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
