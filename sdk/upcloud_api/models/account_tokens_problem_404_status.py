from enum import IntEnum


class AccountTokensProblem404Status(IntEnum):
    VALUE_404 = 404

    def __str__(self) -> str:
        return str(self.value)
