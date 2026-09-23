from enum import StrEnum


class DatabaseServicePropertiesPgSynchronousReplication(StrEnum):
    OFF = "off"
    QUORUM = "quorum"

    def __str__(self) -> str:
        return str(self.value)
