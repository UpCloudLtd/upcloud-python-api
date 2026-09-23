from enum import StrEnum


class PlanFamily(StrEnum):
    CLOUD_NATIVE = "cloud_native"
    DEVELOPER = "developer"
    GENERAL_PURPOSE = "general_purpose"
    GPU = "gpu"
    PREMIUM = "premium"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
