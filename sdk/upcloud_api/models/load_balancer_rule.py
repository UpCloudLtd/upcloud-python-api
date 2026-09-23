from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.load_balancer_rule_matching_condition import LoadBalancerRuleMatchingCondition

if TYPE_CHECKING:
    from ..models.load_balancer_action_response import LoadBalancerActionResponse
    from ..models.load_balancer_matcher_response import LoadBalancerMatcherResponse


T = TypeVar("T", bound="LoadBalancerRule")


@_attrs_define
class LoadBalancerRule:
    """Represents a load balancer rule that defines how incoming traffic is matched and processed by a frontend, including
    priority, matching conditions, and actions to perform.

        Attributes:
            name (str): Human-readable name assigned to the routing rule. Example: redirect-to-https.
            priority (int): Priority order for rule evaluation, where lower values indicate higher priority. Example: 100.
            matching_condition (LoadBalancerRuleMatchingCondition): Logical operator determining how multiple matchers are
                combined (and/or). Example: and.
            matchers (list[LoadBalancerMatcherResponse]): List of conditions that incoming requests must satisfy for this
                rule to apply. Example: [{'type': 'path', 'inverse': False, 'match_path': {'method': 'starts_with', 'value':
                '/api', 'ignore_case': True}}].
            actions (list[LoadBalancerActionResponse]): List of actions to execute when the rule matches an incoming
                request. Example: [{'type': 'set_forwarded_headers', 'action_set_forwarded_headers': {}}, {'type':
                'set_request_header', 'action_set_request_header': {'header': 'X-Forwarded-Proto', 'value': 'https'}}, {'type':
                'http_redirect', 'action_http_redirect': {'location': 'https://example.com', 'status': 301}}].
            created_at (datetime.datetime): Timestamp when the rule was created (RFC 3339 format).
            updated_at (datetime.datetime): Timestamp when the rule was last updated (RFC 3339 format).
    """

    name: str
    priority: int
    matching_condition: LoadBalancerRuleMatchingCondition
    matchers: list[LoadBalancerMatcherResponse]
    actions: list[LoadBalancerActionResponse]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        priority = self.priority

        matching_condition = self.matching_condition.value

        matchers = []
        for matchers_item_data in self.matchers:
            matchers_item = matchers_item_data.to_dict()
            matchers.append(matchers_item)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "priority": priority,
                "matching_condition": matching_condition,
                "matchers": matchers,
                "actions": actions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_response import LoadBalancerActionResponse  # noqa: PLC0415
        from ..models.load_balancer_matcher_response import LoadBalancerMatcherResponse  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        priority = d.pop("priority")

        matching_condition = LoadBalancerRuleMatchingCondition(d.pop("matching_condition"))

        matchers = []
        _matchers = d.pop("matchers")
        for matchers_item_data in _matchers:
            matchers_item = LoadBalancerMatcherResponse.from_dict(matchers_item_data)

            matchers.append(matchers_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = LoadBalancerActionResponse.from_dict(actions_item_data)

            actions.append(actions_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_rule = cls(
            name=name,
            priority=priority,
            matching_condition=matching_condition,
            matchers=matchers,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
        )

        load_balancer_rule.additional_properties = d
        return load_balancer_rule

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
