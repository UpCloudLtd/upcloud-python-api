from enum import StrEnum


class DatabaseConnectionPoolCreatePoolMode(StrEnum):
    SESSION = "session"
    STATEMENT = "statement"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
