from enum import StrEnum


class ObjectStorage2NetworkType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
