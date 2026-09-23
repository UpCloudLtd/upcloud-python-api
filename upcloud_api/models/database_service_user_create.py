from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_user_create_opensearch_access_control import (
        DatabaseServiceUserCreateOpensearchAccessControl,
    )
    from ..models.database_service_user_create_pg_access_control import DatabaseServiceUserCreatePgAccessControl
    from ..models.database_service_user_create_redis_access_control import DatabaseServiceUserCreateRedisAccessControl
    from ..models.database_service_user_create_valkey_access_control import DatabaseServiceUserCreateValkeyAccessControl


T = TypeVar("T", bound="DatabaseServiceUserCreate")


@_attrs_define
class DatabaseServiceUserCreate:
    """Schema for creating a service user with access control settings

    Attributes:
        username (str): The username of the service user
        password (str | Unset): The password of the service user
        authentication (str | Unset): The authentication method for the service user
        redis_access_control (DatabaseServiceUserCreateRedisAccessControl | Unset): Redis access control settings
        pg_access_control (DatabaseServiceUserCreatePgAccessControl | Unset): PostgreSQL access control settings
        opensearch_access_control (DatabaseServiceUserCreateOpensearchAccessControl | Unset): OpenSearch access control
            settings
        valkey_access_control (DatabaseServiceUserCreateValkeyAccessControl | Unset): Valkey access control settings
    """

    username: str
    password: str | Unset = UNSET
    authentication: str | Unset = UNSET
    redis_access_control: DatabaseServiceUserCreateRedisAccessControl | Unset = UNSET
    pg_access_control: DatabaseServiceUserCreatePgAccessControl | Unset = UNSET
    opensearch_access_control: DatabaseServiceUserCreateOpensearchAccessControl | Unset = UNSET
    valkey_access_control: DatabaseServiceUserCreateValkeyAccessControl | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        authentication = self.authentication

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

        field_dict.update(
            {
                "username": username,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
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
        from ..models.database_service_user_create_opensearch_access_control import (
            DatabaseServiceUserCreateOpensearchAccessControl,  # noqa: PLC0415
        )
        from ..models.database_service_user_create_pg_access_control import (
            DatabaseServiceUserCreatePgAccessControl,  # noqa: PLC0415
        )
        from ..models.database_service_user_create_redis_access_control import (
            DatabaseServiceUserCreateRedisAccessControl,  # noqa: PLC0415
        )
        from ..models.database_service_user_create_valkey_access_control import (
            DatabaseServiceUserCreateValkeyAccessControl,  # noqa: PLC0415
        )

        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password", UNSET)

        authentication = d.pop("authentication", UNSET)

        _redis_access_control = d.pop("redis_access_control", UNSET)
        redis_access_control: DatabaseServiceUserCreateRedisAccessControl | Unset
        if isinstance(_redis_access_control, Unset):
            redis_access_control = UNSET
        else:
            redis_access_control = DatabaseServiceUserCreateRedisAccessControl.from_dict(_redis_access_control)

        _pg_access_control = d.pop("pg_access_control", UNSET)
        pg_access_control: DatabaseServiceUserCreatePgAccessControl | Unset
        if isinstance(_pg_access_control, Unset):
            pg_access_control = UNSET
        else:
            pg_access_control = DatabaseServiceUserCreatePgAccessControl.from_dict(_pg_access_control)

        _opensearch_access_control = d.pop("opensearch_access_control", UNSET)
        opensearch_access_control: DatabaseServiceUserCreateOpensearchAccessControl | Unset
        if isinstance(_opensearch_access_control, Unset):
            opensearch_access_control = UNSET
        else:
            opensearch_access_control = DatabaseServiceUserCreateOpensearchAccessControl.from_dict(
                _opensearch_access_control
            )

        _valkey_access_control = d.pop("valkey_access_control", UNSET)
        valkey_access_control: DatabaseServiceUserCreateValkeyAccessControl | Unset
        if isinstance(_valkey_access_control, Unset):
            valkey_access_control = UNSET
        else:
            valkey_access_control = DatabaseServiceUserCreateValkeyAccessControl.from_dict(_valkey_access_control)

        database_service_user_create = cls(
            username=username,
            password=password,
            authentication=authentication,
            redis_access_control=redis_access_control,
            pg_access_control=pg_access_control,
            opensearch_access_control=opensearch_access_control,
            valkey_access_control=valkey_access_control,
        )

        return database_service_user_create
