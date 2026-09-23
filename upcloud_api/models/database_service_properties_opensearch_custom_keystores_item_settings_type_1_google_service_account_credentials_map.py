from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap"
)


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap:
    """
    Attributes:
        client_email (str):  Example: my-service-account@some-my-project.iam.gserviceaccount.com.
        client_id (str):  Example: 103654484443722885992.
        private_key (str):  Example: -----BEGIN PRIVATE KEY-----
            ...
            -----END PRIVATE KEY-----
            .
        private_key_id (str):  Example: 5fdeb02a11ddf081930ac3ac60bf376a0aef8fad.
        type_ (str): Always service_account for credentials created in Gcloud console or CLI Example: service_account.
        auth_provider_x509_cert_url (str | Unset):  Example: https://www.googleapis.com/oauth2/v1/certs.
        auth_uri (str | Unset):  Example: https://accounts.google.com/o/oauth2/auth.
        client_x509_cert_url (str | Unset):  Example: https://www.googleapis.com/robot/v1/metadata/x509/my-service-
            account%40some-my-project.iam.gserviceaccount.com.
        hmac_access_id (str | Unset): The access ID for HMAC authentication with Google Cloud Storage
        hmac_secret (str | Unset): The secret key for HMAC authentication with Google Cloud Storage
        project_id (str | Unset):  Example: some-my-project.
        token_uri (str | Unset):  Example: https://accounts.google.com/o/oauth2/token.
        universe_domain (str | Unset): The universe domain. The default universe domain is googleapis.com. Example:
            {"universe_domain": "googleapis.com", ....
    """

    client_email: str
    client_id: str
    private_key: str
    private_key_id: str
    type_: str
    auth_provider_x509_cert_url: str | Unset = UNSET
    auth_uri: str | Unset = UNSET
    client_x509_cert_url: str | Unset = UNSET
    hmac_access_id: str | Unset = UNSET
    hmac_secret: str | Unset = UNSET
    project_id: str | Unset = UNSET
    token_uri: str | Unset = UNSET
    universe_domain: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_email = self.client_email

        client_id = self.client_id

        private_key = self.private_key

        private_key_id = self.private_key_id

        type_ = self.type_

        auth_provider_x509_cert_url = self.auth_provider_x509_cert_url

        auth_uri = self.auth_uri

        client_x509_cert_url = self.client_x509_cert_url

        hmac_access_id = self.hmac_access_id

        hmac_secret = self.hmac_secret

        project_id = self.project_id

        token_uri = self.token_uri

        universe_domain = self.universe_domain

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "client_email": client_email,
                "client_id": client_id,
                "private_key": private_key,
                "private_key_id": private_key_id,
                "type": type_,
            }
        )
        if auth_provider_x509_cert_url is not UNSET:
            field_dict["auth_provider_x509_cert_url"] = auth_provider_x509_cert_url
        if auth_uri is not UNSET:
            field_dict["auth_uri"] = auth_uri
        if client_x509_cert_url is not UNSET:
            field_dict["client_x509_cert_url"] = client_x509_cert_url
        if hmac_access_id is not UNSET:
            field_dict["hmac_access_id"] = hmac_access_id
        if hmac_secret is not UNSET:
            field_dict["hmac_secret"] = hmac_secret
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if token_uri is not UNSET:
            field_dict["token_uri"] = token_uri
        if universe_domain is not UNSET:
            field_dict["universe_domain"] = universe_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_email = d.pop("client_email")

        client_id = d.pop("client_id")

        private_key = d.pop("private_key")

        private_key_id = d.pop("private_key_id")

        type_ = d.pop("type")

        auth_provider_x509_cert_url = d.pop("auth_provider_x509_cert_url", UNSET)

        auth_uri = d.pop("auth_uri", UNSET)

        client_x509_cert_url = d.pop("client_x509_cert_url", UNSET)

        hmac_access_id = d.pop("hmac_access_id", UNSET)

        hmac_secret = d.pop("hmac_secret", UNSET)

        project_id = d.pop("project_id", UNSET)

        token_uri = d.pop("token_uri", UNSET)

        universe_domain = d.pop("universe_domain", UNSET)

        database_service_properties_opensearch_custom_keystores_item_settings_type_1_google_service_account_credentials_map = cls(
            client_email=client_email,
            client_id=client_id,
            private_key=private_key,
            private_key_id=private_key_id,
            type_=type_,
            auth_provider_x509_cert_url=auth_provider_x509_cert_url,
            auth_uri=auth_uri,
            client_x509_cert_url=client_x509_cert_url,
            hmac_access_id=hmac_access_id,
            hmac_secret=hmac_secret,
            project_id=project_id,
            token_uri=token_uri,
            universe_domain=universe_domain,
        )

        return database_service_properties_opensearch_custom_keystores_item_settings_type_1_google_service_account_credentials_map
