from enum import StrEnum


class DatabaseIntegrationEndpoint(StrEnum):
    LOGS = "logs"
    PROMETHEUS = "prometheus"
    RSYSLOG = "rsyslog"

    def __str__(self) -> str:
        return str(self.value)
