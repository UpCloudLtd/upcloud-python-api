from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionHttpReturnResponse")


@_attrs_define
class LoadBalancerActionHttpReturnResponse:
    """Defines a custom HTTP response returned to the client when a rule matches. Used when the action type is
    'http_return'.

        Example:
            {'status': 403, 'content_type': 'text/plain', 'payload': 'QWNjZXNzIERlbmllZAo='}

        Attributes:
            status (int): HTTP status code to return. Example: 403.
            content_type (str): MIME type of the response body. Example: text/plain.
            payload (str): Base64-encoded payload returned as the response body. Example: QWNjZXNzIERlbmllZAo=.
    """

    status: int
    content_type: str
    payload: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        content_type = self.content_type

        payload = self.payload

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "content_type": content_type,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        content_type = d.pop("content_type")

        payload = d.pop("payload")

        load_balancer_action_http_return_response = cls(
            status=status,
            content_type=content_type,
            payload=payload,
        )

        return load_balancer_action_http_return_response
