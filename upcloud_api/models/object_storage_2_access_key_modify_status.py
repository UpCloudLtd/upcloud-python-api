from enum import StrEnum


class ObjectStorage2AccessKeyModifyStatus(StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
