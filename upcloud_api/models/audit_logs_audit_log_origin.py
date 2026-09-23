from enum import StrEnum


class AuditLogsAuditLogOrigin(StrEnum):
    API = "api"
    GUI = "gui"
    UPCLOUD_INTERNAL = "upcloud_internal"

    def __str__(self) -> str:
        return str(self.value)
