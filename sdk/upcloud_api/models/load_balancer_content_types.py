from enum import StrEnum


class LoadBalancerContentTypes(StrEnum):
    APPLICATIONJAVASCRIPT = "application/javascript"
    APPLICATIONJSON = "application/json"
    TEXTHTML = "text/html"
    TEXTPLAIN = "text/plain"

    def __str__(self) -> str:
        return str(self.value)
