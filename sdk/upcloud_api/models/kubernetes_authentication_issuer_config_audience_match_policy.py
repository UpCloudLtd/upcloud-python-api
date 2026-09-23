from enum import StrEnum


class KubernetesAuthenticationIssuerConfigAudienceMatchPolicy(StrEnum):
    MATCHANY = "MatchAny"
    VALUE_1 = ""

    def __str__(self) -> str:
        return str(self.value)
