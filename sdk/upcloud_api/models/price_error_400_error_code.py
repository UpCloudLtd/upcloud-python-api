from enum import StrEnum


class PriceError400ErrorCode(StrEnum):
    PRICE_INVALID = "PRICE_INVALID"

    def __str__(self) -> str:
        return str(self.value)
