from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_glob_pattern_and_number_of_indexes_matching_that_pattern_to_be_kept_deletion_sorting_algorithm import (
    DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDeletionSortingAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept")


@_attrs_define
class DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKept:
    """Allows you to create glob style patterns and set a max number of indexes matching this pattern you want to keep.
    Creating indexes exceeding this value will cause the oldest one to get deleted. You could for example create a
    pattern looking like 'logs.?' and then create index logs.1, logs.2 etc, it will delete logs.1 once you create
    logs.6. Do note 'logs.?' does not apply to logs.10. Note: Setting max_index_count to 0 will do nothing and the
    pattern gets ignored.

        Attributes:
            max_index_count (int):  Example: 3.
            pattern (str):  Example: logs_*_foo_*.
            sorting_algorithm (DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDe
                letionSortingAlgorithm | Unset):  Default: DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatch
                ingThatPatternToBeKeptDeletionSortingAlgorithm.CREATION_DATE.
    """

    max_index_count: int
    pattern: str
    sorting_algorithm: (
        DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDeletionSortingAlgorithm
        | Unset
    ) = DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDeletionSortingAlgorithm.CREATION_DATE

    def to_dict(self) -> dict[str, Any]:
        max_index_count = self.max_index_count

        pattern = self.pattern

        sorting_algorithm: str | Unset = UNSET
        if not isinstance(self.sorting_algorithm, Unset):
            sorting_algorithm = self.sorting_algorithm.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "max_index_count": max_index_count,
                "pattern": pattern,
            }
        )
        if sorting_algorithm is not UNSET:
            field_dict["sorting_algorithm"] = sorting_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_index_count = d.pop("max_index_count")

        pattern = d.pop("pattern")

        _sorting_algorithm = d.pop("sorting_algorithm", UNSET)
        sorting_algorithm: (
            DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDeletionSortingAlgorithm
            | Unset
        )
        if isinstance(_sorting_algorithm, Unset):
            sorting_algorithm = UNSET
        else:
            sorting_algorithm = DatabaseServicePropertiesOpensearchGlobPatternAndNumberOfIndexesMatchingThatPatternToBeKeptDeletionSortingAlgorithm(
                _sorting_algorithm
            )

        database_service_properties_opensearch_glob_pattern_and_number_of_indexes_matching_that_pattern_to_be_kept = (
            cls(
                max_index_count=max_index_count,
                pattern=pattern,
                sorting_algorithm=sorting_algorithm,
            )
        )

        return (
            database_service_properties_opensearch_glob_pattern_and_number_of_indexes_matching_that_pattern_to_be_kept
        )
