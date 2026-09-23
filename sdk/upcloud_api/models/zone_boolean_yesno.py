from enum import StrEnum


class ZoneBooleanYesno(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
