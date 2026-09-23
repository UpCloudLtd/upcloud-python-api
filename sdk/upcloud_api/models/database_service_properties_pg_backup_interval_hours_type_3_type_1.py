from enum import IntEnum


class DatabaseServicePropertiesPgBackupIntervalHoursType3Type1(IntEnum):
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_8 = 8
    VALUE_12 = 12
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
