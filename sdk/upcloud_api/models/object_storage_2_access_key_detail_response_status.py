from enum import StrEnum


class ObjectStorage2AccessKeyDetailResponseStatus(StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
