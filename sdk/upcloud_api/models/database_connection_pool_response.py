from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseConnectionPoolResponse")


@_attrs_define
class DatabaseConnectionPoolResponse:
    """Schema for a connection pool response.

    Attributes:
        connection_uri (str | Unset): The connection URI of the connection pool. Example:
            postgresql://user:password@hostname:5432/dbname.
        database (str | Unset): The database name associated with the connection pool. Example: defaultdb.
        pool_mode (str | Unset): The mode of the connection pool. Example: session.
        pool_name (str | Unset): The name of the connection pool.
        pool_size (int | Unset): The size of the connection pool. Example: 10.
        username (str | Unset): The username for the connection pool Example: updamin.
    """

    connection_uri: str | Unset = UNSET
    database: str | Unset = UNSET
    pool_mode: str | Unset = UNSET
    pool_name: str | Unset = UNSET
    pool_size: int | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_uri = self.connection_uri

        database = self.database

        pool_mode = self.pool_mode

        pool_name = self.pool_name

        pool_size = self.pool_size

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_uri is not UNSET:
            field_dict["connection_uri"] = connection_uri
        if database is not UNSET:
            field_dict["database"] = database
        if pool_mode is not UNSET:
            field_dict["pool_mode"] = pool_mode
        if pool_name is not UNSET:
            field_dict["pool_name"] = pool_name
        if pool_size is not UNSET:
            field_dict["pool_size"] = pool_size
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_uri = d.pop("connection_uri", UNSET)

        database = d.pop("database", UNSET)

        pool_mode = d.pop("pool_mode", UNSET)

        pool_name = d.pop("pool_name", UNSET)

        pool_size = d.pop("pool_size", UNSET)

        username = d.pop("username", UNSET)

        database_connection_pool_response = cls(
            connection_uri=connection_uri,
            database=database,
            pool_mode=pool_mode,
            pool_name=pool_name,
            pool_size=pool_size,
            username=username,
        )

        database_connection_pool_response.additional_properties = d
        return database_connection_pool_response

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
