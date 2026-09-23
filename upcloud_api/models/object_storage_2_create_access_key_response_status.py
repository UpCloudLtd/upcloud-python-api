from enum import StrEnum


class ObjectStorage2CreateAccessKeyResponseStatus(StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
