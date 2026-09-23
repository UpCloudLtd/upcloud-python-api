from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerGpusGpusItem")


@_attrs_define
class ServerGpusGpusItem:
    """
    Attributes:
        model (str): Model name of the GPU
        firmware (None | str | Unset): Firmware version of the GPU
        serial (None | str | Unset): Serial number of the GPU
        part (None | str | Unset): Part number of the GPU
        memory_gib (int | None | Unset): Memory size of the GPU in GiB
        cores (int | None | Unset): Number of processing cores in the GPU
    """

    model: str
    firmware: None | str | Unset = UNSET
    serial: None | str | Unset = UNSET
    part: None | str | Unset = UNSET
    memory_gib: int | None | Unset = UNSET
    cores: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        firmware: None | str | Unset
        if isinstance(self.firmware, Unset):
            firmware = UNSET
        else:
            firmware = self.firmware

        serial: None | str | Unset
        if isinstance(self.serial, Unset):
            serial = UNSET
        else:
            serial = self.serial

        part: None | str | Unset
        if isinstance(self.part, Unset):
            part = UNSET
        else:
            part = self.part

        memory_gib: int | None | Unset
        if isinstance(self.memory_gib, Unset):
            memory_gib = UNSET
        else:
            memory_gib = self.memory_gib

        cores: int | None | Unset
        if isinstance(self.cores, Unset):
            cores = UNSET
        else:
            cores = self.cores

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model": model,
            }
        )
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if serial is not UNSET:
            field_dict["serial"] = serial
        if part is not UNSET:
            field_dict["part"] = part
        if memory_gib is not UNSET:
            field_dict["memory_gib"] = memory_gib
        if cores is not UNSET:
            field_dict["cores"] = cores

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        def _parse_firmware(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        firmware = _parse_firmware(d.pop("firmware", UNSET))

        def _parse_serial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial = _parse_serial(d.pop("serial", UNSET))

        def _parse_part(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        part = _parse_part(d.pop("part", UNSET))

        def _parse_memory_gib(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_gib = _parse_memory_gib(d.pop("memory_gib", UNSET))

        def _parse_cores(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cores = _parse_cores(d.pop("cores", UNSET))

        server_gpus_gpus_item = cls(
            model=model,
            firmware=firmware,
            serial=serial,
            part=part,
            memory_gib=memory_gib,
            cores=cores,
        )

        return server_gpus_gpus_item
