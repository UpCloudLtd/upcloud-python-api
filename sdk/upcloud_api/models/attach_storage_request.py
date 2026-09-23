from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.attach_storage_request_storage_device import AttachStorageRequestStorageDevice


T = TypeVar("T", bound="AttachStorageRequest")


@_attrs_define
class AttachStorageRequest:
    """Request schema for attaching this storage resource to a Cloud Server.

    Example:
        {'storage_device': {'server': '00798b85-efdc-41ca-8021-f6ef457b8531', 'type': 'disk'}}

    Attributes:
        storage_device (AttachStorageRequestStorageDevice): Parameters for attaching this storage resource to a Cloud
            Server in the same zone.
    """

    storage_device: AttachStorageRequestStorageDevice

    def to_dict(self) -> dict[str, Any]:
        storage_device = self.storage_device.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storage_device": storage_device,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attach_storage_request_storage_device import AttachStorageRequestStorageDevice  # noqa: PLC0415

        d = dict(src_dict)
        storage_device = AttachStorageRequestStorageDevice.from_dict(d.pop("storage_device"))

        attach_storage_request = cls(
            storage_device=storage_device,
        )

        return attach_storage_request
