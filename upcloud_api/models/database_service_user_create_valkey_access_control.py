from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServiceUserCreateValkeyAccessControl")


@_attrs_define
class DatabaseServiceUserCreateValkeyAccessControl:
    """Valkey access control settings

    Attributes:
        categories (list[str] | Unset): List of categories for Valkey ACL
        channels (list[str] | Unset): List of channels for Valkey ACL
        commands (list[str] | Unset): List of commands for Valkey ACL
        keys (list[str] | Unset): List of keys for Valkey ACL
    """

    categories: list[str] | Unset = UNSET
    channels: list[str] | Unset = UNSET
    commands: list[str] | Unset = UNSET
    keys: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        commands: list[str] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = self.commands

        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if channels is not UNSET:
            field_dict["channels"] = channels
        if commands is not UNSET:
            field_dict["commands"] = commands
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = cast(list[str], d.pop("categories", UNSET))

        channels = cast(list[str], d.pop("channels", UNSET))

        commands = cast(list[str], d.pop("commands", UNSET))

        keys = cast(list[str], d.pop("keys", UNSET))

        database_service_user_create_valkey_access_control = cls(
            categories=categories,
            channels=channels,
            commands=commands,
            keys=keys,
        )

        return database_service_user_create_valkey_access_control
