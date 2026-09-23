from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_storage_2_service_detail_response_configured_status import (
    ObjectStorage2ServiceDetailResponseConfiguredStatus,
)
from ..models.object_storage_2_service_detail_response_operational_state import (
    ObjectStorage2ServiceDetailResponseOperationalState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_custom_domain_detail_response import ObjectStorage2CustomDomainDetailResponse
    from ..models.object_storage_2_endpoint_response import ObjectStorage2EndpointResponse
    from ..models.object_storage_2_label_detail_response import ObjectStorage2LabelDetailResponse
    from ..models.object_storage_2_network_detail_response import ObjectStorage2NetworkDetailResponse
    from ..models.object_storage_2_service_detail_response_state_messages_item import (
        ObjectStorage2ServiceDetailResponseStateMessagesItem,
    )
    from ..models.object_storage_2_service_detail_response_usage import ObjectStorage2ServiceDetailResponseUsage
    from ..models.object_storage_2_static_website_config import ObjectStorage2StaticWebsiteConfig
    from ..models.object_storage_2_user_detail_response import ObjectStorage2UserDetailResponse


T = TypeVar("T", bound="ObjectStorage2ServiceDetailResponse")


@_attrs_define
class ObjectStorage2ServiceDetailResponse:
    """Response schema for service details, including UUID, name, and endpoints.

    Attributes:
        uuid (str | Unset):  Example: 1200ecde-db95-4d1c-9133-6508f3232567.
        name (str | Unset):  Example: example-service.
        region (str | Unset):  Example: europe-1.
        configured_status (ObjectStorage2ServiceDetailResponseConfiguredStatus | Unset):  Example: started.
        operational_state (ObjectStorage2ServiceDetailResponseOperationalState | Unset):  Example: running.
        networks (list[ObjectStorage2NetworkDetailResponse] | Unset):
        usage (ObjectStorage2ServiceDetailResponseUsage | Unset):
        labels (list[ObjectStorage2LabelDetailResponse] | Unset):
        users (list[ObjectStorage2UserDetailResponse] | Unset):
        endpoints (list[ObjectStorage2EndpointResponse] | Unset):
        custom_domains (list[ObjectStorage2CustomDomainDetailResponse] | Unset):
        static_websites (list[ObjectStorage2StaticWebsiteConfig] | Unset): Static website configurations for this
            service
        state_messages (list[ObjectStorage2ServiceDetailResponseStateMessagesItem] | Unset):
        termination_protection (bool | Unset):  Example: False.
        created_at (datetime.datetime | Unset):  Example: 2023-05-07T15:55:24.655776Z.
        updated_at (datetime.datetime | Unset):  Example: 2023-05-07T21:38:15.757405Z.
    """

    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    configured_status: ObjectStorage2ServiceDetailResponseConfiguredStatus | Unset = UNSET
    operational_state: ObjectStorage2ServiceDetailResponseOperationalState | Unset = UNSET
    networks: list[ObjectStorage2NetworkDetailResponse] | Unset = UNSET
    usage: ObjectStorage2ServiceDetailResponseUsage | Unset = UNSET
    labels: list[ObjectStorage2LabelDetailResponse] | Unset = UNSET
    users: list[ObjectStorage2UserDetailResponse] | Unset = UNSET
    endpoints: list[ObjectStorage2EndpointResponse] | Unset = UNSET
    custom_domains: list[ObjectStorage2CustomDomainDetailResponse] | Unset = UNSET
    static_websites: list[ObjectStorage2StaticWebsiteConfig] | Unset = UNSET
    state_messages: list[ObjectStorage2ServiceDetailResponseStateMessagesItem] | Unset = UNSET
    termination_protection: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        region = self.region

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        operational_state: str | Unset = UNSET
        if not isinstance(self.operational_state, Unset):
            operational_state = self.operational_state.value

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        endpoints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = []
            for endpoints_item_data in self.endpoints:
                endpoints_item = endpoints_item_data.to_dict()
                endpoints.append(endpoints_item)

        custom_domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_domains, Unset):
            custom_domains = []
            for custom_domains_item_data in self.custom_domains:
                custom_domains_item = custom_domains_item_data.to_dict()
                custom_domains.append(custom_domains_item)

        static_websites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.static_websites, Unset):
            static_websites = []
            for static_websites_item_data in self.static_websites:
                static_websites_item = static_websites_item_data.to_dict()
                static_websites.append(static_websites_item)

        state_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.state_messages, Unset):
            state_messages = []
            for state_messages_item_data in self.state_messages:
                state_messages_item = state_messages_item_data.to_dict()
                state_messages.append(state_messages_item)

        termination_protection = self.termination_protection

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if networks is not UNSET:
            field_dict["networks"] = networks
        if usage is not UNSET:
            field_dict["usage"] = usage
        if labels is not UNSET:
            field_dict["labels"] = labels
        if users is not UNSET:
            field_dict["users"] = users
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if custom_domains is not UNSET:
            field_dict["custom_domains"] = custom_domains
        if static_websites is not UNSET:
            field_dict["static_websites"] = static_websites
        if state_messages is not UNSET:
            field_dict["state_messages"] = state_messages
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_custom_domain_detail_response import (
            ObjectStorage2CustomDomainDetailResponse,  # noqa: PLC0415
        )
        from ..models.object_storage_2_endpoint_response import ObjectStorage2EndpointResponse  # noqa: PLC0415
        from ..models.object_storage_2_label_detail_response import ObjectStorage2LabelDetailResponse  # noqa: PLC0415
        from ..models.object_storage_2_network_detail_response import (
            ObjectStorage2NetworkDetailResponse,  # noqa: PLC0415
        )
        from ..models.object_storage_2_service_detail_response_state_messages_item import (
            ObjectStorage2ServiceDetailResponseStateMessagesItem,  # noqa: PLC0415
        )
        from ..models.object_storage_2_service_detail_response_usage import (
            ObjectStorage2ServiceDetailResponseUsage,  # noqa: PLC0415
        )
        from ..models.object_storage_2_static_website_config import ObjectStorage2StaticWebsiteConfig  # noqa: PLC0415
        from ..models.object_storage_2_user_detail_response import ObjectStorage2UserDetailResponse  # noqa: PLC0415

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: ObjectStorage2ServiceDetailResponseConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = ObjectStorage2ServiceDetailResponseConfiguredStatus(_configured_status)

        _operational_state = d.pop("operational_state", UNSET)
        operational_state: ObjectStorage2ServiceDetailResponseOperationalState | Unset
        if isinstance(_operational_state, Unset):
            operational_state = UNSET
        else:
            operational_state = ObjectStorage2ServiceDetailResponseOperationalState(_operational_state)

        _networks = d.pop("networks", UNSET)
        networks: list[ObjectStorage2NetworkDetailResponse] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = ObjectStorage2NetworkDetailResponse.from_dict(networks_item_data)

                networks.append(networks_item)

        _usage = d.pop("usage", UNSET)
        usage: ObjectStorage2ServiceDetailResponseUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ObjectStorage2ServiceDetailResponseUsage.from_dict(_usage)

        _labels = d.pop("labels", UNSET)
        labels: list[ObjectStorage2LabelDetailResponse] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = ObjectStorage2LabelDetailResponse.from_dict(labels_item_data)

                labels.append(labels_item)

        _users = d.pop("users", UNSET)
        users: list[ObjectStorage2UserDetailResponse] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = ObjectStorage2UserDetailResponse.from_dict(users_item_data)

                users.append(users_item)

        _endpoints = d.pop("endpoints", UNSET)
        endpoints: list[ObjectStorage2EndpointResponse] | Unset = UNSET
        if _endpoints is not UNSET:
            endpoints = []
            for endpoints_item_data in _endpoints:
                endpoints_item = ObjectStorage2EndpointResponse.from_dict(endpoints_item_data)

                endpoints.append(endpoints_item)

        _custom_domains = d.pop("custom_domains", UNSET)
        custom_domains: list[ObjectStorage2CustomDomainDetailResponse] | Unset = UNSET
        if _custom_domains is not UNSET:
            custom_domains = []
            for custom_domains_item_data in _custom_domains:
                custom_domains_item = ObjectStorage2CustomDomainDetailResponse.from_dict(custom_domains_item_data)

                custom_domains.append(custom_domains_item)

        _static_websites = d.pop("static_websites", UNSET)
        static_websites: list[ObjectStorage2StaticWebsiteConfig] | Unset = UNSET
        if _static_websites is not UNSET:
            static_websites = []
            for static_websites_item_data in _static_websites:
                static_websites_item = ObjectStorage2StaticWebsiteConfig.from_dict(static_websites_item_data)

                static_websites.append(static_websites_item)

        _state_messages = d.pop("state_messages", UNSET)
        state_messages: list[ObjectStorage2ServiceDetailResponseStateMessagesItem] | Unset = UNSET
        if _state_messages is not UNSET:
            state_messages = []
            for state_messages_item_data in _state_messages:
                state_messages_item = ObjectStorage2ServiceDetailResponseStateMessagesItem.from_dict(
                    state_messages_item_data
                )

                state_messages.append(state_messages_item)

        termination_protection = d.pop("termination_protection", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        object_storage_2_service_detail_response = cls(
            uuid=uuid,
            name=name,
            region=region,
            configured_status=configured_status,
            operational_state=operational_state,
            networks=networks,
            usage=usage,
            labels=labels,
            users=users,
            endpoints=endpoints,
            custom_domains=custom_domains,
            static_websites=static_websites,
            state_messages=state_messages,
            termination_protection=termination_protection,
            created_at=created_at,
            updated_at=updated_at,
        )

        object_storage_2_service_detail_response.additional_properties = d
        return object_storage_2_service_detail_response

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
