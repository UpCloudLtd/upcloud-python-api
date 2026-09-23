from enum import StrEnum


class ObjectStorage2CustomDomainModifyType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
