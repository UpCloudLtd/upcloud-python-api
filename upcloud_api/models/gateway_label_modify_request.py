from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayLabelModifyRequest")


@_attrs_define
class GatewayLabelModifyRequest:
    """Gateway label

    Attributes:
        key (str | Unset): The key of a label.
        value (None | str | Unset): The value of a label.
    """

    key: str | Unset = UNSET
    value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        gateway_label_modify_request = cls(
            key=key,
            value=value,
        )

        return gateway_label_modify_request
