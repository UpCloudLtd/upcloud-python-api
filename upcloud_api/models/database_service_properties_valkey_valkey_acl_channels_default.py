from enum import StrEnum


class DatabaseServicePropertiesValkeyValkeyAclChannelsDefault(StrEnum):
    ALLCHANNELS = "allchannels"
    RESETCHANNELS = "resetchannels"

    def __str__(self) -> str:
        return str(self.value)
