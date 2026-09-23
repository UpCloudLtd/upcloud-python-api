from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_connection_pool_create_pool_mode import DatabaseConnectionPoolCreatePoolMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseConnectionPoolCreate")


@_attrs_define
class DatabaseConnectionPoolCreate:
    """Schema for creating a connection pool.

    Attributes:
        database (str): Database
        pool_mode (DatabaseConnectionPoolCreatePoolMode): Connection Pool mode
        pool_name (str): Connection Pool name
        pool_size (int): Connection Pool size
        username (str | Unset): Connection Pool username
    """

    database: str
    pool_mode: DatabaseConnectionPoolCreatePoolMode
    pool_name: str
    pool_size: int
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        database = self.database

        pool_mode = self.pool_mode.value

        pool_name = self.pool_name

        pool_size = self.pool_size

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "database": database,
                "pool_mode": pool_mode,
                "pool_name": pool_name,
                "pool_size": pool_size,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database = d.pop("database")

        pool_mode = DatabaseConnectionPoolCreatePoolMode(d.pop("pool_mode"))

        pool_name = d.pop("pool_name")

        pool_size = d.pop("pool_size")

        username = d.pop("username", UNSET)

        database_connection_pool_create = cls(
            database=database,
            pool_mode=pool_mode,
            pool_name=pool_name,
            pool_size=pool_size,
            username=username,
        )

        return database_connection_pool_create
