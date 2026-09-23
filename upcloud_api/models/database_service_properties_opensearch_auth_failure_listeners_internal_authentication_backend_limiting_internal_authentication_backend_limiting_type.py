from enum import StrEnum


class DatabaseServicePropertiesOpensearchAuthFailureListenersInternalAuthenticationBackendLimitingInternalAuthenticationBackendLimitingType(
    StrEnum
):
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
