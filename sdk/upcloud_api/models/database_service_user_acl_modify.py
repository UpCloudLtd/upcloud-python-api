from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_user_acl_modify_opensearch_access_control import (
        DatabaseServiceUserAclModifyOpensearchAccessControl,
    )
    from ..models.database_service_user_acl_modify_pg_access_control import DatabaseServiceUserAclModifyPgAccessControl
    from ..models.database_service_user_acl_modify_redis_access_control import (
        DatabaseServiceUserAclModifyRedisAccessControl,
    )
    from ..models.database_service_user_acl_modify_valkey_access_control import (
        DatabaseServiceUserAclModifyValkeyAccessControl,
    )


T = TypeVar("T", bound="DatabaseServiceUserAclModify")


@_attrs_define
class DatabaseServiceUserAclModify:
    """Schema for modifying user access control lists (ACL) for various services

    Attributes:
        redis_access_control (DatabaseServiceUserAclModifyRedisAccessControl | Unset): Redis ACL modification schema
        pg_access_control (DatabaseServiceUserAclModifyPgAccessControl | Unset): PostgreSQL replication permission
            modification schema
        opensearch_access_control (DatabaseServiceUserAclModifyOpensearchAccessControl | Unset): OpenSearch index
            permission modification schema
        valkey_access_control (DatabaseServiceUserAclModifyValkeyAccessControl | Unset): Valkey ACL modification schema
    """

    redis_access_control: DatabaseServiceUserAclModifyRedisAccessControl | Unset = UNSET
    pg_access_control: DatabaseServiceUserAclModifyPgAccessControl | Unset = UNSET
    opensearch_access_control: DatabaseServiceUserAclModifyOpensearchAccessControl | Unset = UNSET
    valkey_access_control: DatabaseServiceUserAclModifyValkeyAccessControl | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        redis_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redis_access_control, Unset):
            redis_access_control = self.redis_access_control.to_dict()

        pg_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pg_access_control, Unset):
            pg_access_control = self.pg_access_control.to_dict()

        opensearch_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.opensearch_access_control, Unset):
            opensearch_access_control = self.opensearch_access_control.to_dict()

        valkey_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valkey_access_control, Unset):
            valkey_access_control = self.valkey_access_control.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if redis_access_control is not UNSET:
            field_dict["redis_access_control"] = redis_access_control
        if pg_access_control is not UNSET:
            field_dict["pg_access_control"] = pg_access_control
        if opensearch_access_control is not UNSET:
            field_dict["opensearch_access_control"] = opensearch_access_control
        if valkey_access_control is not UNSET:
            field_dict["valkey_access_control"] = valkey_access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_user_acl_modify_opensearch_access_control import (
            DatabaseServiceUserAclModifyOpensearchAccessControl,  # noqa: PLC0415
        )
        from ..models.database_service_user_acl_modify_pg_access_control import (
            DatabaseServiceUserAclModifyPgAccessControl,  # noqa: PLC0415
        )
        from ..models.database_service_user_acl_modify_redis_access_control import (
            DatabaseServiceUserAclModifyRedisAccessControl,  # noqa: PLC0415
        )
        from ..models.database_service_user_acl_modify_valkey_access_control import (
            DatabaseServiceUserAclModifyValkeyAccessControl,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _redis_access_control = d.pop("redis_access_control", UNSET)
        redis_access_control: DatabaseServiceUserAclModifyRedisAccessControl | Unset
        if isinstance(_redis_access_control, Unset):
            redis_access_control = UNSET
        else:
            redis_access_control = DatabaseServiceUserAclModifyRedisAccessControl.from_dict(_redis_access_control)

        _pg_access_control = d.pop("pg_access_control", UNSET)
        pg_access_control: DatabaseServiceUserAclModifyPgAccessControl | Unset
        if isinstance(_pg_access_control, Unset):
            pg_access_control = UNSET
        else:
            pg_access_control = DatabaseServiceUserAclModifyPgAccessControl.from_dict(_pg_access_control)

        _opensearch_access_control = d.pop("opensearch_access_control", UNSET)
        opensearch_access_control: DatabaseServiceUserAclModifyOpensearchAccessControl | Unset
        if isinstance(_opensearch_access_control, Unset):
            opensearch_access_control = UNSET
        else:
            opensearch_access_control = DatabaseServiceUserAclModifyOpensearchAccessControl.from_dict(
                _opensearch_access_control
            )

        _valkey_access_control = d.pop("valkey_access_control", UNSET)
        valkey_access_control: DatabaseServiceUserAclModifyValkeyAccessControl | Unset
        if isinstance(_valkey_access_control, Unset):
            valkey_access_control = UNSET
        else:
            valkey_access_control = DatabaseServiceUserAclModifyValkeyAccessControl.from_dict(_valkey_access_control)

        database_service_user_acl_modify = cls(
            redis_access_control=redis_access_control,
            pg_access_control=pg_access_control,
            opensearch_access_control=opensearch_access_control,
            valkey_access_control=valkey_access_control,
        )

        return database_service_user_acl_modify
