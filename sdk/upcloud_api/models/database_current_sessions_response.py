from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_mysql_current_session_response import DatabaseMysqlCurrentSessionResponse
    from ..models.database_pg_current_session_response import DatabasePgCurrentSessionResponse
    from ..models.database_redis_valkey_current_session_response import DatabaseRedisValkeyCurrentSessionResponse


T = TypeVar("T", bound="DatabaseCurrentSessionsResponse")


@_attrs_define
class DatabaseCurrentSessionsResponse:
    """Schema for representing current sessions for various services

    Attributes:
        pg (list[DatabasePgCurrentSessionResponse] | Unset):
        mysql (list[DatabaseMysqlCurrentSessionResponse] | Unset):
        redis (list[DatabaseRedisValkeyCurrentSessionResponse] | Unset):
        valkey (list[DatabaseRedisValkeyCurrentSessionResponse] | Unset):
    """

    pg: list[DatabasePgCurrentSessionResponse] | Unset = UNSET
    mysql: list[DatabaseMysqlCurrentSessionResponse] | Unset = UNSET
    redis: list[DatabaseRedisValkeyCurrentSessionResponse] | Unset = UNSET
    valkey: list[DatabaseRedisValkeyCurrentSessionResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pg: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pg, Unset):
            pg = []
            for pg_item_data in self.pg:
                pg_item = pg_item_data.to_dict()
                pg.append(pg_item)

        mysql: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mysql, Unset):
            mysql = []
            for mysql_item_data in self.mysql:
                mysql_item = mysql_item_data.to_dict()
                mysql.append(mysql_item)

        redis: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redis, Unset):
            redis = []
            for redis_item_data in self.redis:
                redis_item = redis_item_data.to_dict()
                redis.append(redis_item)

        valkey: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.valkey, Unset):
            valkey = []
            for valkey_item_data in self.valkey:
                valkey_item = valkey_item_data.to_dict()
                valkey.append(valkey_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pg is not UNSET:
            field_dict["pg"] = pg
        if mysql is not UNSET:
            field_dict["mysql"] = mysql
        if redis is not UNSET:
            field_dict["redis"] = redis
        if valkey is not UNSET:
            field_dict["valkey"] = valkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_mysql_current_session_response import (
            DatabaseMysqlCurrentSessionResponse,  # noqa: PLC0415
        )
        from ..models.database_pg_current_session_response import DatabasePgCurrentSessionResponse  # noqa: PLC0415
        from ..models.database_redis_valkey_current_session_response import (
            DatabaseRedisValkeyCurrentSessionResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _pg = d.pop("pg", UNSET)
        pg: list[DatabasePgCurrentSessionResponse] | Unset = UNSET
        if _pg is not UNSET:
            pg = []
            for pg_item_data in _pg:
                pg_item = DatabasePgCurrentSessionResponse.from_dict(pg_item_data)

                pg.append(pg_item)

        _mysql = d.pop("mysql", UNSET)
        mysql: list[DatabaseMysqlCurrentSessionResponse] | Unset = UNSET
        if _mysql is not UNSET:
            mysql = []
            for mysql_item_data in _mysql:
                mysql_item = DatabaseMysqlCurrentSessionResponse.from_dict(mysql_item_data)

                mysql.append(mysql_item)

        _redis = d.pop("redis", UNSET)
        redis: list[DatabaseRedisValkeyCurrentSessionResponse] | Unset = UNSET
        if _redis is not UNSET:
            redis = []
            for redis_item_data in _redis:
                redis_item = DatabaseRedisValkeyCurrentSessionResponse.from_dict(redis_item_data)

                redis.append(redis_item)

        _valkey = d.pop("valkey", UNSET)
        valkey: list[DatabaseRedisValkeyCurrentSessionResponse] | Unset = UNSET
        if _valkey is not UNSET:
            valkey = []
            for valkey_item_data in _valkey:
                valkey_item = DatabaseRedisValkeyCurrentSessionResponse.from_dict(valkey_item_data)

                valkey.append(valkey_item)

        database_current_sessions_response = cls(
            pg=pg,
            mysql=mysql,
            redis=redis,
            valkey=valkey,
        )

        database_current_sessions_response.additional_properties = d
        return database_current_sessions_response

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
