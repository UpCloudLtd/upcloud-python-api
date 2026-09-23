from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServiceComponentResponse")


@_attrs_define
class DatabaseServiceComponentResponse:
    """Schema for a service component response.

    Attributes:
        component (str | Unset): The name of the service component. Example: pg.
        host (str | Unset): The hostname or IP address of the service component. Example: pg-2x2xcpu-4gb-50gb-de-
            fra1-example-prefix-project.db.upclouddatabases.com.
        port (int | Unset): The port number of the service component. Example: 1150.
        route (str | Unset): The route to access the service component. Example: dynamic.
        usage (str | Unset): The usage of the service component. Example: replica.
        ssl (bool | Unset): Indicates if SSL is enabled for the service component. Example: True.
    """

    component: str | Unset = UNSET
    host: str | Unset = UNSET
    port: int | Unset = UNSET
    route: str | Unset = UNSET
    usage: str | Unset = UNSET
    ssl: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        host = self.host

        port = self.port

        route = self.route

        usage = self.usage

        ssl = self.ssl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if route is not UNSET:
            field_dict["route"] = route
        if usage is not UNSET:
            field_dict["usage"] = usage
        if ssl is not UNSET:
            field_dict["ssl"] = ssl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component = d.pop("component", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        route = d.pop("route", UNSET)

        usage = d.pop("usage", UNSET)

        ssl = d.pop("ssl", UNSET)

        database_service_component_response = cls(
            component=component,
            host=host,
            port=port,
            route=route,
            usage=usage,
            ssl=ssl,
        )

        database_service_component_response.additional_properties = d
        return database_service_component_response

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
