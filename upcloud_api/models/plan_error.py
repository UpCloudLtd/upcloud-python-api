from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.plan_error_error import PlanErrorError


T = TypeVar("T", bound="PlanError")


@_attrs_define
class PlanError:
    """A general error response indicating that the request could not be fulfilled due to a technical issue.

    Attributes:
        error (PlanErrorError):
    """

    error: PlanErrorError

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_error_error import PlanErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = PlanErrorError.from_dict(d.pop("error"))

        plan_error = cls(
            error=error,
        )

        return plan_error
