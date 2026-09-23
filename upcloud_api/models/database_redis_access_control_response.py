from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseRedisAccessControlResponse")


@_attrs_define
class DatabaseRedisAccessControlResponse:
    """Schema for Redis access control response.

    Attributes:
        categories (list[str] | Unset): List of command categories the user has access to. Example: ['@all', '@fast'].
        channels (list[str] | Unset): List of Pub/Sub channels the user has access to. Example: ['news', 'updates'].
        commands (list[str] | Unset): List of specific commands the user has access to. Example: ['GET', 'SET', 'DEL'].
        keys (list[str] | Unset): List of key patterns the user has access to. Example: ['user:*', 'session:*'].
    """

    categories: list[str] | Unset = UNSET
    channels: list[str] | Unset = UNSET
    commands: list[str] | Unset = UNSET
    keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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

        database_redis_access_control_response = cls(
            categories=categories,
            channels=channels,
            commands=commands,
            keys=keys,
        )

        database_redis_access_control_response.additional_properties = d
        return database_redis_access_control_response

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
