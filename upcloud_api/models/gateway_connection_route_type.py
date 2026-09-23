from enum import StrEnum


class GatewayConnectionRouteType(StrEnum):
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
