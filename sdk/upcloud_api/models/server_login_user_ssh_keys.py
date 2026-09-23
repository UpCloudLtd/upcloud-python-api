from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServerLoginUserSshKeys")


@_attrs_define
class ServerLoginUserSshKeys:
    """
    Attributes:
        ssh_key (list[str]):
    """

    ssh_key: list[str]

    def to_dict(self) -> dict[str, Any]:
        ssh_key = self.ssh_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ssh_key": ssh_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssh_key = cast(list[str], d.pop("ssh_key"))

        server_login_user_ssh_keys = cls(
            ssh_key=ssh_key,
        )

        return server_login_user_ssh_keys
