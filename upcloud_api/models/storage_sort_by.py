from enum import StrEnum


class StorageSortBy(StrEnum):
    CREATED = "created"
    SIZE = "size"
    TIER = "tier"
    TITLE = "title"
    TYPE = "type"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)
