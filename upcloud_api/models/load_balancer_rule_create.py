from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.load_balancer_matching_condition import LoadBalancerMatchingCondition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_action_create_type_0 import LoadBalancerActionCreateType0
    from ..models.load_balancer_action_create_type_1 import LoadBalancerActionCreateType1
    from ..models.load_balancer_action_create_type_2 import LoadBalancerActionCreateType2
    from ..models.load_balancer_action_create_type_3 import LoadBalancerActionCreateType3
    from ..models.load_balancer_action_create_type_4 import LoadBalancerActionCreateType4
    from ..models.load_balancer_action_create_type_5 import LoadBalancerActionCreateType5
    from ..models.load_balancer_action_create_type_6 import LoadBalancerActionCreateType6
    from ..models.load_balancer_action_create_type_7 import LoadBalancerActionCreateType7
    from ..models.load_balancer_action_create_type_8 import LoadBalancerActionCreateType8
    from ..models.load_balancer_matcher_create_type_0 import LoadBalancerMatcherCreateType0
    from ..models.load_balancer_matcher_create_type_1 import LoadBalancerMatcherCreateType1
    from ..models.load_balancer_matcher_create_type_2 import LoadBalancerMatcherCreateType2
    from ..models.load_balancer_matcher_create_type_3 import LoadBalancerMatcherCreateType3
    from ..models.load_balancer_matcher_create_type_4 import LoadBalancerMatcherCreateType4
    from ..models.load_balancer_matcher_create_type_5 import LoadBalancerMatcherCreateType5
    from ..models.load_balancer_matcher_create_type_6 import LoadBalancerMatcherCreateType6
    from ..models.load_balancer_matcher_create_type_7 import LoadBalancerMatcherCreateType7
    from ..models.load_balancer_matcher_create_type_8 import LoadBalancerMatcherCreateType8
    from ..models.load_balancer_matcher_create_type_9 import LoadBalancerMatcherCreateType9
    from ..models.load_balancer_matcher_create_type_10 import LoadBalancerMatcherCreateType10
    from ..models.load_balancer_matcher_create_type_11 import LoadBalancerMatcherCreateType11
    from ..models.load_balancer_matcher_create_type_12 import LoadBalancerMatcherCreateType12
    from ..models.load_balancer_matcher_create_type_13 import LoadBalancerMatcherCreateType13
    from ..models.load_balancer_matcher_create_type_14 import LoadBalancerMatcherCreateType14


T = TypeVar("T", bound="LoadBalancerRuleCreate")


