from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2StaticWebsiteConfig")


@_attrs_define
class ObjectStorage2StaticWebsiteConfig:
    """Static website hosting configuration for a specific domain.

    Attributes:
        domain_name (str): The domain this configuration applies to Example: abc123-static.upbucket.example.com.
        bucket_name (str): Name of the S3/ECS bucket containing the website content. Only alphanumerics, dots, hyphens,
            and underscores are allowed. Example: my-website.
        bucket_prefix (str): Optional prefix/subfolder within the bucket. Only alphanumerics, slashes, dots, hyphens,
            and underscores are allowed. Default: ''. Example: v2/.
        index_document (str): Default document for directories. Only alphanumerics, slashes, dots, hyphens, and
            underscores are allowed. Default: 'index.html'. Example: index.html.
        error_pages (list[Any]): Custom error page configurations for specific HTTP status codes or ranges Example:
            [{'status_code': 403, 'error_document': 'errors/403.html'}, {'status_code': 404, 'error_document':
            'errors/404.html'}, {'status_range': {'start': 400, 'end': 499}, 'error_document': 'errors/4xx.html'}].
        enabled (bool): Whether the static website configuration is currently active Example: True.
        created_at (datetime.datetime): Timestamp when this configuration was created Example: 2025-10-28T10:00:00Z.
        updated_at (datetime.datetime): Timestamp when this configuration was last updated Example:
            2025-10-28T12:00:00Z.
        spa_mode (bool | Unset): Enable Single Page Application (SPA) mode. When enabled, all non-file routes serve the
            index document, allowing client-side routing to handle the URL. Essential for React, Vue, Next.js, and similar
            frameworks. Default: False. Example: True.
    """

    domain_name: str
    bucket_name: str
    error_pages: list[Any]
    enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    bucket_prefix: str = ""
    index_document: str = "index.html"
    spa_mode: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_name = self.domain_name

        bucket_name = self.bucket_name

        bucket_prefix = self.bucket_prefix

        index_document = self.index_document

        error_pages = []
        for error_pages_item_data in self.error_pages:
            error_pages_item: Any
            error_pages_item = error_pages_item_data
            error_pages.append(error_pages_item)

        enabled = self.enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        spa_mode = self.spa_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_name": domain_name,
                "bucket_name": bucket_name,
                "bucket_prefix": bucket_prefix,
                "index_document": index_document,
                "error_pages": error_pages,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if spa_mode is not UNSET:
            field_dict["spa_mode"] = spa_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_name = d.pop("domain_name")

        bucket_name = d.pop("bucket_name")

        bucket_prefix = d.pop("bucket_prefix")

        index_document = d.pop("index_document")

        error_pages = []
        _error_pages = d.pop("error_pages")
        for error_pages_item_data in _error_pages:

            def _parse_error_pages_item(data: object) -> Any:
                return cast(Any, data)

            error_pages_item = _parse_error_pages_item(error_pages_item_data)

            error_pages.append(error_pages_item)

        enabled = d.pop("enabled")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        spa_mode = d.pop("spa_mode", UNSET)

        object_storage_2_static_website_config = cls(
            domain_name=domain_name,
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            index_document=index_document,
            error_pages=error_pages,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            spa_mode=spa_mode,
        )

        object_storage_2_static_website_config.additional_properties = d
        return object_storage_2_static_website_config

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
