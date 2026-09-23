from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.partner_error_400_address_invalid import PartnerError400AddressInvalid
    from ..models.partner_error_400_city_invalid import PartnerError400CityInvalid
    from ..models.partner_error_400_company_invalid import PartnerError400CompanyInvalid
    from ..models.partner_error_400_country_invalid import PartnerError400CountryInvalid
    from ..models.partner_error_400_country_missing import PartnerError400CountryMissing
    from ..models.partner_error_400_email_invalid import PartnerError400EmailInvalid
    from ..models.partner_error_400_email_missing import PartnerError400EmailMissing
    from ..models.partner_error_400_first_name_invalid import PartnerError400FirstNameInvalid
    from ..models.partner_error_400_first_name_missing import PartnerError400FirstNameMissing
    from ..models.partner_error_400_last_name_invalid import PartnerError400LastNameInvalid
    from ..models.partner_error_400_last_name_missing import PartnerError400LastNameMissing
    from ..models.partner_error_400_password_invalid import PartnerError400PasswordInvalid
    from ..models.partner_error_400_password_missing import PartnerError400PasswordMissing
    from ..models.partner_error_400_phone_invalid import PartnerError400PhoneInvalid
    from ..models.partner_error_400_phone_missing import PartnerError400PhoneMissing
    from ..models.partner_error_400_postal_code_invalid import PartnerError400PostalCodeInvalid
    from ..models.partner_error_400_postal_code_missing import PartnerError400PostalCodeMissing


T = TypeVar("T", bound="PartnerError400")


