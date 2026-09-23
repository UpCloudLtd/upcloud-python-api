from enum import StrEnum


class KubernetesClusterPlan(StrEnum):
    DEVELOPMENT = "development"
    DEV_MD = "dev-md"
    PRODUCTION_SMALL = "production-small"
    PROD_MD = "prod-md"
    PROD_MD_HA = "prod-md-ha"

    def __str__(self) -> str:
        return str(self.value)
