from enum import StrEnum


class DatabaseServicePropertiesPgPgbouncerPGBouncerPoolMode(StrEnum):
    SESSION = "session"
    STATEMENT = "statement"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
