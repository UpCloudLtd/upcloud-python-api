from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_content_types import LoadBalancerContentTypes

T = TypeVar("T", bound="LoadBalancerActionHttpReturnCreate")


@_attrs_define
class LoadBalancerActionHttpReturnCreate:
    """Forwarding rule HTTP Return action

    Attributes:
        status (int): HTTP Status code Example: 200.
        content_type (LoadBalancerContentTypes): Content types
        payload (str): Response body content to return to the client.
    """

    status: int
    content_type: LoadBalancerContentTypes
    payload: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        content_type = self.content_type.value

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

        content_type = LoadBalancerContentTypes(d.pop("content_type"))

        payload = d.pop("payload")

        load_balancer_action_http_return_create = cls(
            status=status,
            content_type=content_type,
            payload=payload,
        )

        return load_balancer_action_http_return_create
