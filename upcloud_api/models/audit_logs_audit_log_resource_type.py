from enum import StrEnum


class AuditLogsAuditLogResourceType(StrEnum):
    ACCOUNT = "account"
    AUTH = "auth"
    INIT_SCRIPT = "init-script"
    MANAGED_DATABASE = "managed-database"
    MANAGED_LOADBALANCER = "managed-loadbalancer"
    MANAGED_LOADBALANCER_CERTIFICATE_BUNDLE = "managed-loadbalancer-certificate-bundle"
    MANAGED_OBJECT_STORAGE = "managed-object-storage"
    NETWORK_GATEWAY = "network-gateway"
    SERVER = "server"
    SSH_KEY = "ssh-key"
    STORAGE = "storage"
    UKS = "uks"

    def __str__(self) -> str:
        return str(self.value)
