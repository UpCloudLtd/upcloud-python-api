from enum import StrEnum


class GatewayIpsecIkeSaMetricsDetailsResponseChildSasItemState(StrEnum):
    CREATED = "created"
    DELETED = "deleted"
    DELETING = "deleting"
    DESTROYING = "destroying"
    INSTALLED = "installed"
    INSTALLING = "installing"
    REKEYED = "rekeyed"
    REKEYING = "rekeying"
    RETRYING = "retrying"
    ROUTED = "routed"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"
    UPDATING = "updating"

    def __str__(self) -> str:
        return str(self.value)
