from enum import StrEnum


class KubernetesEffect(StrEnum):
    NOEXECUTE = "NoExecute"
    NOSCHEDULE = "NoSchedule"
    PREFERNOSCHEDULE = "PreferNoSchedule"

    def __str__(self) -> str:
        return str(self.value)
