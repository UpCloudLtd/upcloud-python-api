from enum import StrEnum


class DatabaseServiceIntegration(StrEnum):
    LOGS = "logs"
    PROMETHEUS = "prometheus"
    RSYSLOG = "rsyslog"

    def __str__(self) -> str:
        return str(self.value)
