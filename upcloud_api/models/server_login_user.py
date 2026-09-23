from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_login_user_ssh_keys import ServerLoginUserSshKeys


T = TypeVar("T", bound="ServerLoginUser")


@_attrs_define
class ServerLoginUser:
    """Login user configuration for Cloud Server creation

    Example:
        {'username': 'upclouduser'}

    Attributes:
        create_password (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        ssh_keys (ServerLoginUserSshKeys | Unset):
        username (str | Unset): Username for logging in to the Cloud Server
    """

    create_password: ServerBooleanYesno | Unset = UNSET
    ssh_keys: ServerLoginUserSshKeys | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        create_password: str | Unset = UNSET
        if not isinstance(self.create_password, Unset):
            create_password = self.create_password.value

        ssh_keys: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = self.ssh_keys.to_dict()

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if create_password is not UNSET:
            field_dict["create_password"] = create_password
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_login_user_ssh_keys import ServerLoginUserSshKeys  # noqa: PLC0415

        d = dict(src_dict)
        _create_password = d.pop("create_password", UNSET)
        create_password: ServerBooleanYesno | Unset
        if isinstance(_create_password, Unset):
            create_password = UNSET
        else:
            create_password = ServerBooleanYesno(_create_password)

        _ssh_keys = d.pop("ssh_keys", UNSET)
        ssh_keys: ServerLoginUserSshKeys | Unset
        if isinstance(_ssh_keys, Unset):
            ssh_keys = UNSET
        else:
            ssh_keys = ServerLoginUserSshKeys.from_dict(_ssh_keys)

        username = d.pop("username", UNSET)

        server_login_user = cls(
            create_password=create_password,
            ssh_keys=ssh_keys,
            username=username,
        )

        return server_login_user
