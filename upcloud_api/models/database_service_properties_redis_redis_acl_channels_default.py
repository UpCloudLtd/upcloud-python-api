from enum import StrEnum


class DatabaseServicePropertiesRedisRedisAclChannelsDefault(StrEnum):
    ALLCHANNELS = "allchannels"
    RESETCHANNELS = "resetchannels"

    def __str__(self) -> str:
        return str(self.value)
