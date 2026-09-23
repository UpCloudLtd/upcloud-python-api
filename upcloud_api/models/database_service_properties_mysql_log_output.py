from enum import StrEnum


class DatabaseServicePropertiesMysqlLogOutput(StrEnum):
    INSIGHTS = "INSIGHTS"
    INSIGHTSTABLE = "INSIGHTS,TABLE"
    NONE = "NONE"
    TABLE = "TABLE"

    def __str__(self) -> str:
        return str(self.value)
