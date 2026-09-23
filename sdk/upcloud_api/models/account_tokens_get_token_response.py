from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountTokensGetTokenResponse")


@_attrs_define
class AccountTokensGetTokenResponse:
    """A token.

    Example:
        {'id': '0c848138-2559-4562-9520-b1f22c4ae751', 'name': 'token', 'token_type': 'workspace', 'created_at':
            '2025-03-25T13:46:19.502878Z', 'expires_at': '2025-03-25T14:16:19.502644Z', 'can_create_tokens': True,
            'allowed_ip_ranges': ['1.2.3.4'], 'gui': False}

    Attributes:
        id (UUID | Unset): UUID of the token
        name (str | Unset): The name of the token. Does not need to be unique.
        created_at (datetime.datetime | Unset): Token creation time. Example: 2025-11-30T08:03:15.944Z.
        expires_at (datetime.datetime | Unset): The requested expiry time of the token, in RFC3339 format
            (2025-10-12T07:20:50.52Z). Needs to be in the future and maximum of 1 year in the future. Example:
            2025-11-30T08:03:15.944Z.
        last_used_at (datetime.datetime | Unset): The last time the token was used. Example: 2025-11-30T08:03:15.944Z.
        can_create_tokens (bool | Unset): Whether the token can create other tokens. Default: False. Example: False.
        gui (bool | Unset): Token is for internal GUI use. Can not be used externally. Default: False. Example: False.
        allowed_ip_ranges (list[str] | Unset): List of IP ranges that are allowed to authenticate with the token. Empty
            list denies access from everywhere. If unset, the default list will be the IP filters of the account. If no IP
            filters are defined for the account either, the default will be ["0.0.0.0/0", "::/0"], i.e. allow from any
            address. Example: ['0.0.0.0/0', '::/0'].
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    can_create_tokens: bool | Unset = False
    gui: bool | Unset = False
    allowed_ip_ranges: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        can_create_tokens = self.can_create_tokens

        gui = self.gui

        allowed_ip_ranges: list[str] | Unset = UNSET
        if not isinstance(self.allowed_ip_ranges, Unset):
            allowed_ip_ranges = self.allowed_ip_ranges

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if can_create_tokens is not UNSET:
            field_dict["can_create_tokens"] = can_create_tokens
        if gui is not UNSET:
            field_dict["gui"] = gui
        if allowed_ip_ranges is not UNSET:
            field_dict["allowed_ip_ranges"] = allowed_ip_ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = datetime.datetime.fromisoformat(_last_used_at)

        can_create_tokens = d.pop("can_create_tokens", UNSET)

        gui = d.pop("gui", UNSET)

        allowed_ip_ranges = cast(list[str], d.pop("allowed_ip_ranges", UNSET))

        account_tokens_get_token_response = cls(
            id=id,
            name=name,
            created_at=created_at,
            expires_at=expires_at,
            last_used_at=last_used_at,
            can_create_tokens=can_create_tokens,
            gui=gui,
            allowed_ip_ranges=allowed_ip_ranges,
        )

        return account_tokens_get_token_response
