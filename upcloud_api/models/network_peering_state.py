from enum import StrEnum


class NetworkPeeringState(StrEnum):
    ACTIVE = "active"
    CONFLICT_SUBNET = "conflict-subnet"
    DELETED_PEER_NETWORK = "deleted-peer-network"
    DISABLED = "disabled"
    ERROR = "error"
    MISSING_LOCAL_ROUTER = "missing-local-router"
    MISSING_PEER_ROUTER = "missing-peer-router"
    PEER_DISABLED = "peer-disabled"
    PENDING_PEER = "pending-peer"
    PROVISIONING = "provisioning"

    def __str__(self) -> str:
        return str(self.value)
