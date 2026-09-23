from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_query_statistics_mysql_response import DatabaseQueryStatisticsMysqlResponse
    from ..models.database_query_statistics_pg_response import DatabaseQueryStatisticsPgResponse


T = TypeVar("T", bound="DatabaseQueryStatisticsResponse")


@_attrs_define
class DatabaseQueryStatisticsResponse:
    """Schema for query statistics response.

    Attributes:
        mysql (list[DatabaseQueryStatisticsMysqlResponse] | Unset):
        pg (list[DatabaseQueryStatisticsPgResponse] | Unset):
    """

    mysql: list[DatabaseQueryStatisticsMysqlResponse] | Unset = UNSET
    pg: list[DatabaseQueryStatisticsPgResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mysql: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mysql, Unset):
            mysql = []
            for mysql_item_data in self.mysql:
                mysql_item = mysql_item_data.to_dict()
                mysql.append(mysql_item)

        pg: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pg, Unset):
            pg = []
            for pg_item_data in self.pg:
                pg_item = pg_item_data.to_dict()
                pg.append(pg_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mysql is not UNSET:
            field_dict["mysql"] = mysql
        if pg is not UNSET:
            field_dict["pg"] = pg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_query_statistics_mysql_response import (
            DatabaseQueryStatisticsMysqlResponse,  # noqa: PLC0415
        )
        from ..models.database_query_statistics_pg_response import DatabaseQueryStatisticsPgResponse  # noqa: PLC0415

        d = dict(src_dict)
        _mysql = d.pop("mysql", UNSET)
        mysql: list[DatabaseQueryStatisticsMysqlResponse] | Unset = UNSET
        if _mysql is not UNSET:
            mysql = []
            for mysql_item_data in _mysql:
                mysql_item = DatabaseQueryStatisticsMysqlResponse.from_dict(mysql_item_data)

                mysql.append(mysql_item)

        _pg = d.pop("pg", UNSET)
        pg: list[DatabaseQueryStatisticsPgResponse] | Unset = UNSET
        if _pg is not UNSET:
            pg = []
            for pg_item_data in _pg:
                pg_item = DatabaseQueryStatisticsPgResponse.from_dict(pg_item_data)

                pg.append(pg_item)

        database_query_statistics_response = cls(
            mysql=mysql,
            pg=pg,
        )

        database_query_statistics_response.additional_properties = d
        return database_query_statistics_response

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
