from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_legacy_boolean import ServerLegacyBoolean
from ..models.server_rebuild_server_rebuild_password_delivery import ServerRebuildServerRebuildPasswordDelivery
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_rebuild_server_rebuild_login_user import ServerRebuildServerRebuildLoginUser


T = TypeVar("T", bound="ServerRebuildServerRebuild")


@_attrs_define
class ServerRebuildServerRebuild:
    """
    Attributes:
        clone_source (UUID): UUID of the public template used for the new system disk.
        delete_detached_disk (ServerLegacyBoolean | Unset): Boolean value accepted by the legacy API
        detach_disk (UUID | Unset): UUID of the storage to detach before rebuilding.
        encrypted (ServerLegacyBoolean | Unset): Boolean value accepted by the legacy API
        login_user (ServerRebuildServerRebuildLoginUser | Unset):
        password_delivery (ServerRebuildServerRebuildPasswordDelivery | Unset): One-time password delivery method.
        storage_title (str | Unset): Title of the new system storage.
        user_data (str | Unset): User data supplied to cloud-init.
    """

    clone_source: UUID
    delete_detached_disk: ServerLegacyBoolean | Unset = UNSET
    detach_disk: UUID | Unset = UNSET
    encrypted: ServerLegacyBoolean | Unset = UNSET
    login_user: ServerRebuildServerRebuildLoginUser | Unset = UNSET
    password_delivery: ServerRebuildServerRebuildPasswordDelivery | Unset = UNSET
    storage_title: str | Unset = UNSET
    user_data: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        clone_source = str(self.clone_source)

        delete_detached_disk: str | Unset = UNSET
        if not isinstance(self.delete_detached_disk, Unset):
            delete_detached_disk = self.delete_detached_disk.value

        detach_disk: str | Unset = UNSET
        if not isinstance(self.detach_disk, Unset):
            detach_disk = str(self.detach_disk)

        encrypted: str | Unset = UNSET
        if not isinstance(self.encrypted, Unset):
            encrypted = self.encrypted.value

        login_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login_user, Unset):
            login_user = self.login_user.to_dict()

        password_delivery: str | Unset = UNSET
        if not isinstance(self.password_delivery, Unset):
            password_delivery = self.password_delivery.value

        storage_title = self.storage_title

        user_data = self.user_data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "clone_source": clone_source,
            }
        )
        if delete_detached_disk is not UNSET:
            field_dict["delete_detached_disk"] = delete_detached_disk
        if detach_disk is not UNSET:
            field_dict["detach_disk"] = detach_disk
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if login_user is not UNSET:
            field_dict["login_user"] = login_user
        if password_delivery is not UNSET:
            field_dict["password_delivery"] = password_delivery
        if storage_title is not UNSET:
            field_dict["storage_title"] = storage_title
        if user_data is not UNSET:
            field_dict["user_data"] = user_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_rebuild_server_rebuild_login_user import (
            ServerRebuildServerRebuildLoginUser,  # noqa: PLC0415
        )

        d = dict(src_dict)
        clone_source = UUID(d.pop("clone_source"))

        _delete_detached_disk = d.pop("delete_detached_disk", UNSET)
        delete_detached_disk: ServerLegacyBoolean | Unset
        if isinstance(_delete_detached_disk, Unset):
            delete_detached_disk = UNSET
        else:
            delete_detached_disk = ServerLegacyBoolean(_delete_detached_disk)

        _detach_disk = d.pop("detach_disk", UNSET)
        detach_disk: UUID | Unset
        if isinstance(_detach_disk, Unset):
            detach_disk = UNSET
        else:
            detach_disk = UUID(_detach_disk)

        _encrypted = d.pop("encrypted", UNSET)
        encrypted: ServerLegacyBoolean | Unset
        if isinstance(_encrypted, Unset):
            encrypted = UNSET
        else:
            encrypted = ServerLegacyBoolean(_encrypted)

        _login_user = d.pop("login_user", UNSET)
        login_user: ServerRebuildServerRebuildLoginUser | Unset
        if isinstance(_login_user, Unset):
            login_user = UNSET
        else:
            login_user = ServerRebuildServerRebuildLoginUser.from_dict(_login_user)

        _password_delivery = d.pop("password_delivery", UNSET)
        password_delivery: ServerRebuildServerRebuildPasswordDelivery | Unset
        if isinstance(_password_delivery, Unset):
            password_delivery = UNSET
        else:
            password_delivery = ServerRebuildServerRebuildPasswordDelivery(_password_delivery)

        storage_title = d.pop("storage_title", UNSET)

        user_data = d.pop("user_data", UNSET)

        server_rebuild_server_rebuild = cls(
            clone_source=clone_source,
            delete_detached_disk=delete_detached_disk,
            detach_disk=detach_disk,
            encrypted=encrypted,
            login_user=login_user,
            password_delivery=password_delivery,
            storage_title=storage_title,
            user_data=user_data,
        )

        return server_rebuild_server_rebuild
