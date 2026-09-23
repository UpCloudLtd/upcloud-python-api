from enum import StrEnum


class DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingAuthenticationBackend(
    StrEnum
):
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