@_attrs_define
class LoadBalancerRuleCreate:
    """Load Balancer Forwarding Rule

    Attributes:
        name (str): Name of the rule Example: my-rule.
        priority (int): Priority Example: 10.
        matchers (list[LoadBalancerMatcherCreateType0 | LoadBalancerMatcherCreateType1 | LoadBalancerMatcherCreateType10
            | LoadBalancerMatcherCreateType11 | LoadBalancerMatcherCreateType12 | LoadBalancerMatcherCreateType13 |
            LoadBalancerMatcherCreateType14 | LoadBalancerMatcherCreateType2 | LoadBalancerMatcherCreateType3 |
            LoadBalancerMatcherCreateType4 | LoadBalancerMatcherCreateType5 | LoadBalancerMatcherCreateType6 |
            LoadBalancerMatcherCreateType7 | LoadBalancerMatcherCreateType8 | LoadBalancerMatcherCreateType9] | None): Rule
            matchers
        actions (list[LoadBalancerActionCreateType0 | LoadBalancerActionCreateType1 | LoadBalancerActionCreateType2 |
            LoadBalancerActionCreateType3 | LoadBalancerActionCreateType4 | LoadBalancerActionCreateType5 |
            LoadBalancerActionCreateType6 | LoadBalancerActionCreateType7 | LoadBalancerActionCreateType8]): Rule actions
        matching_condition (LoadBalancerMatchingCondition | Unset): Defines how multiple matching criteria are combined
            to evaluate a condition.
    """

    name: str
    priority: int
    matchers: (
        list[
            LoadBalancerMatcherCreateType0
            | LoadBalancerMatcherCreateType1
            | LoadBalancerMatcherCreateType10
            | LoadBalancerMatcherCreateType11
            | LoadBalancerMatcherCreateType12
            | LoadBalancerMatcherCreateType13
            | LoadBalancerMatcherCreateType14
            | LoadBalancerMatcherCreateType2
            | LoadBalancerMatcherCreateType3
            | LoadBalancerMatcherCreateType4
            | LoadBalancerMatcherCreateType5
            | LoadBalancerMatcherCreateType6
            | LoadBalancerMatcherCreateType7
            | LoadBalancerMatcherCreateType8
            | LoadBalancerMatcherCreateType9
        ]
        | None
    )
    actions: list[
        LoadBalancerActionCreateType0
        | LoadBalancerActionCreateType1
        | LoadBalancerActionCreateType2
        | LoadBalancerActionCreateType3
        | LoadBalancerActionCreateType4
        | LoadBalancerActionCreateType5
        | LoadBalancerActionCreateType6
        | LoadBalancerActionCreateType7
        | LoadBalancerActionCreateType8
    ]
    matching_condition: LoadBalancerMatchingCondition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_action_create_type_0 import LoadBalancerActionCreateType0  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_1 import LoadBalancerActionCreateType1  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_2 import LoadBalancerActionCreateType2  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_3 import LoadBalancerActionCreateType3  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_4 import LoadBalancerActionCreateType4  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_5 import LoadBalancerActionCreateType5  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_6 import LoadBalancerActionCreateType6  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_7 import LoadBalancerActionCreateType7  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_0 import LoadBalancerMatcherCreateType0  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_1 import LoadBalancerMatcherCreateType1  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_2 import LoadBalancerMatcherCreateType2  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_3 import LoadBalancerMatcherCreateType3  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_4 import LoadBalancerMatcherCreateType4  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_5 import LoadBalancerMatcherCreateType5  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_6 import LoadBalancerMatcherCreateType6  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_7 import LoadBalancerMatcherCreateType7  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_8 import LoadBalancerMatcherCreateType8  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_9 import LoadBalancerMatcherCreateType9  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_10 import LoadBalancerMatcherCreateType10  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_11 import LoadBalancerMatcherCreateType11  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_12 import LoadBalancerMatcherCreateType12  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_13 import LoadBalancerMatcherCreateType13  # noqa: PLC0415

        name = self.name

        priority = self.priority

        matchers: list[dict[str, Any]] | None
        if isinstance(self.matchers, list):
            matchers = []
            for matchers_type_0_item_data in self.matchers:
                matchers_type_0_item: dict[str, Any]
                if isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType0):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType1):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType2):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType3):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType4):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType5):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType6):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType7):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType8):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType9):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType10):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType11):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType12):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                elif isinstance(matchers_type_0_item_data, LoadBalancerMatcherCreateType13):
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()
                else:
                    matchers_type_0_item = matchers_type_0_item_data.to_dict()

                matchers.append(matchers_type_0_item)

        else:
            matchers = self.matchers

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, LoadBalancerActionCreateType0):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType1):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType2):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType3):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType4):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType5):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType6):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, LoadBalancerActionCreateType7):
                actions_item = actions_item_data.to_dict()
            else:
                actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        matching_condition: str | Unset = UNSET
        if not isinstance(self.matching_condition, Unset):
            matching_condition = self.matching_condition.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "priority": priority,
                "matchers": matchers,
                "actions": actions,
            }
        )
        if matching_condition is not UNSET:
            field_dict["matching_condition"] = matching_condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_create_type_0 import LoadBalancerActionCreateType0  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_1 import LoadBalancerActionCreateType1  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_2 import LoadBalancerActionCreateType2  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_3 import LoadBalancerActionCreateType3  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_4 import LoadBalancerActionCreateType4  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_5 import LoadBalancerActionCreateType5  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_6 import LoadBalancerActionCreateType6  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_7 import LoadBalancerActionCreateType7  # noqa: PLC0415
        from ..models.load_balancer_action_create_type_8 import LoadBalancerActionCreateType8  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_0 import LoadBalancerMatcherCreateType0  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_1 import LoadBalancerMatcherCreateType1  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_2 import LoadBalancerMatcherCreateType2  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_3 import LoadBalancerMatcherCreateType3  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_4 import LoadBalancerMatcherCreateType4  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_5 import LoadBalancerMatcherCreateType5  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_6 import LoadBalancerMatcherCreateType6  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_7 import LoadBalancerMatcherCreateType7  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_8 import LoadBalancerMatcherCreateType8  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_9 import LoadBalancerMatcherCreateType9  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_10 import LoadBalancerMatcherCreateType10  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_11 import LoadBalancerMatcherCreateType11  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_12 import LoadBalancerMatcherCreateType12  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_13 import LoadBalancerMatcherCreateType13  # noqa: PLC0415
        from ..models.load_balancer_matcher_create_type_14 import LoadBalancerMatcherCreateType14  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        priority = d.pop("priority")

        def _parse_matchers(
            data: object,
        ) -> (
            list[
                LoadBalancerMatcherCreateType0
                | LoadBalancerMatcherCreateType1
                | LoadBalancerMatcherCreateType10
                | LoadBalancerMatcherCreateType11
                | LoadBalancerMatcherCreateType12
                | LoadBalancerMatcherCreateType13
                | LoadBalancerMatcherCreateType14
                | LoadBalancerMatcherCreateType2
                | LoadBalancerMatcherCreateType3
                | LoadBalancerMatcherCreateType4
                | LoadBalancerMatcherCreateType5
                | LoadBalancerMatcherCreateType6
                | LoadBalancerMatcherCreateType7
                | LoadBalancerMatcherCreateType8
                | LoadBalancerMatcherCreateType9
            ]
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                matchers_type_0 = []
                _matchers_type_0 = data
                for matchers_type_0_item_data in _matchers_type_0:

                    def _parse_matchers_type_0_item(
                        data: object,
                    ) -> (
                        LoadBalancerMatcherCreateType0
                        | LoadBalancerMatcherCreateType1
                        | LoadBalancerMatcherCreateType10
                        | LoadBalancerMatcherCreateType11
                        | LoadBalancerMatcherCreateType12
                        | LoadBalancerMatcherCreateType13
                        | LoadBalancerMatcherCreateType14
                        | LoadBalancerMatcherCreateType2
                        | LoadBalancerMatcherCreateType3
                        | LoadBalancerMatcherCreateType4
                        | LoadBalancerMatcherCreateType5
                        | LoadBalancerMatcherCreateType6
                        | LoadBalancerMatcherCreateType7
                        | LoadBalancerMatcherCreateType8
                        | LoadBalancerMatcherCreateType9
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_0 = (
                                LoadBalancerMatcherCreateType0.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_1 = (
                                LoadBalancerMatcherCreateType1.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_2 = (
                                LoadBalancerMatcherCreateType2.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_3 = (
                                LoadBalancerMatcherCreateType3.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_4 = (
                                LoadBalancerMatcherCreateType4.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_5 = (
                                LoadBalancerMatcherCreateType5.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_6 = (
                                LoadBalancerMatcherCreateType6.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_7 = (
                                LoadBalancerMatcherCreateType7.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_8 = (
                                LoadBalancerMatcherCreateType8.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_9 = (
                                LoadBalancerMatcherCreateType9.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_10 = (
                                LoadBalancerMatcherCreateType10.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_11 = (
                                LoadBalancerMatcherCreateType11.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_12 = (
                                LoadBalancerMatcherCreateType12.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_12
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemasload_balancer_matcher_create_type_13 = (
                                LoadBalancerMatcherCreateType13.from_dict(data)
                            )

                            return componentsschemasload_balancer_matcher_create_type_13
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemasload_balancer_matcher_create_type_14 = (
                            LoadBalancerMatcherCreateType14.from_dict(data)
                        )

                        return componentsschemasload_balancer_matcher_create_type_14

                    matchers_type_0_item = _parse_matchers_type_0_item(matchers_type_0_item_data)

                    matchers_type_0.append(matchers_type_0_item)

                return matchers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    LoadBalancerMatcherCreateType0
                    | LoadBalancerMatcherCreateType1
                    | LoadBalancerMatcherCreateType10
                    | LoadBalancerMatcherCreateType11
                    | LoadBalancerMatcherCreateType12
                    | LoadBalancerMatcherCreateType13
                    | LoadBalancerMatcherCreateType14
                    | LoadBalancerMatcherCreateType2
                    | LoadBalancerMatcherCreateType3
                    | LoadBalancerMatcherCreateType4
                    | LoadBalancerMatcherCreateType5
                    | LoadBalancerMatcherCreateType6
                    | LoadBalancerMatcherCreateType7
                    | LoadBalancerMatcherCreateType8
                    | LoadBalancerMatcherCreateType9
                ]
                | None,
                data,
            )

        matchers = _parse_matchers(d.pop("matchers"))

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> (
                LoadBalancerActionCreateType0
                | LoadBalancerActionCreateType1
                | LoadBalancerActionCreateType2
                | LoadBalancerActionCreateType3
                | LoadBalancerActionCreateType4
                | LoadBalancerActionCreateType5
                | LoadBalancerActionCreateType6
                | LoadBalancerActionCreateType7
                | LoadBalancerActionCreateType8
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_0 = LoadBalancerActionCreateType0.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_1 = LoadBalancerActionCreateType1.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_2 = LoadBalancerActionCreateType2.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_3 = LoadBalancerActionCreateType3.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_4 = LoadBalancerActionCreateType4.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_5 = LoadBalancerActionCreateType5.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_6 = LoadBalancerActionCreateType6.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemasload_balancer_action_create_type_7 = LoadBalancerActionCreateType7.from_dict(data)

                    return componentsschemasload_balancer_action_create_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasload_balancer_action_create_type_8 = LoadBalancerActionCreateType8.from_dict(data)

                return componentsschemasload_balancer_action_create_type_8

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        _matching_condition = d.pop("matching_condition", UNSET)
        matching_condition: LoadBalancerMatchingCondition | Unset
        if isinstance(_matching_condition, Unset):
            matching_condition = UNSET
        else:
            matching_condition = LoadBalancerMatchingCondition(_matching_condition)

        load_balancer_rule_create = cls(
            name=name,
            priority=priority,
            matchers=matchers,
            actions=actions,
            matching_condition=matching_condition,
        )

        return load_balancer_rule_create
