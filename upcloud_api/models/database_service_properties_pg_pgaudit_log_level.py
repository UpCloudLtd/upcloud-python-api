from enum import StrEnum


class DatabaseServicePropertiesPgPgauditLogLevel(StrEnum):
    DEBUG1 = "debug1"
    DEBUG2 = "debug2"
    DEBUG3 = "debug3"
    DEBUG4 = "debug4"
    DEBUG5 = "debug5"
    INFO = "info"
    LOG = "log"
    NOTICE = "notice"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
