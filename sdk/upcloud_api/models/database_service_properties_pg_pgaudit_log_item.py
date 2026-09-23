from enum import StrEnum


class DatabaseServicePropertiesPgPgauditLogItem(StrEnum):
    ALL = "all"
    DDL = "ddl"
    FUNCTION = "function"
    MISC = "misc"
    MISC_SET = "misc_set"
    READ = "read"
    ROLE = "role"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
