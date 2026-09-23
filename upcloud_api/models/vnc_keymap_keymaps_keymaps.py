from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="VncKeymapKeymapsKeymaps")


@_attrs_define
class VncKeymapKeymapsKeymaps:
    """
    Example:
        {'keymap': ['fi', 'us', 'de']}

    Attributes:
        keymap (list[str]):  Example: ['fi', 'us'].
    """

    keymap: list[str]

    def to_dict(self) -> dict[str, Any]:
        keymap = self.keymap

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keymap": keymap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keymap = cast(list[str], d.pop("keymap"))

        vnc_keymap_keymaps_keymaps = cls(
            keymap=keymap,
        )

        return vnc_keymap_keymaps_keymaps
