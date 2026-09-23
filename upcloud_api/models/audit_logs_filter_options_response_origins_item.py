from enum import StrEnum


class AuditLogsFilterOptionsResponseOriginsItem(StrEnum):
    API = "api"
    GUI = "gui"
    UPCLOUD_INTERNAL = "upcloud_internal"

    def __str__(self) -> str:
        return str(self.value)
