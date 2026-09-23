from enum import StrEnum


class DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogLogLevel(StrEnum):
    DEBUG = "debug"
    INFO = "info"
    TRACE = "trace"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
