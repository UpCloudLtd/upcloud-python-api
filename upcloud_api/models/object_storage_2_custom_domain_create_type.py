from enum import StrEnum


class ObjectStorage2CustomDomainCreateType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
