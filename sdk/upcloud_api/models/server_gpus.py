from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_gpus_gpus_item import ServerGpusGpusItem


T = TypeVar("T", bound="ServerGpus")


@_attrs_define
class ServerGpus:
    """GPUs attached to a Cloud Server. The array is empty when no GPUs are attached.

    Example:
        {'gpus': [{'cores': 5888, 'firmware': '92.00.18.00.01', 'memory_gib': 24, 'model': 'NVIDIA RTX A5000', 'part':
            '900-5G132-2500-000', 'serial': 'GPU-01234567'}]}

    Attributes:
        gpus (list[ServerGpusGpusItem]):
    """

    gpus: list[ServerGpusGpusItem]

    def to_dict(self) -> dict[str, Any]:
        gpus = []
        for gpus_item_data in self.gpus:
            gpus_item = gpus_item_data.to_dict()
            gpus.append(gpus_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gpus": gpus,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_gpus_gpus_item import ServerGpusGpusItem  # noqa: PLC0415

        d = dict(src_dict)
        gpus = []
        _gpus = d.pop("gpus")
        for gpus_item_data in _gpus:
            gpus_item = ServerGpusGpusItem.from_dict(gpus_item_data)

            gpus.append(gpus_item)

        server_gpus = cls(
            gpus=gpus,
        )

        return server_gpus
