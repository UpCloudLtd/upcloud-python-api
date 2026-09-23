from enum import StrEnum


class GetAvailablePassthroughDevicesType(StrEnum):
    GPU = "gpu"

    def __str__(self) -> str:
        return str(self.value)
