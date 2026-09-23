from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_authentication_issuer_config import KubernetesAuthenticationIssuerConfig
from ...models.kubernetes_error import KubernetesError
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: KubernetesAuthenticationIssuerConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/kubernetes/{uuid}/authentication".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KubernetesAuthenticationIssuerConfig | KubernetesError:
    if response.status_code == 201:
        response_201 = KubernetesAuthenticationIssuerConfig.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = KubernetesError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = KubernetesError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = KubernetesError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = KubernetesError.from_dict(response.json())

        return response_409

    response_default = KubernetesError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    """Create a cluster authentication entry

     Creates a new OIDC authentication issuer configuration. The new entry is validated together with the
    cluster's existing entries before being applied. Fails if an entry with the same name already
    exists.

    Args:
        uuid (UUID): UUID
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesAuthenticationIssuerConfig | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> KubernetesAuthenticationIssuerConfig | KubernetesError | None:
    """Create a cluster authentication entry

     Creates a new OIDC authentication issuer configuration. The new entry is validated together with the
    cluster's existing entries before being applied. Fails if an entry with the same name already
    exists.

    Args:
        uuid (UUID): UUID
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesAuthenticationIssuerConfig | KubernetesError
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    """Create a cluster authentication entry

     Creates a new OIDC authentication issuer configuration. The new entry is validated together with the
    cluster's existing entries before being applied. Fails if an entry with the same name already
    exists.

    Args:
        uuid (UUID): UUID
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesAuthenticationIssuerConfig | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> KubernetesAuthenticationIssuerConfig | KubernetesError | None:
    """Create a cluster authentication entry

     Creates a new OIDC authentication issuer configuration. The new entry is validated together with the
    cluster's existing entries before being applied. Fails if an entry with the same name already
    exists.

    Args:
        uuid (UUID): UUID
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesAuthenticationIssuerConfig | KubernetesError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
