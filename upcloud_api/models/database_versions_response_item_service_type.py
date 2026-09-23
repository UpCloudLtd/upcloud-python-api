from enum import StrEnum


class DatabaseVersionsResponseItemServiceType(StrEnum):
    MYSQL = "mysql"
    OPENSEARCH = "opensearch"
    PG = "pg"
    VALKEY = "valkey"

    def __str__(self) -> str:
        return str(self.value)
