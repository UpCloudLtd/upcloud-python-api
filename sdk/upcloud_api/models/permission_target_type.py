from enum import StrEnum


class PermissionTargetType(StrEnum):
    FILE_STORAGE = "file_storage"
    INTERFACE = "interface"
    MANAGED_CONTAINER_REGISTRY = "managed_container_registry"
    MANAGED_DATABASE = "managed_database"
    MANAGED_KUBERNETES = "managed_kubernetes"
    MANAGED_LOADBALANCER = "managed_loadbalancer"
    MANAGED_OBJECT_STORAGE = "managed_object_storage"
    NETWORK = "network"
    NETWORK_GATEWAY = "network_gateway"
    OBJECT_STORAGE = "object_storage"
    ROUTER = "router"
    SERVER = "server"
    SSH_KEY = "ssh_key"
    STORAGE = "storage"
    TAG_ACCESS = "tag_access"

    def __str__(self) -> str:
        return str(self.value)
