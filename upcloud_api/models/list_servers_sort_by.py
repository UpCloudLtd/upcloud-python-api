from enum import StrEnum


class ListServersSortBy(StrEnum):
    CORES = "cores"
    MEMORY = "memory"
    POPULARITY = "popularity"
    SIZE = "size"
    TITLE = "title"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)
