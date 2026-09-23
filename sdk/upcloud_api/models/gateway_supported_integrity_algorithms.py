from enum import StrEnum


class GatewaySupportedIntegrityAlgorithms(StrEnum):
    AES128GMAC = "aes128gmac"
    AES256GMAC = "aes256gmac"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def __str__(self) -> str:
        return str(self.value)
