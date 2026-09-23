from enum import StrEnum


class NetworkBooleanYesno(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
