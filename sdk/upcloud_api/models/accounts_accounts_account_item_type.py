from enum import StrEnum


class AccountsAccountsAccountItemType(StrEnum):
    MAIN = "main"
    SUB = "sub"

    def __str__(self) -> str:
        return str(self.value)
