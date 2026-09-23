from enum import StrEnum


class DatabasePlansResponseServiceTypesItemComputeShapesItemFamily(StrEnum):
    DEVELOPMENT = "development"
    MEMORY = "memory"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
