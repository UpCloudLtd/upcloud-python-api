from enum import StrEnum


class ServerNetworkStatsSummaryVariableItemTitle(StrEnum):
    IN = "In"
    OUT = "Out"

    def __str__(self) -> str:
        return str(self.value)
