from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.vnc_keymap_keymaps_keymaps import VncKeymapKeymapsKeymaps


T = TypeVar("T", bound="VncKeymapKeymaps")


@_attrs_define
class VncKeymapKeymaps:
    """List of available VNC keymaps

    Example:
        {'keymaps': {'keymap': ['fi', 'us', 'de']}}

    Attributes:
        keymaps (VncKeymapKeymapsKeymaps):  Example: {'keymap': ['fi', 'us', 'de']}.
    """

    keymaps: VncKeymapKeymapsKeymaps

    def to_dict(self) -> dict[str, Any]:
        keymaps = self.keymaps.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keymaps": keymaps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vnc_keymap_keymaps_keymaps import VncKeymapKeymapsKeymaps  # noqa: PLC0415

        d = dict(src_dict)
        keymaps = VncKeymapKeymapsKeymaps.from_dict(d.pop("keymaps"))

        vnc_keymap_keymaps = cls(
            keymaps=keymaps,
        )

        return vnc_keymap_keymaps
