from enum import StrEnum


class ObjectStorage2ServiceDomainsDomainsItemType(StrEnum):
    CUSTOM = "custom"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
