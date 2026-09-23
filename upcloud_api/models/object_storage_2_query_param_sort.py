from enum import StrEnum


class ObjectStorage2QueryParamSort(StrEnum):
    CREATED_AT = "created_at"
    OPERATIONAL_STATE = "operational_state"
    REGION_NAME = "region_name"
    SERVICE_NAME = "service_name"
    VALUE_1 = "-created_at"
    VALUE_3 = "-service_name"
    VALUE_5 = "-operational_state"
    VALUE_7 = "-region_name"

    def __str__(self) -> str:
        return str(self.value)
