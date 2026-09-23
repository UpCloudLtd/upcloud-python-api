from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerDeviceMetadata")


@_attrs_define
class ServerDeviceMetadata:
    """
    Attributes:
        serial (str):
        memory (int): Amount of memory in MB Example: 2048.
        cores (int): Number of CPU cores Example: 2.
    """

    serial: str
    memory: int
    cores: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        serial = self.serial

        memory = self.memory

        cores = self.cores

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serial": serial,
                "memory": memory,
                "cores": cores,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        serial = d.pop("serial")

        memory = d.pop("memory")

        cores = d.pop("cores")

        server_device_metadata = cls(
            serial=serial,
            memory=memory,
            cores=cores,
        )

        server_device_metadata.additional_properties = d
        return server_device_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
