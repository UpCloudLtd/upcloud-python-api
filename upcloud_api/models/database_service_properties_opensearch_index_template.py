from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchIndexTemplate")


@_attrs_define
class DatabaseServicePropertiesOpensearchIndexTemplate:
    """
    Attributes:
        mapping_nested_objects_limit (int | None | Unset): The maximum number of nested JSON objects that a single
            document can contain across all nested types. This limit helps to prevent out of memory errors when a document
            contains too many nested objects. Default is 10000. Deprecated, use an index template instead.
        number_of_replicas (int | None | Unset): The number of replicas each primary shard has. Deprecated, use an index
            template instead.
        number_of_shards (int | None | Unset): The number of primary shards that an index should have. Deprecated, use
            an index template instead.
    """

    mapping_nested_objects_limit: int | None | Unset = UNSET
    number_of_replicas: int | None | Unset = UNSET
    number_of_shards: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mapping_nested_objects_limit: int | None | Unset
        if isinstance(self.mapping_nested_objects_limit, Unset):
            mapping_nested_objects_limit = UNSET
        else:
            mapping_nested_objects_limit = self.mapping_nested_objects_limit

        number_of_replicas: int | None | Unset
        if isinstance(self.number_of_replicas, Unset):
            number_of_replicas = UNSET
        else:
            number_of_replicas = self.number_of_replicas

        number_of_shards: int | None | Unset
        if isinstance(self.number_of_shards, Unset):
            number_of_shards = UNSET
        else:
            number_of_shards = self.number_of_shards

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mapping_nested_objects_limit is not UNSET:
            field_dict["mapping_nested_objects_limit"] = mapping_nested_objects_limit
        if number_of_replicas is not UNSET:
            field_dict["number_of_replicas"] = number_of_replicas
        if number_of_shards is not UNSET:
            field_dict["number_of_shards"] = number_of_shards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_mapping_nested_objects_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mapping_nested_objects_limit = _parse_mapping_nested_objects_limit(d.pop("mapping_nested_objects_limit", UNSET))

        def _parse_number_of_replicas(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_replicas = _parse_number_of_replicas(d.pop("number_of_replicas", UNSET))

        def _parse_number_of_shards(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_shards = _parse_number_of_shards(d.pop("number_of_shards", UNSET))

        database_service_properties_opensearch_index_template = cls(
            mapping_nested_objects_limit=mapping_nested_objects_limit,
            number_of_replicas=number_of_replicas,
            number_of_shards=number_of_shards,
        )

        return database_service_properties_opensearch_index_template
