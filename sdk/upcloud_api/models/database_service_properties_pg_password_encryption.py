from enum import StrEnum


class DatabaseServicePropertiesPgPasswordEncryption(StrEnum):
    MD5 = "md5"
    SCRAM_SHA_256 = "scram-sha-256"

    def __str__(self) -> str:
        return str(self.value)
