from enum import StrEnum


class AccountResourceNetworkUsageType(StrEnum):
    LOAD_BALANCER_PRIVATE = "load_balancer_private"
    LOAD_BALANCER_PRIVATE_VLAN = "load_balancer_private_vlan"
    LOAD_BALANCER_PUBLIC = "load_balancer_public"
    NETWORK_GATEWAY_PRIVATE = "network_gateway_private"
    NETWORK_GATEWAY_PRIVATE_VLAN = "network_gateway_private_vlan"
    NETWORK_GATEWAY_PUBLIC = "network_gateway_public"
    OBJECT_STORAGE_V2_PRIVATE = "object_storage_v2_private"
    OBJECT_STORAGE_V2_PUBLIC = "object_storage_v2_public"
    SERVER_PRIVATE = "server_private"
    SERVER_PRIVATE_VLAN = "server_private_vlan"
    SERVER_PUBLIC = "server_public"

    def __str__(self) -> str:
        return str(self.value)
