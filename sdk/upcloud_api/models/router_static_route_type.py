from enum import StrEnum


class RouterStaticRouteType(StrEnum):
    SERVICE = "service"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
