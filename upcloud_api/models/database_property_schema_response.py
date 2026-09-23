from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_property_schema_response_default import DatabasePropertySchemaResponseDefault
    from ..models.database_property_schema_response_dependencies import DatabasePropertySchemaResponseDependencies
    from ..models.database_property_schema_response_example import DatabasePropertySchemaResponseExample
    from ..models.database_property_schema_response_maximum_item import DatabasePropertySchemaResponseMaximumItem
    from ..models.database_property_schema_response_minimum_item import DatabasePropertySchemaResponseMinimumItem
    from ..models.database_property_schema_response_properties import DatabasePropertySchemaResponseProperties


T = TypeVar("T", bound="DatabasePropertySchemaResponse")


@_attrs_define
class DatabasePropertySchemaResponse:
    """Schema definition for a single property

    Attributes:
        schema (str | Unset): JSON Schema URI Example: https://json-schema.org/draft/2020-12/schema.
        id (str | Unset): Schema identifier Example: sample-id.
        create_only (bool | Unset): Whether the property can only be set during creation Example: False.
        default (DatabasePropertySchemaResponseDefault | Unset): Any valid JSON value is allowed here Example: {'foo':
            'bar'}.
        example (DatabasePropertySchemaResponseExample | Unset): Any valid JSON value is allowed here Example: {'foo':
            'bar'}.
        max_length (int | Unset): Maximum length for the property schema Example: 255.
        min_length (int | Unset): Minimum length for the property schema Example: 255.
        pattern (str | Unset): Allowed patterns for the property Example: ^[a-zA-Z0-9_./:-]+(\\[[^\\]]+\\])?$.
        title (str | Unset): Human-readable title for the property Example: Sample Property.
        type_ (str | Unset): Data type of the property Example: any string.
        user_error (str | Unset): User-friendly error message Example: Invalid input provided.
        items (DatabasePropertySchemaResponse | Unset): Schema definition for a single property
        properties (DatabasePropertySchemaResponseProperties | Unset): Properties for object type
        dependencies (DatabasePropertySchemaResponseDependencies | Unset): Property dependency collection Example:
            {'required': ['host', 'port']}.
        required (list[str] | Unset): List of required properties Example: ['host', 'port'].
        max_items (int | Unset): Maximum number of items for arrays Example: 10.
        description (str | Unset): Description of the property Example: This is a sample property used for demonstration
            purposes..
        minimum (list[DatabasePropertySchemaResponseMinimumItem] | Unset): Minimum values for numeric properties
        maximum (list[DatabasePropertySchemaResponseMaximumItem] | Unset): Maximum values for numeric properties
            Example: [1, 0].
        enum (list[Any] | Unset): Enumeration of allowed values
        additional_properties (bool | Unset): Whether additional properties are allowed
    """

    schema: str | Unset = UNSET
    id: str | Unset = UNSET
    create_only: bool | Unset = UNSET
    default: DatabasePropertySchemaResponseDefault | Unset = UNSET
    example: DatabasePropertySchemaResponseExample | Unset = UNSET
    max_length: int | Unset = UNSET
    min_length: int | Unset = UNSET
    pattern: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    user_error: str | Unset = UNSET
    items: DatabasePropertySchemaResponse | Unset = UNSET
    properties: DatabasePropertySchemaResponseProperties | Unset = UNSET
    dependencies: DatabasePropertySchemaResponseDependencies | Unset = UNSET
    required: list[str] | Unset = UNSET
    max_items: int | Unset = UNSET
    description: str | Unset = UNSET
    minimum: list[DatabasePropertySchemaResponseMinimumItem] | Unset = UNSET
    maximum: list[DatabasePropertySchemaResponseMaximumItem] | Unset = UNSET
    enum: list[Any] | Unset = UNSET
    additional_properties: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        id = self.id

        create_only = self.create_only

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        max_length = self.max_length

        min_length = self.min_length

        pattern = self.pattern

        title = self.title

        type_ = self.type_

        user_error = self.user_error

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        dependencies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies.to_dict()

        required: list[str] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        max_items = self.max_items

        description = self.description

        minimum: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.minimum, Unset):
            minimum = []
            for minimum_item_data in self.minimum:
                minimum_item = minimum_item_data.to_dict()
                minimum.append(minimum_item)

        maximum: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.maximum, Unset):
            maximum = []
            for maximum_item_data in self.maximum:
                maximum_item = maximum_item_data.to_dict()
                maximum.append(maximum_item)

        enum: list[Any] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        additional_properties = self.additional_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if id is not UNSET:
            field_dict["$id"] = id
        if create_only is not UNSET:
            field_dict["createOnly"] = create_only
        if default is not UNSET:
            field_dict["default"] = default
        if example is not UNSET:
            field_dict["example"] = example
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_error is not UNSET:
            field_dict["user_error"] = user_error
        if items is not UNSET:
            field_dict["items"] = items
        if properties is not UNSET:
            field_dict["properties"] = properties
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if required is not UNSET:
            field_dict["required"] = required
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if description is not UNSET:
            field_dict["description"] = description
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if enum is not UNSET:
            field_dict["enum"] = enum
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_property_schema_response_default import (
            DatabasePropertySchemaResponseDefault,  # noqa: PLC0415
        )
        from ..models.database_property_schema_response_dependencies import (
            DatabasePropertySchemaResponseDependencies,  # noqa: PLC0415
        )
        from ..models.database_property_schema_response_example import (
            DatabasePropertySchemaResponseExample,  # noqa: PLC0415
        )
        from ..models.database_property_schema_response_maximum_item import (
            DatabasePropertySchemaResponseMaximumItem,  # noqa: PLC0415
        )
        from ..models.database_property_schema_response_minimum_item import (
            DatabasePropertySchemaResponseMinimumItem,  # noqa: PLC0415
        )
        from ..models.database_property_schema_response_properties import (
            DatabasePropertySchemaResponseProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        id = d.pop("$id", UNSET)

        create_only = d.pop("createOnly", UNSET)

        _default = d.pop("default", UNSET)
        default: DatabasePropertySchemaResponseDefault | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = DatabasePropertySchemaResponseDefault.from_dict(_default)

        _example = d.pop("example", UNSET)
        example: DatabasePropertySchemaResponseExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = DatabasePropertySchemaResponseExample.from_dict(_example)

        max_length = d.pop("maxLength", UNSET)

        min_length = d.pop("minLength", UNSET)

        pattern = d.pop("pattern", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        user_error = d.pop("user_error", UNSET)

        _items = d.pop("items", UNSET)
        items: DatabasePropertySchemaResponse | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = DatabasePropertySchemaResponse.from_dict(_items)

        _properties = d.pop("properties", UNSET)
        properties: DatabasePropertySchemaResponseProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabasePropertySchemaResponseProperties.from_dict(_properties)

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: DatabasePropertySchemaResponseDependencies | Unset
        if isinstance(_dependencies, Unset):
            dependencies = UNSET
        else:
            dependencies = DatabasePropertySchemaResponseDependencies.from_dict(_dependencies)

        required = cast(list[str], d.pop("required", UNSET))

        max_items = d.pop("maxItems", UNSET)

        description = d.pop("description", UNSET)

        _minimum = d.pop("minimum", UNSET)
        minimum: list[DatabasePropertySchemaResponseMinimumItem] | Unset = UNSET
        if _minimum is not UNSET:
            minimum = []
            for minimum_item_data in _minimum:
                minimum_item = DatabasePropertySchemaResponseMinimumItem.from_dict(minimum_item_data)

                minimum.append(minimum_item)

        _maximum = d.pop("maximum", UNSET)
        maximum: list[DatabasePropertySchemaResponseMaximumItem] | Unset = UNSET
        if _maximum is not UNSET:
            maximum = []
            for maximum_item_data in _maximum:
                maximum_item = DatabasePropertySchemaResponseMaximumItem.from_dict(maximum_item_data)

                maximum.append(maximum_item)

        enum = cast(list[Any], d.pop("enum", UNSET))

        additional_properties = d.pop("additionalProperties", UNSET)

        database_property_schema_response = cls(
            schema=schema,
            id=id,
            create_only=create_only,
            default=default,
            example=example,
            max_length=max_length,
            min_length=min_length,
            pattern=pattern,
            title=title,
            type_=type_,
            user_error=user_error,
            items=items,
            properties=properties,
            dependencies=dependencies,
            required=required,
            max_items=max_items,
            description=description,
            minimum=minimum,
            maximum=maximum,
            enum=enum,
            additional_properties=additional_properties,
        )

        database_property_schema_response.additional_properties = d
        return database_property_schema_response

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
