from enum import StrEnum


class IpAddressIpReleasePolicy(StrEnum):
    KEEP = "keep"
    RELEASE = "release"

    def __str__(self) -> str:
        return str(self.value)
