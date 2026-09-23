from enum import StrEnum


class DatabaseNetworkInformationDetailsResponseFamily(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"

    def __str__(self) -> str:
        return str(self.value)
