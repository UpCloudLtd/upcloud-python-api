from enum import StrEnum


class ObjectStorage2CustomDomainCreateMode(StrEnum):
    API = "api"
    STATIC_WEBSITE = "static-website"

    def __str__(self) -> str:
        return str(self.value)
