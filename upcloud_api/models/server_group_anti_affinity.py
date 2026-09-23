from enum import StrEnum


class ServerGroupAntiAffinity(StrEnum):
    NO = "no"
    STRICT = "strict"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
