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
    name: str,
    *,
    body: KubernetesAuthenticationIssuerConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/kubernetes/{uuid}/authentication/{name}".format(
            uuid=quote(str(uuid), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KubernetesAuthenticationIssuerConfig | KubernetesError:
    if response.status_code == 200:
        response_200 = KubernetesAuthenticationIssuerConfig.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = KubernetesError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = KubernetesError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = KubernetesError.from_dict(response.json())

        return response_404

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
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    """Update a cluster authentication entry

     Updates an existing OIDC authentication issuer configuration. The name in the path is authoritative.
    The updated entry is validated together with the cluster's other entries before being applied.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesAuthenticationIssuerConfig | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> KubernetesAuthenticationIssuerConfig | KubernetesError | None:
    """Update a cluster authentication entry

     Updates an existing OIDC authentication issuer configuration. The name in the path is authoritative.
    The updated entry is validated together with the cluster's other entries before being applied.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesAuthenticationIssuerConfig | KubernetesError
    """

    return sync_detailed(
        uuid=uuid,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    """Update a cluster authentication entry

     Updates an existing OIDC authentication issuer configuration. The name in the path is authoritative.
    The updated entry is validated together with the cluster's other entries before being applied.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesAuthenticationIssuerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesAuthenticationIssuerConfig | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesAuthenticationIssuerConfig,
) -> KubernetesAuthenticationIssuerConfig | KubernetesError | None:
    """Update a cluster authentication entry

     Updates an existing OIDC authentication issuer configuration. The name in the path is authoritative.
    The updated entry is validated together with the cluster's other entries before being applied.

    Args:
        uuid (UUID): UUID
        name (str): Name
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
            name=name,
            client=client,
            body=body,
        )
    ).parsed
