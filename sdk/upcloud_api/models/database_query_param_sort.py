from enum import StrEnum


class DatabaseQueryParamSort(StrEnum):
    CREATED_AT = "created_at"
    NAME = "name"
    OPERATIONAL_STATE = "operational_state"
    VALUE_1 = "-created_at"
    VALUE_3 = "-name"
    VALUE_5 = "-operational_state"
    VALUE_7 = "-zone"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)
