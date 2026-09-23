from enum import StrEnum


class ServerRebuildServerRebuildPasswordDelivery(StrEnum):
    EMAIL = "email"
    NONE = "none"
    SMS = "sms"

    def __str__(self) -> str:
        return str(self.value)
