from enum import StrEnum


class GatewayQueryParamSortServices(StrEnum):
    CREATED_AT = "created_at"
    NAME = "name"
    UUID = "uuid"
    VALUE_1 = "-created_at"
    VALUE_3 = "-name"
    VALUE_5 = "-uuid"

    def __str__(self) -> str:
        return str(self.value)