@_attrs_define
class PartnerError400:
    """400 Bad Request errors for partner account creation.

    Example:
        {'error': {'error_code': 'EMAIL_INVALID', 'error_message': 'The attribute email has an invalid value.'}}

    Attributes:
        error (PartnerError400AddressInvalid | PartnerError400CityInvalid | PartnerError400CompanyInvalid |
            PartnerError400CountryInvalid | PartnerError400CountryMissing | PartnerError400EmailInvalid |
            PartnerError400EmailMissing | PartnerError400FirstNameInvalid | PartnerError400FirstNameMissing |
            PartnerError400LastNameInvalid | PartnerError400LastNameMissing | PartnerError400PasswordInvalid |
            PartnerError400PasswordMissing | PartnerError400PhoneInvalid | PartnerError400PhoneMissing |
            PartnerError400PostalCodeInvalid | PartnerError400PostalCodeMissing):  Example: {'error_code': 'EMAIL_INVALID',
            'error_message': 'The attribute email has an invalid value.'}.
    """

    error: (
        PartnerError400AddressInvalid
        | PartnerError400CityInvalid
        | PartnerError400CompanyInvalid
        | PartnerError400CountryInvalid
        | PartnerError400CountryMissing
        | PartnerError400EmailInvalid
        | PartnerError400EmailMissing
        | PartnerError400FirstNameInvalid
        | PartnerError400FirstNameMissing
        | PartnerError400LastNameInvalid
        | PartnerError400LastNameMissing
        | PartnerError400PasswordInvalid
        | PartnerError400PasswordMissing
        | PartnerError400PhoneInvalid
        | PartnerError400PhoneMissing
        | PartnerError400PostalCodeInvalid
        | PartnerError400PostalCodeMissing
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_error_400_address_invalid import PartnerError400AddressInvalid  # noqa: PLC0415
        from ..models.partner_error_400_city_invalid import PartnerError400CityInvalid  # noqa: PLC0415
        from ..models.partner_error_400_company_invalid import PartnerError400CompanyInvalid  # noqa: PLC0415
        from ..models.partner_error_400_country_invalid import PartnerError400CountryInvalid  # noqa: PLC0415
        from ..models.partner_error_400_country_missing import PartnerError400CountryMissing  # noqa: PLC0415
        from ..models.partner_error_400_email_invalid import PartnerError400EmailInvalid  # noqa: PLC0415
        from ..models.partner_error_400_email_missing import PartnerError400EmailMissing  # noqa: PLC0415
        from ..models.partner_error_400_first_name_invalid import PartnerError400FirstNameInvalid  # noqa: PLC0415
        from ..models.partner_error_400_first_name_missing import PartnerError400FirstNameMissing  # noqa: PLC0415
        from ..models.partner_error_400_last_name_invalid import PartnerError400LastNameInvalid  # noqa: PLC0415
        from ..models.partner_error_400_last_name_missing import PartnerError400LastNameMissing  # noqa: PLC0415
        from ..models.partner_error_400_password_invalid import PartnerError400PasswordInvalid  # noqa: PLC0415
        from ..models.partner_error_400_password_missing import PartnerError400PasswordMissing  # noqa: PLC0415
        from ..models.partner_error_400_phone_invalid import PartnerError400PhoneInvalid  # noqa: PLC0415
        from ..models.partner_error_400_phone_missing import PartnerError400PhoneMissing  # noqa: PLC0415
        from ..models.partner_error_400_postal_code_invalid import PartnerError400PostalCodeInvalid  # noqa: PLC0415

        error: dict[str, Any]
        if isinstance(self.error, PartnerError400AddressInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400CityInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400CompanyInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400CountryInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400CountryMissing):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400EmailInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400EmailMissing):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400FirstNameInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400FirstNameMissing):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400LastNameInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400LastNameMissing):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400PasswordInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400PasswordMissing):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400PhoneInvalid):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400PhoneMissing):
            error = self.error.to_dict()
        elif isinstance(self.error, PartnerError400PostalCodeInvalid):
            error = self.error.to_dict()
        else:
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
        from ..models.partner_error_400_address_invalid import PartnerError400AddressInvalid  # noqa: PLC0415
        from ..models.partner_error_400_city_invalid import PartnerError400CityInvalid  # noqa: PLC0415
        from ..models.partner_error_400_company_invalid import PartnerError400CompanyInvalid  # noqa: PLC0415
        from ..models.partner_error_400_country_invalid import PartnerError400CountryInvalid  # noqa: PLC0415
        from ..models.partner_error_400_country_missing import PartnerError400CountryMissing  # noqa: PLC0415
        from ..models.partner_error_400_email_invalid import PartnerError400EmailInvalid  # noqa: PLC0415
        from ..models.partner_error_400_email_missing import PartnerError400EmailMissing  # noqa: PLC0415
        from ..models.partner_error_400_first_name_invalid import PartnerError400FirstNameInvalid  # noqa: PLC0415
        from ..models.partner_error_400_first_name_missing import PartnerError400FirstNameMissing  # noqa: PLC0415
        from ..models.partner_error_400_last_name_invalid import PartnerError400LastNameInvalid  # noqa: PLC0415
        from ..models.partner_error_400_last_name_missing import PartnerError400LastNameMissing  # noqa: PLC0415
        from ..models.partner_error_400_password_invalid import PartnerError400PasswordInvalid  # noqa: PLC0415
        from ..models.partner_error_400_password_missing import PartnerError400PasswordMissing  # noqa: PLC0415
        from ..models.partner_error_400_phone_invalid import PartnerError400PhoneInvalid  # noqa: PLC0415
        from ..models.partner_error_400_phone_missing import PartnerError400PhoneMissing  # noqa: PLC0415
        from ..models.partner_error_400_postal_code_invalid import PartnerError400PostalCodeInvalid  # noqa: PLC0415
        from ..models.partner_error_400_postal_code_missing import PartnerError400PostalCodeMissing  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_error(
            data: object,
        ) -> (
            PartnerError400AddressInvalid
            | PartnerError400CityInvalid
            | PartnerError400CompanyInvalid
            | PartnerError400CountryInvalid
            | PartnerError400CountryMissing
            | PartnerError400EmailInvalid
            | PartnerError400EmailMissing
            | PartnerError400FirstNameInvalid
            | PartnerError400FirstNameMissing
            | PartnerError400LastNameInvalid
            | PartnerError400LastNameMissing
            | PartnerError400PasswordInvalid
            | PartnerError400PasswordMissing
            | PartnerError400PhoneInvalid
            | PartnerError400PhoneMissing
            | PartnerError400PostalCodeInvalid
            | PartnerError400PostalCodeMissing
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = PartnerError400AddressInvalid.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_1 = PartnerError400CityInvalid.from_dict(data)

                return error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_2 = PartnerError400CompanyInvalid.from_dict(data)

                return error_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_3 = PartnerError400CountryInvalid.from_dict(data)

                return error_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_4 = PartnerError400CountryMissing.from_dict(data)

                return error_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_5 = PartnerError400EmailInvalid.from_dict(data)

                return error_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_6 = PartnerError400EmailMissing.from_dict(data)

                return error_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_7 = PartnerError400FirstNameInvalid.from_dict(data)

                return error_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_8 = PartnerError400FirstNameMissing.from_dict(data)

                return error_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_9 = PartnerError400LastNameInvalid.from_dict(data)

                return error_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_10 = PartnerError400LastNameMissing.from_dict(data)

                return error_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_11 = PartnerError400PasswordInvalid.from_dict(data)

                return error_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_12 = PartnerError400PasswordMissing.from_dict(data)

                return error_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_13 = PartnerError400PhoneInvalid.from_dict(data)

                return error_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_14 = PartnerError400PhoneMissing.from_dict(data)

                return error_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_15 = PartnerError400PostalCodeInvalid.from_dict(data)

                return error_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            error_type_16 = PartnerError400PostalCodeMissing.from_dict(data)

            return error_type_16

        error = _parse_error(d.pop("error"))

        partner_error_400 = cls(
            error=error,
        )

        return partner_error_400
