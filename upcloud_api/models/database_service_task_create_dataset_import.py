from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceTaskCreateDatasetImport")


@_attrs_define
class DatabaseServiceTaskCreateDatasetImport:
    """
    Attributes:
        dataset_name (str): The name of the dataset to be imported.
    """

    dataset_name: str

    def to_dict(self) -> dict[str, Any]:
        dataset_name = self.dataset_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dataset_name": dataset_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_name = d.pop("dataset_name")

        database_service_task_create_dataset_import = cls(
            dataset_name=dataset_name,
        )

        return database_service_task_create_dataset_import
