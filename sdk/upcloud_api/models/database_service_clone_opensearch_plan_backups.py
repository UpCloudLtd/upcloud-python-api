from enum import StrEnum


class DatabaseServiceCloneOpensearchPlanBackups(StrEnum):
    EXTENDED = "extended"
    MINI = "mini"
    REGULAR = "regular"

    def __str__(self) -> str:
        return str(self.value)
