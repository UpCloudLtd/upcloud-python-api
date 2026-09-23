from enum import StrEnum


class DatabasePlanComponentsResponseBackupsName(StrEnum):
    EXTENDED = "extended"
    MINI = "mini"
    REGULAR = "regular"

    def __str__(self) -> str:
        return str(self.value)
