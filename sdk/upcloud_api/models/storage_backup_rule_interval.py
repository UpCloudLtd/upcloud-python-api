from enum import StrEnum


class StorageBackupRuleInterval(StrEnum):
    DAILY = "daily"
    FRI = "fri"
    MON = "mon"
    SAT = "sat"
    SUN = "sun"
    THU = "thu"
    TUE = "tue"
    WED = "wed"

    def __str__(self) -> str:
        return str(self.value)
