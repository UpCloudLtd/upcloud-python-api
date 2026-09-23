from enum import IntEnum


class AccountTokensProblem400Status(IntEnum):
    VALUE_400 = 400

    def __str__(self) -> str:
        return str(self.value)
