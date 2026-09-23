from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2StaticWebsiteConfigCreate")


@_attrs_define
class ObjectStorage2StaticWebsiteConfigCreate:
    """Request body for creating a static website configuration. If domain is omitted, the primary static website domain is
    used.

        Attributes:
            bucket_name (str): Name of the S3/ECS bucket containing the website content. Only alphanumerics, dots, hyphens,
                and underscores are allowed. Example: my-website.
            domain_name (str | Unset): Custom domain to use for static website hosting. Must be a custom domain attached to
                the service. If omitted, the primary static website domain is used. Example: www.example.com.
            bucket_prefix (str | Unset): Optional prefix/subfolder within the bucket. Only alphanumerics, slashes, dots,
                hyphens, and underscores are allowed. Default: ''. Example: v2/.
            index_document (str | Unset): Default document for directories. Only alphanumerics, slashes, dots, hyphens, and
                underscores are allowed. Default: 'index.html'. Example: index.html.
            spa_mode (bool | None | Unset): Enable Single Page Application (SPA) mode. When enabled, all non-file routes
                serve the index document, allowing client-side routing to handle the URL. Essential for React, Vue, Next.js, and
                similar frameworks. Default: False. Example: False.
            enabled (bool | Unset): Whether the static website configuration should be active. Defaults to true if not
                specified. Default: True. Example: True.
            error_pages (list[Any] | Unset): Custom error page configurations for specific HTTP status codes or ranges
                Example: [{'status_code': 404, 'error_document': 'errors/404.html'}, {'status_range': {'start': 500, 'end':
                599}, 'error_document': 'errors/5xx.html'}].
    """

    bucket_name: str
    domain_name: str | Unset = UNSET
    bucket_prefix: str | Unset = ""
    index_document: str | Unset = "index.html"
    spa_mode: bool | None | Unset = False
    enabled: bool | Unset = True
    error_pages: list[Any] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bucket_name = self.bucket_name

        domain_name = self.domain_name

        bucket_prefix = self.bucket_prefix

        index_document = self.index_document

        spa_mode: bool | None | Unset
        if isinstance(self.spa_mode, Unset):
            spa_mode = UNSET
        else:
            spa_mode = self.spa_mode

        enabled = self.enabled

        error_pages: list[Any] | Unset = UNSET
        if not isinstance(self.error_pages, Unset):
            error_pages = []
            for error_pages_item_data in self.error_pages:
                error_pages_item: Any
                error_pages_item = error_pages_item_data
                error_pages.append(error_pages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bucket_name": bucket_name,
            }
        )
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if bucket_prefix is not UNSET:
            field_dict["bucket_prefix"] = bucket_prefix
        if index_document is not UNSET:
            field_dict["index_document"] = index_document
        if spa_mode is not UNSET:
            field_dict["spa_mode"] = spa_mode
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if error_pages is not UNSET:
            field_dict["error_pages"] = error_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_name = d.pop("bucket_name")

        domain_name = d.pop("domain_name", UNSET)

        bucket_prefix = d.pop("bucket_prefix", UNSET)

        index_document = d.pop("index_document", UNSET)

        def _parse_spa_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        spa_mode = _parse_spa_mode(d.pop("spa_mode", UNSET))

        enabled = d.pop("enabled", UNSET)

        _error_pages = d.pop("error_pages", UNSET)
        error_pages: list[Any] | Unset = UNSET
        if _error_pages is not UNSET:
            error_pages = []
            for error_pages_item_data in _error_pages:

                def _parse_error_pages_item(data: object) -> Any:
                    return cast(Any, data)

                error_pages_item = _parse_error_pages_item(error_pages_item_data)

                error_pages.append(error_pages_item)

        object_storage_2_static_website_config_create = cls(
            bucket_name=bucket_name,
            domain_name=domain_name,
            bucket_prefix=bucket_prefix,
            index_document=index_document,
            spa_mode=spa_mode,
            enabled=enabled,
            error_pages=error_pages,
        )

        return object_storage_2_static_website_config_create
