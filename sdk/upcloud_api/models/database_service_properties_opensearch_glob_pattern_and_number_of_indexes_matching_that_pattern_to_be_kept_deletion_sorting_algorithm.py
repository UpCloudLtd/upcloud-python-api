from enum import StrEnum


class DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDeletionSortingAlgorithm(
    StrEnum
):
    ALPHABETICAL = "alphabetical"
    CREATION_DATE = "creation_date"

    def __str__(self) -> str:
        return str(self.value)
