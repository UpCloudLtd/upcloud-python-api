from enum import StrEnum


class AuditLogsFormatParameter(StrEnum):
    CSV = "csv"
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
