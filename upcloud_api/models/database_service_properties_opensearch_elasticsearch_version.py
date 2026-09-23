from enum import StrEnum


class DatabaseServicePropertiesOpensearchElasticsearchVersion(StrEnum):
    VALUE_0 = "1"
    VALUE_1 = "2"
    VALUE_2 = "2.19"
    VALUE_3 = "3.3"
    VALUE_4 = "3.6"

    def __str__(self) -> str:
        return str(self.value)
