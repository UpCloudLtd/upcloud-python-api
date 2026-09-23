from enum import StrEnum


class DatabaseServicePropertiesOpensearchSearchBackpressureTheSearchBackpressureMode(StrEnum):
    DISABLED = "disabled"
    ENFORCED = "enforced"
    MONITOR_ONLY = "monitor_only"

    def __str__(self) -> str:
        return str(self.value)
