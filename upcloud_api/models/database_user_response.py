from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_open_search_access_control_response import DatabaseOpenSearchAccessControlResponse
    from ..models.database_pg_access_control_response import DatabasePgAccessControlResponse
    from ..models.database_redis_access_control_response import DatabaseRedisAccessControlResponse
    from ..models.database_valkey_access_control_response import DatabaseValkeyAccessControlResponse


T = TypeVar("T", bound="DatabaseUserResponse")


@_attrs_define
class DatabaseUserResponse:
    """Schema for a user response.

    Attributes:
        username (str | Unset): The username of the user. Example: admin.
        password (str | Unset): The password of the user. Example: my-password.
        authentication (str | Unset): The authentication method used by the user. Example: caching_sha2_password.
        type_ (str | Unset): The type of the user. Example: admin.
        pg_access_control (DatabasePgAccessControlResponse | Unset): Schema for PostgreSQL access control response.
        redis_access_control (DatabaseRedisAccessControlResponse | Unset): Schema for Redis access control response.
        valkey_access_control (DatabaseValkeyAccessControlResponse | Unset): Schema for Valkey user access control
            response
        opensearch_access_control (DatabaseOpenSearchAccessControlResponse | Unset): Schema for OpenSearch access
            control response.
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    authentication: str | Unset = UNSET
    type_: str | Unset = UNSET
    pg_access_control: DatabasePgAccessControlResponse | Unset = UNSET
    redis_access_control: DatabaseRedisAccessControlResponse | Unset = UNSET
    valkey_access_control: DatabaseValkeyAccessControlResponse | Unset = UNSET
    opensearch_access_control: DatabaseOpenSearchAccessControlResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        authentication = self.authentication

        type_ = self.type_

        pg_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pg_access_control, Unset):
            pg_access_control = self.pg_access_control.to_dict()

        redis_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redis_access_control, Unset):
            redis_access_control = self.redis_access_control.to_dict()

        valkey_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valkey_access_control, Unset):
            valkey_access_control = self.valkey_access_control.to_dict()

        opensearch_access_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.opensearch_access_control, Unset):
            opensearch_access_control = self.opensearch_access_control.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if type_ is not UNSET:
            field_dict["type"] = type_
        if pg_access_control is not UNSET:
            field_dict["pg_access_control"] = pg_access_control
        if redis_access_control is not UNSET:
            field_dict["redis_access_control"] = redis_access_control
        if valkey_access_control is not UNSET:
            field_dict["valkey_access_control"] = valkey_access_control
        if opensearch_access_control is not UNSET:
            field_dict["opensearch_access_control"] = opensearch_access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_open_search_access_control_response import (
            DatabaseOpenSearchAccessControlResponse,  # noqa: PLC0415
        )
        from ..models.database_pg_access_control_response import DatabasePgAccessControlResponse  # noqa: PLC0415
        from ..models.database_redis_access_control_response import DatabaseRedisAccessControlResponse  # noqa: PLC0415
        from ..models.database_valkey_access_control_response import (
            DatabaseValkeyAccessControlResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        authentication = d.pop("authentication", UNSET)

        type_ = d.pop("type", UNSET)

        _pg_access_control = d.pop("pg_access_control", UNSET)
        pg_access_control: DatabasePgAccessControlResponse | Unset
        if isinstance(_pg_access_control, Unset):
            pg_access_control = UNSET
        else:
            pg_access_control = DatabasePgAccessControlResponse.from_dict(_pg_access_control)

        _redis_access_control = d.pop("redis_access_control", UNSET)
        redis_access_control: DatabaseRedisAccessControlResponse | Unset
        if isinstance(_redis_access_control, Unset):
            redis_access_control = UNSET
        else:
            redis_access_control = DatabaseRedisAccessControlResponse.from_dict(_redis_access_control)

        _valkey_access_control = d.pop("valkey_access_control", UNSET)
        valkey_access_control: DatabaseValkeyAccessControlResponse | Unset
        if isinstance(_valkey_access_control, Unset):
            valkey_access_control = UNSET
        else:
            valkey_access_control = DatabaseValkeyAccessControlResponse.from_dict(_valkey_access_control)

        _opensearch_access_control = d.pop("opensearch_access_control", UNSET)
        opensearch_access_control: DatabaseOpenSearchAccessControlResponse | Unset
        if isinstance(_opensearch_access_control, Unset):
            opensearch_access_control = UNSET
        else:
            opensearch_access_control = DatabaseOpenSearchAccessControlResponse.from_dict(_opensearch_access_control)

        database_user_response = cls(
            username=username,
            password=password,
            authentication=authentication,
            type_=type_,
            pg_access_control=pg_access_control,
            redis_access_control=redis_access_control,
            valkey_access_control=valkey_access_control,
            opensearch_access_control=opensearch_access_control,
        )

        database_user_response.additional_properties = d
        return database_user_response

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
