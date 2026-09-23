from enum import StrEnum


class ObjectStorage2EndpointResponseType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
