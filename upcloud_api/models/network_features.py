from enum import StrEnum


class NetworkFeatures(StrEnum):
    ALLOW_CGNAT_ADDRESS = "allow-cgnat-address"
    ALLOW_LINKLOCAL_ADDRESS = "allow-linklocal-address"
    ALLOW_OVERLAPPING_IP_NETWORK = "allow-overlapping-ip-network"
    MANAGED_BY_SERVICE = "managed-by-service"

    def __str__(self) -> str:
        return str(self.value)
