from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_error_404_error import ServerError404Error


T = TypeVar("T", bound="ServerError404")


@_attrs_define
class ServerError404:
    """Schema for Cloud Server 404 error responses.

    Example:
        {'error': {'code': 'SERVER_NOT_FOUND', 'message': 'The server 007bf7bd-e3cf-4a10-bf01-4251dc7f3b65 does not
            exist.'}}

    Attributes:
        error (ServerError404Error):
    """

    error: ServerError404Error
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_error_404_error import ServerError404Error  # noqa: PLC0415

        d = dict(src_dict)
        error = ServerError404Error.from_dict(d.pop("error"))

        server_error_404 = cls(
            error=error,
        )

        server_error_404.additional_properties = d
        return server_error_404

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
