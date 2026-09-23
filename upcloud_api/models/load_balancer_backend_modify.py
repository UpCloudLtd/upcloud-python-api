from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_backend_properties_create import LoadBalancerBackendPropertiesCreate
    from ..models.load_balancer_member_modify_type_0 import LoadBalancerMemberModifyType0
    from ..models.load_balancer_member_modify_type_1 import LoadBalancerMemberModifyType1
    from ..models.load_balancer_tls_config_create import LoadBalancerTlsConfigCreate


T = TypeVar("T", bound="LoadBalancerBackendModify")


@_attrs_define
class LoadBalancerBackendModify:
    """Load Balancer Backend

    Attributes:
        name (str | Unset): Name of the backend
        members (list[LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1] | None | Unset): Backend members
        tls_configs (list[LoadBalancerTlsConfigCreate] | None | Unset): TLS Configs
        resolver (None | str | Unset): Resolver reference
        properties (LoadBalancerBackendPropertiesCreate | Unset): Backend Properties
    """

    name: str | Unset = UNSET
    members: list[LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1] | None | Unset = UNSET
    tls_configs: list[LoadBalancerTlsConfigCreate] | None | Unset = UNSET
    resolver: None | str | Unset = UNSET
    properties: LoadBalancerBackendPropertiesCreate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_member_modify_type_0 import LoadBalancerMemberModifyType0  # noqa: PLC0415

        name = self.name

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item: dict[str, Any]
                if isinstance(members_type_0_item_data, LoadBalancerMemberModifyType0):
                    members_type_0_item = members_type_0_item_data.to_dict()
                else:
                    members_type_0_item = members_type_0_item_data.to_dict()

                members.append(members_type_0_item)

        else:
            members = self.members

        tls_configs: list[dict[str, Any]] | None | Unset
        if isinstance(self.tls_configs, Unset):
            tls_configs = UNSET
        elif isinstance(self.tls_configs, list):
            tls_configs = []
            for tls_configs_type_0_item_data in self.tls_configs:
                tls_configs_type_0_item = tls_configs_type_0_item_data.to_dict()
                tls_configs.append(tls_configs_type_0_item)

        else:
            tls_configs = self.tls_configs

        resolver: None | str | Unset
        if isinstance(self.resolver, Unset):
            resolver = UNSET
        else:
            resolver = self.resolver

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if members is not UNSET:
            field_dict["members"] = members
        if tls_configs is not UNSET:
            field_dict["tls_configs"] = tls_configs
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_backend_properties_create import (
            LoadBalancerBackendPropertiesCreate,  # noqa: PLC0415
        )
        from ..models.load_balancer_member_modify_type_0 import LoadBalancerMemberModifyType0  # noqa: PLC0415
        from ..models.load_balancer_member_modify_type_1 import LoadBalancerMemberModifyType1  # noqa: PLC0415
        from ..models.load_balancer_tls_config_create import LoadBalancerTlsConfigCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_members(
            data: object,
        ) -> list[LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in _members_type_0:

                    def _parse_members_type_0_item(
                        data: object,
                    ) -> LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_member_modify_type_0 = (
                                LoadBalancerMemberModifyType0.from_dict(data)
                            )

                            return componentsschemasload_balancer_member_modify_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasload_balancer_member_modify_type_1 = LoadBalancerMemberModifyType1.from_dict(
                            data
                        )

                        return componentsschemasload_balancer_member_modify_type_1

                    members_type_0_item = _parse_members_type_0_item(members_type_0_item_data)

                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))

        def _parse_tls_configs(data: object) -> list[LoadBalancerTlsConfigCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tls_configs_type_0 = []
                _tls_configs_type_0 = data
                for tls_configs_type_0_item_data in _tls_configs_type_0:
                    tls_configs_type_0_item = LoadBalancerTlsConfigCreate.from_dict(tls_configs_type_0_item_data)

                    tls_configs_type_0.append(tls_configs_type_0_item)

                return tls_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LoadBalancerTlsConfigCreate] | None | Unset, data)

        tls_configs = _parse_tls_configs(d.pop("tls_configs", UNSET))

        def _parse_resolver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolver = _parse_resolver(d.pop("resolver", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: LoadBalancerBackendPropertiesCreate | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = LoadBalancerBackendPropertiesCreate.from_dict(_properties)

        load_balancer_backend_modify = cls(
            name=name,
            members=members,
            tls_configs=tls_configs,
            resolver=resolver,
            properties=properties,
        )

        return load_balancer_backend_modify
