from enum import IntEnum


class AccountTokensProblem403Status(IntEnum):
    VALUE_403 = 403

    def __str__(self) -> str:
        return str(self.value)
