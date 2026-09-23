from enum import StrEnum


class AccountCreateMsLmaSigningLinkResponseSigningStatusState(StrEnum):
    CANCELED = "canceled"
    COMPLETED = "completed"
    INITIATED = "initiated"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
