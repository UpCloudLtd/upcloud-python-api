from enum import StrEnum


class RouterType(StrEnum):
    NORMAL = "normal"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
