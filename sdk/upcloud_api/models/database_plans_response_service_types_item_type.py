from enum import StrEnum


class DatabasePlansResponseServiceTypesItemType(StrEnum):
    MYSQL = "mysql"
    PG = "pg"

    def __str__(self) -> str:
        return str(self.value)
