from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoadBalancerMemberCreateType0")


@_attrs_define
class LoadBalancerMemberCreateType0:
    """
    Attributes:
        type_ (Literal['static']):
        ip (str): Target IP address (IPv4 or IPv6)
        port (int): Target Port
    """

    type_: Literal["static"]
    ip: str
    port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ip: str
        ip = self.ip

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ip": ip,
                "port": port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["static"], d.pop("type"))
        if type_ != "static":
            raise ValueError(f"type must match const 'static', got '{type_}'")

        def _parse_ip(data: object) -> str:
            return cast(str, data)

        ip = _parse_ip(d.pop("ip"))

        port = d.pop("port")

        load_balancer_member_create_type_0 = cls(
            type_=type_,
            ip=ip,
            port=port,
        )

        load_balancer_member_create_type_0.additional_properties = d
        return load_balancer_member_create_type_0

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
