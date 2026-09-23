from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0:
    """
    Attributes:
        account (str):
        key (str | Unset): Azure account secret key. One of key or sas_token should be specified
        sas_token (str | Unset): A shared access signatures (SAS) token. One of key or sas_token should be specified
    """

    account: str
    key: str | Unset = UNSET
    sas_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account = self.account

        key = self.key

        sas_token = self.sas_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account": account,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if sas_token is not UNSET:
            field_dict["sas_token"] = sas_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account")

        key = d.pop("key", UNSET)

        sas_token = d.pop("sas_token", UNSET)

        database_service_properties_opensearch_custom_keystores_item_settings_type_0 = cls(
            account=account,
            key=key,
            sas_token=sas_token,
        )

        return database_service_properties_opensearch_custom_keystores_item_settings_type_0
