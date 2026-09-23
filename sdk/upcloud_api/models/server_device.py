from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_device_metadata import ServerDeviceMetadata


T = TypeVar("T", bound="ServerDevice")


@_attrs_define
class ServerDevice:
    """Schema for passthrough device information.

    Example:
        {'serial': '1723925007011', 'type': 'gpu', 'model': 'NVIDIA L40S', 'metadata': {'serial': '1723925007011',
            'memory': 48, 'cores': 18176}}

    Attributes:
        serial (str):
        type_ (str):
        model (str):
        metadata (ServerDeviceMetadata):
    """

    serial: str
    type_: str
    model: str
    metadata: ServerDeviceMetadata

    def to_dict(self) -> dict[str, Any]:
        serial = self.serial

        type_ = self.type_

        model = self.model

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serial": serial,
                "type": type_,
                "model": model,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_device_metadata import ServerDeviceMetadata  # noqa: PLC0415

        d = dict(src_dict)
        serial = d.pop("serial")

        type_ = d.pop("type")

        model = d.pop("model")

        metadata = ServerDeviceMetadata.from_dict(d.pop("metadata"))

        server_device = cls(
            serial=serial,
            type_=type_,
            model=model,
            metadata=metadata,
        )

        return server_device
