from enum import StrEnum


class GatewaySupportedProposalAlgorithms(StrEnum):
    AES128 = "aes128"
    AES128GCM128 = "aes128gcm128"
    AES128GCM16 = "aes128gcm16"
    AES192 = "aes192"
    AES192GCM128 = "aes192gcm128"
    AES192GCM16 = "aes192gcm16"
    AES256 = "aes256"
    AES256GCM128 = "aes256gcm128"
    AES256GCM16 = "aes256gcm16"

    def __str__(self) -> str:
        return str(self.value)
