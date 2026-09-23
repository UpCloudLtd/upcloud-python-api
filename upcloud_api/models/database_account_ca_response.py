from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseAccountCaResponse")


@_attrs_define
class DatabaseAccountCaResponse:
    """Response schema for account CA

    Attributes:
        certificate (str | Unset): Name of the CA Example: -----BEGIN CERTIFICATE-----
            axxxxxxxxxxxxx+tkP9Uh9+PxxxxxcNAQEM
            BQAwOjE4MDYGA1UEAwwvZWYzMTc1xxxxxxxxxx0YjM2OWIz
            M2RkIFByb2plY3QgQ0EwHhcNMjEwMzMwMDgxNDU0WhcNMzEwMzI4MDgxNDU0WjA6
            MTgwNgYDVQQDDC9lZjMxNzU1NC1lNzYzLTQ5ZjUtODI4Ni1lZDRiMzY5YjMzZGQg
            UHJvamVjdCBDQTCCAaIwDQYJKoZIhvcNAQEBBQxxxxggGBAK1Vh4GR
            lfxPZ3Icw8E1WlS5+9rADOdrstYtL3oiHBqzljmjvKf1Vuu0LLHtszWrCElOvoZ4
            zhg6+yVIB9YcvTZJNU0BNlIilF0rafn/40pFjeKrtxxxxxxxxxxy48Hnk
            MAiqoRyJ6hGRpYmKVip2sbMEtI+X9xQahlhlTMLo9082gS2hI5nvmhDqRiOlly28
            twr2I/nbsIao8pIE19bdptKVqrv9x+O51O2JK7NlyjxnJVaHS9Tv6z1gG0GZgzYW
            kram1U8oTu72cjvGhMIBhgz7AlQ74PMtAub/eH4hipGU4LDZQiZ+9kCT+FCD9uAq
            Iq+ALiLPHTCaGiKTJYoerutgrmrz1HZp6RmxRc8Wk7MdPp8OHqSXUnewKSGlzEl3
            hlJ5UMOVQ+tSDffAuvA6phUS0mmm1xxxxxxxxxxxxxxxMcrVE8AjbF5nkieOV0r6hIwIDAQAB
            oz8wPTAdBgNVHQ4EFxxxxgQUHTUNeVDpSFx8fjq9xxxxxxxxFDnqn8xY0iAwDwYDVR0TBAgwBgEB
            /wIBADALBgNxxxxxxxxxxLtt8qOjsbvS
            YZtePpqZjx7NkmFdScc0LOBj6oXFetcJlhLQKzrguQDi/trt29sxjZZ5zLnQufnE
            s8IYtbclhDbF0qGG15oP8tYVRXfzKLHF4HfuMrdiyqzF/q6Qy0fVIiFWD7t1it8V
            PLqlk9oFDL7xUnsZOfYcqv8Ct+aWE7L73gJVgUkDHP+gkdGTWKYm4zzYTLfqh1Iu
            yivOjn+KSyjjtsJsOGUDZBkh215OMKPp4JpWQpgQeK6kjTnwuMwEYYFyhfu/z5wU
            wN7z7Ad39fyGmQzkGbFXtP0te4MFElOVSkiHaB4T4lTM6690st6+uIhFI1Qo/oAY
            30ybOpOTLF7FZxwY5Z+BTW27hytyECLkG3b4iKIqKsRIvlFkwKP8cfKjq7ImSbBG
            OJ8JBcraffygrLznbJ2979Y9yN+n+8wW0xxxxxxxxxxov24snxDmm6fAMoO1
            xBM7c2KZA5ZoZDefcz9e28r7xxxx==
            -----END CERTIFICATE-----
            .
    """

    certificate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate = self.certificate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate = d.pop("certificate", UNSET)

        database_account_ca_response = cls(
            certificate=certificate,
        )

        database_account_ca_response.additional_properties = d
        return database_account_ca_response

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
