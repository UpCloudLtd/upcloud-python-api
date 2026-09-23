from enum import StrEnum


class DatabaseServicePropertiesPgPgbouncerIgnoreStartupParametersItem(StrEnum):
    EXTRA_FLOAT_DIGITS = "extra_float_digits"
    SEARCH_PATH = "search_path"

    def __str__(self) -> str:
        return str(self.value)
