from enum import StrEnum


class ObjectStorage2ServiceDetailResponseOperationalState(StrEnum):
    CLEANUP_DELETED_BUCKETS = "cleanup-deleted-buckets"
    DELETE_BUCKETS = "delete-buckets"
    DELETE_DNS = "delete-dns"
    DELETE_IAM = "delete-iam"
    DELETE_NAMESPACE = "delete-namespace"
    DELETE_NETWORK = "delete-network"
    DELETE_PRIVATE_ENDPOINT = "delete-private-endpoint"
    DELETE_PUBLIC_ENDPOINT = "delete-public-endpoint"
    DELETE_SERVICE = "delete-service"
    DELETE_TLS = "delete-tls"
    PENDING = "pending"
    RUNNING = "running"
    SETUP_CHECKUP = "setup-checkup"
    SETUP_DNS = "setup-dns"
    SETUP_IAM = "setup-iam"
    SETUP_NETWORK = "setup-network"
    SETUP_PRIVATE_ENDPOINT = "setup-private-endpoint"
    SETUP_PUBLIC_ENDPOINT = "setup-public-endpoint"
    SETUP_SERVICE = "setup-service"
    SETUP_TLS = "setup-tls"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
