from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_connection_pool_modify_pool_mode import DatabaseConnectionPoolModifyPoolMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseConnectionPoolModify")


@_attrs_define
class DatabaseConnectionPoolModify:
    """Schema for modifying a connection pool.

    Attributes:
        database (str | Unset): Database
        pool_mode (DatabaseConnectionPoolModifyPoolMode | Unset): Connection Pool mode
        pool_size (int | Unset): Connection Pool size
        username (None | str | Unset): Connection Pool username
    """

    database: str | Unset = UNSET
    pool_mode: DatabaseConnectionPoolModifyPoolMode | Unset = UNSET
    pool_size: int | Unset = UNSET
    username: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database = self.database

        pool_mode: str | Unset = UNSET
        if not isinstance(self.pool_mode, Unset):
            pool_mode = self.pool_mode.value

        pool_size = self.pool_size

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if database is not UNSET:
            field_dict["database"] = database
        if pool_mode is not UNSET:
            field_dict["pool_mode"] = pool_mode
        if pool_size is not UNSET:
            field_dict["pool_size"] = pool_size
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database = d.pop("database", UNSET)

        _pool_mode = d.pop("pool_mode", UNSET)
        pool_mode: DatabaseConnectionPoolModifyPoolMode | Unset
        if isinstance(_pool_mode, Unset):
            pool_mode = UNSET
        else:
            pool_mode = DatabaseConnectionPoolModifyPoolMode(_pool_mode)

        pool_size = d.pop("pool_size", UNSET)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        database_connection_pool_modify = cls(
            database=database,
            pool_mode=pool_mode,
            pool_size=pool_size,
            username=username,
        )

        return database_connection_pool_modify
