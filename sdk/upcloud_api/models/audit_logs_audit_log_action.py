from enum import StrEnum


class AuditLogsAuditLogAction(StrEnum):
    ACCESS_GRANTED = "access-granted"
    ACCESS_GRANTED_KUBECONFIG = "access-granted-kubeconfig"
    ACCESS_MODIFIED = "access-modified"
    ACCESS_UPDATE = "access-update"
    ATTACH = "attach"
    CLONE = "clone"
    CREATE = "create"
    DELETE = "delete"
    DETACH = "detach"
    LOGIN = "login"
    LOGOUT = "logout"
    MAINTENANCE_START = "maintenance-start"
    OWNER_CHANGE = "owner-change"
    READ = "read"
    START = "start"
    STOP = "stop"
    UPDATE = "update"
    WRITES_ENABLE = "writes-enable"

    def __str__(self) -> str:
        return str(self.value)
