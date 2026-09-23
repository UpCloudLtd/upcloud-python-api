from enum import StrEnum


class ServerNicModel(StrEnum):
    E1000 = "e1000"
    RTL8139 = "rtl8139"
    VIRTIO = "virtio"

    def __str__(self) -> str:
        return str(self.value)
