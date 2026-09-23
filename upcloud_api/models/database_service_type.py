from enum import StrEnum


class DatabaseServiceType(StrEnum):
    MYSQL = "mysql"
    OPENSEARCH = "opensearch"
    PG = "pg"
    VALKEY = "valkey"

    def __str__(self) -> str:
        return str(self.value)
