from enum import StrEnum


class KubernetesClusterUpgradeStrategyType(StrEnum):
    MANUAL = "manual"
    ROLLING_UPDATE = "rolling-update"

    def __str__(self) -> str:
        return str(self.value)
