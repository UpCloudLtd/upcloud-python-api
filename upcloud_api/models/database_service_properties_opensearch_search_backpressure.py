from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_search_backpressure_the_search_backpressure_mode import (
    DatabaseServicePropertiesOpensearchSearchBackpressureTheSearchBackpressureMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_search_backpressure_node_duress_settings import (
        DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings,
    )
    from ..models.database_service_properties_opensearch_search_backpressure_search_shard_settings import (
        DatabaseServicePropertiesOpensearchSearchBackpressureSearchShardSettings,
    )
    from ..models.database_service_properties_opensearch_search_backpressure_search_task_settings import (
        DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSearchBackpressure")


@_attrs_define
class DatabaseServicePropertiesOpensearchSearchBackpressure:
    """
    Attributes:
        mode (DatabaseServicePropertiesOpensearchSearchBackpressureTheSearchBackpressureMode | Unset): The search
            backpressure mode. Valid values are monitor_only, enforced, or disabled. Default is monitor_only
        node_duress (DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings | Unset):
        search_shard_task (DatabaseServicePropertiesOpensearchSearchBackpressureSearchShardSettings | Unset):
        search_task (DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings | Unset):
    """

    mode: DatabaseServicePropertiesOpensearchSearchBackpressureTheSearchBackpressureMode | Unset = UNSET
    node_duress: DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings | Unset = UNSET
    search_shard_task: DatabaseServicePropertiesOpensearchSearchBackpressureSearchShardSettings | Unset = UNSET
    search_task: DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        node_duress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_duress, Unset):
            node_duress = self.node_duress.to_dict()

        search_shard_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_shard_task, Unset):
            search_shard_task = self.search_shard_task.to_dict()

        search_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_task, Unset):
            search_task = self.search_task.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if node_duress is not UNSET:
            field_dict["node_duress"] = node_duress
        if search_shard_task is not UNSET:
            field_dict["search_shard_task"] = search_shard_task
        if search_task is not UNSET:
            field_dict["search_task"] = search_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_search_backpressure_node_duress_settings import (
            DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_search_backpressure_search_shard_settings import (
            DatabaseServicePropertiesOpensearchSearchBackpressureSearchShardSettings,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_search_backpressure_search_task_settings import (
            DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: DatabaseServicePropertiesOpensearchSearchBackpressureTheSearchBackpressureMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = DatabaseServicePropertiesOpensearchSearchBackpressureTheSearchBackpressureMode(_mode)

        _node_duress = d.pop("node_duress", UNSET)
        node_duress: DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings | Unset
        if isinstance(_node_duress, Unset):
            node_duress = UNSET
        else:
            node_duress = DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings.from_dict(
                _node_duress
            )

        _search_shard_task = d.pop("search_shard_task", UNSET)
        search_shard_task: DatabaseServicePropertiesOpensearchSearchBackpressureSearchShardSettings | Unset
        if isinstance(_search_shard_task, Unset):
            search_shard_task = UNSET
        else:
            search_shard_task = DatabaseServicePropertiesOpensearchSearchBackpressureSearchShardSettings.from_dict(
                _search_shard_task
            )

        _search_task = d.pop("search_task", UNSET)
        search_task: DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings | Unset
        if isinstance(_search_task, Unset):
            search_task = UNSET
        else:
            search_task = DatabaseServicePropertiesOpensearchSearchBackpressureSearchTaskSettings.from_dict(
                _search_task
            )

        database_service_properties_opensearch_search_backpressure = cls(
            mode=mode,
            node_duress=node_duress,
            search_shard_task=search_shard_task,
            search_task=search_task,
        )

        return database_service_properties_opensearch_search_backpressure
