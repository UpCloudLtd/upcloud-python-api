from enum import StrEnum


class ObjectStorage2ServiceDetailResponseStateMessagesItemCode(StrEnum):
    BUCKETS_STUCK_IN_DELETION = "buckets_stuck_in_deletion"
    FAILED_CUSTOM_DOMAIN_VERIFICATION = "failed_custom_domain_verification"
    FAILED_DOMAIN_VERIFICATION = "failed_domain_verification"
    NAMESPACE_STUCK_IN_DELETION = "namespace_stuck_in_deletion"
    WAITING_CERTIFICATE_ISSUING = "waiting_certificate_issuing"

    def __str__(self) -> str:
        return str(self.value)
