from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.account_boolean_yesno import AccountBooleanYesno
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_label import AccountLabel
    from ..models.create_subaccount_request_sub_account_ip_filters import CreateSubaccountRequestSubAccountIpFilters
    from ..models.create_subaccount_request_sub_account_network_access import (
        CreateSubaccountRequestSubAccountNetworkAccess,
    )
    from ..models.create_subaccount_request_sub_account_roles import CreateSubaccountRequestSubAccountRoles
    from ..models.create_subaccount_request_sub_account_server_access import (
        CreateSubaccountRequestSubAccountServerAccess,
    )
    from ..models.create_subaccount_request_sub_account_storage_access import (
        CreateSubaccountRequestSubAccountStorageAccess,
    )
    from ..models.create_subaccount_request_sub_account_tag_access import CreateSubaccountRequestSubAccountTagAccess


T = TypeVar("T", bound="CreateSubaccountRequestSubAccount")


@_attrs_define
class CreateSubaccountRequestSubAccount:
    """
    Attributes:
        username (str): Username for an account.
        email (str):
        phone (str): Phone number in international format.
        language (str): ISO 639-1 code
        timezone (str):
        password (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        company (str | Unset):
        vat_number (str | Unset):
        address (str | Unset):
        postal_code (str | Unset):
        city (str | Unset):
        state (str | Unset):
        country (str | Unset): ISO 3166-1 Alpha-3 code
        currency (str | Unset): ISO 4217 code
        allow_api (AccountBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        allow_gui (AccountBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        roles (CreateSubaccountRequestSubAccountRoles | Unset):
        labels (list[AccountLabel] | Unset):
        ip_filters (CreateSubaccountRequestSubAccountIpFilters | Unset):
        server_access (CreateSubaccountRequestSubAccountServerAccess | Unset):
        storage_access (CreateSubaccountRequestSubAccountStorageAccess | Unset):
        network_access (CreateSubaccountRequestSubAccountNetworkAccess | Unset):
        tag_access (CreateSubaccountRequestSubAccountTagAccess | Unset):
        enable_3rd_party_services (AccountBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
    """

    username: str
    email: str
    phone: str
    language: str
    timezone: str
    password: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    company: str | Unset = UNSET
    vat_number: str | Unset = UNSET
    address: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    country: str | Unset = UNSET
    currency: str | Unset = UNSET
    allow_api: AccountBooleanYesno | Unset = UNSET
    allow_gui: AccountBooleanYesno | Unset = UNSET
    roles: CreateSubaccountRequestSubAccountRoles | Unset = UNSET
    labels: list[AccountLabel] | Unset = UNSET
    ip_filters: CreateSubaccountRequestSubAccountIpFilters | Unset = UNSET
    server_access: CreateSubaccountRequestSubAccountServerAccess | Unset = UNSET
    storage_access: CreateSubaccountRequestSubAccountStorageAccess | Unset = UNSET
    network_access: CreateSubaccountRequestSubAccountNetworkAccess | Unset = UNSET
    tag_access: CreateSubaccountRequestSubAccountTagAccess | Unset = UNSET
    enable_3rd_party_services: AccountBooleanYesno | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        email = self.email

        phone = self.phone

        language = self.language

        timezone = self.timezone

        password = self.password

        first_name = self.first_name

        last_name = self.last_name

        company = self.company

        vat_number = self.vat_number

        address = self.address

        postal_code = self.postal_code

        city = self.city

        state = self.state

        country = self.country

        currency = self.currency

        allow_api: str | Unset = UNSET
        if not isinstance(self.allow_api, Unset):
            allow_api = self.allow_api.value

        allow_gui: str | Unset = UNSET
        if not isinstance(self.allow_gui, Unset):
            allow_gui = self.allow_gui.value

        roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        ip_filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_filters, Unset):
            ip_filters = self.ip_filters.to_dict()

        server_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_access, Unset):
            server_access = self.server_access.to_dict()

        storage_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_access, Unset):
            storage_access = self.storage_access.to_dict()

        network_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_access, Unset):
            network_access = self.network_access.to_dict()

        tag_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_access, Unset):
            tag_access = self.tag_access.to_dict()

        enable_3rd_party_services: str | Unset = UNSET
        if not isinstance(self.enable_3rd_party_services, Unset):
            enable_3rd_party_services = self.enable_3rd_party_services.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
                "email": email,
                "phone": phone,
                "language": language,
                "timezone": timezone,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if vat_number is not UNSET:
            field_dict["vat_number"] = vat_number
        if address is not UNSET:
            field_dict["address"] = address
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if currency is not UNSET:
            field_dict["currency"] = currency
        if allow_api is not UNSET:
            field_dict["allow_api"] = allow_api
        if allow_gui is not UNSET:
            field_dict["allow_gui"] = allow_gui
        if roles is not UNSET:
            field_dict["roles"] = roles
        if labels is not UNSET:
            field_dict["labels"] = labels
        if ip_filters is not UNSET:
            field_dict["ip_filters"] = ip_filters
        if server_access is not UNSET:
            field_dict["server_access"] = server_access
        if storage_access is not UNSET:
            field_dict["storage_access"] = storage_access
        if network_access is not UNSET:
            field_dict["network_access"] = network_access
        if tag_access is not UNSET:
            field_dict["tag_access"] = tag_access
        if enable_3rd_party_services is not UNSET:
            field_dict["enable_3rd_party_services"] = enable_3rd_party_services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_label import AccountLabel  # noqa: PLC0415
        from ..models.create_subaccount_request_sub_account_ip_filters import (
            CreateSubaccountRequestSubAccountIpFilters,  # noqa: PLC0415
        )
        from ..models.create_subaccount_request_sub_account_network_access import (
            CreateSubaccountRequestSubAccountNetworkAccess,  # noqa: PLC0415
        )
        from ..models.create_subaccount_request_sub_account_roles import (
            CreateSubaccountRequestSubAccountRoles,  # noqa: PLC0415
        )
        from ..models.create_subaccount_request_sub_account_server_access import (
            CreateSubaccountRequestSubAccountServerAccess,  # noqa: PLC0415
        )
        from ..models.create_subaccount_request_sub_account_storage_access import (
            CreateSubaccountRequestSubAccountStorageAccess,  # noqa: PLC0415
        )
        from ..models.create_subaccount_request_sub_account_tag_access import (
            CreateSubaccountRequestSubAccountTagAccess,  # noqa: PLC0415
        )

        d = dict(src_dict)
        username = d.pop("username")

        email = d.pop("email")

        phone = d.pop("phone")

        language = d.pop("language")

        timezone = d.pop("timezone")

        password = d.pop("password", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        company = d.pop("company", UNSET)

        vat_number = d.pop("vat_number", UNSET)

        address = d.pop("address", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        currency = d.pop("currency", UNSET)

        _allow_api = d.pop("allow_api", UNSET)
        allow_api: AccountBooleanYesno | Unset
        if isinstance(_allow_api, Unset):
            allow_api = UNSET
        else:
            allow_api = AccountBooleanYesno(_allow_api)

        _allow_gui = d.pop("allow_gui", UNSET)
        allow_gui: AccountBooleanYesno | Unset
        if isinstance(_allow_gui, Unset):
            allow_gui = UNSET
        else:
            allow_gui = AccountBooleanYesno(_allow_gui)

        _roles = d.pop("roles", UNSET)
        roles: CreateSubaccountRequestSubAccountRoles | Unset
        if isinstance(_roles, Unset):
            roles = UNSET
        else:
            roles = CreateSubaccountRequestSubAccountRoles.from_dict(_roles)

        _labels = d.pop("labels", UNSET)
        labels: list[AccountLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = AccountLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        _ip_filters = d.pop("ip_filters", UNSET)
        ip_filters: CreateSubaccountRequestSubAccountIpFilters | Unset
        if isinstance(_ip_filters, Unset):
            ip_filters = UNSET
        else:
            ip_filters = CreateSubaccountRequestSubAccountIpFilters.from_dict(_ip_filters)

        _server_access = d.pop("server_access", UNSET)
        server_access: CreateSubaccountRequestSubAccountServerAccess | Unset
        if isinstance(_server_access, Unset):
            server_access = UNSET
        else:
            server_access = CreateSubaccountRequestSubAccountServerAccess.from_dict(_server_access)

        _storage_access = d.pop("storage_access", UNSET)
        storage_access: CreateSubaccountRequestSubAccountStorageAccess | Unset
        if isinstance(_storage_access, Unset):
            storage_access = UNSET
        else:
            storage_access = CreateSubaccountRequestSubAccountStorageAccess.from_dict(_storage_access)

        _network_access = d.pop("network_access", UNSET)
        network_access: CreateSubaccountRequestSubAccountNetworkAccess | Unset
        if isinstance(_network_access, Unset):
            network_access = UNSET
        else:
            network_access = CreateSubaccountRequestSubAccountNetworkAccess.from_dict(_network_access)

        _tag_access = d.pop("tag_access", UNSET)
        tag_access: CreateSubaccountRequestSubAccountTagAccess | Unset
        if isinstance(_tag_access, Unset):
            tag_access = UNSET
        else:
            tag_access = CreateSubaccountRequestSubAccountTagAccess.from_dict(_tag_access)

        _enable_3rd_party_services = d.pop("enable_3rd_party_services", UNSET)
        enable_3rd_party_services: AccountBooleanYesno | Unset
        if isinstance(_enable_3rd_party_services, Unset):
            enable_3rd_party_services = UNSET
        else:
            enable_3rd_party_services = AccountBooleanYesno(_enable_3rd_party_services)

        create_subaccount_request_sub_account = cls(
            username=username,
            email=email,
            phone=phone,
            language=language,
            timezone=timezone,
            password=password,
            first_name=first_name,
            last_name=last_name,
            company=company,
            vat_number=vat_number,
            address=address,
            postal_code=postal_code,
            city=city,
            state=state,
            country=country,
            currency=currency,
            allow_api=allow_api,
            allow_gui=allow_gui,
            roles=roles,
            labels=labels,
            ip_filters=ip_filters,
            server_access=server_access,
            storage_access=storage_access,
            network_access=network_access,
            tag_access=tag_access,
            enable_3rd_party_services=enable_3rd_party_services,
        )

        return create_subaccount_request_sub_account
