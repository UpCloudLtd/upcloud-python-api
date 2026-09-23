from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSaml")


@_attrs_define
class DatabaseServicePropertiesOpensearchSaml:
    """
    Attributes:
        enabled (bool): Enables or disables SAML-based authentication for OpenSearch. When enabled, users can
            authenticate using SAML with an Identity Provider.
        idp_entity_id (str): The unique identifier for the Identity Provider (IdP) entity that is used for SAML
            authentication. This value is typically provided by the IdP.
        idp_metadata_url (str): The URL of the SAML metadata for the Identity Provider (IdP). This is used to configure
            SAML-based authentication with the IdP.
        sp_entity_id (str): The unique identifier for the Service Provider (SP) entity that is used for SAML
            authentication. This value is typically provided by the SP.
        idp_pemtrustedcas_content (None | str | Unset): This parameter specifies the PEM-encoded root certificate
            authority (CA) content for the SAML identity provider (IdP) server verification. The root CA content is used to
            verify the SSL/TLS certificate presented by the server.
        roles_key (None | str | Unset): Optional. Specifies the attribute in the SAML response where role information is
            stored, if available. Role attributes are not required for SAML authentication, but can be included in SAML
            assertions by most Identity Providers (IdPs) to determine user access levels or permissions.
        subject_key (None | str | Unset): Optional. Specifies the attribute in the SAML response where the subject
            identifier is stored. If not configured, the NameID attribute is used by default.
    """

    enabled: bool
    idp_entity_id: str
    idp_metadata_url: str
    sp_entity_id: str
    idp_pemtrustedcas_content: None | str | Unset = UNSET
    roles_key: None | str | Unset = UNSET
    subject_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        idp_entity_id = self.idp_entity_id

        idp_metadata_url = self.idp_metadata_url

        sp_entity_id = self.sp_entity_id

        idp_pemtrustedcas_content: None | str | Unset
        if isinstance(self.idp_pemtrustedcas_content, Unset):
            idp_pemtrustedcas_content = UNSET
        else:
            idp_pemtrustedcas_content = self.idp_pemtrustedcas_content

        roles_key: None | str | Unset
        if isinstance(self.roles_key, Unset):
            roles_key = UNSET
        else:
            roles_key = self.roles_key

        subject_key: None | str | Unset
        if isinstance(self.subject_key, Unset):
            subject_key = UNSET
        else:
            subject_key = self.subject_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "idp_entity_id": idp_entity_id,
                "idp_metadata_url": idp_metadata_url,
                "sp_entity_id": sp_entity_id,
            }
        )
        if idp_pemtrustedcas_content is not UNSET:
            field_dict["idp_pemtrustedcas_content"] = idp_pemtrustedcas_content
        if roles_key is not UNSET:
            field_dict["roles_key"] = roles_key
        if subject_key is not UNSET:
            field_dict["subject_key"] = subject_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        idp_entity_id = d.pop("idp_entity_id")

        idp_metadata_url = d.pop("idp_metadata_url")

        sp_entity_id = d.pop("sp_entity_id")

        def _parse_idp_pemtrustedcas_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idp_pemtrustedcas_content = _parse_idp_pemtrustedcas_content(d.pop("idp_pemtrustedcas_content", UNSET))

        def _parse_roles_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roles_key = _parse_roles_key(d.pop("roles_key", UNSET))

        def _parse_subject_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_key = _parse_subject_key(d.pop("subject_key", UNSET))

        database_service_properties_opensearch_saml = cls(
            enabled=enabled,
            idp_entity_id=idp_entity_id,
            idp_metadata_url=idp_metadata_url,
            sp_entity_id=sp_entity_id,
            idp_pemtrustedcas_content=idp_pemtrustedcas_content,
            roles_key=roles_key,
            subject_key=subject_key,
        )

        return database_service_properties_opensearch_saml
