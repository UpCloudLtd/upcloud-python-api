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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/kubernetes/{uuid}/authentication/{name}".format(
            uuid=quote(str(uuid), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KubernetesAuthenticationIssuerConfig | KubernetesError:
    if response.status_code == 200:
        response_200 = KubernetesAuthenticationIssuerConfig.from_dict(response.json())

        return response_200

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
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    """Get a cluster authentication entry

    Args:
        uuid (UUID): UUID
        name (str): Name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesAuthenticationIssuerConfig | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
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
) -> KubernetesAuthenticationIssuerConfig | KubernetesError | None:
    """Get a cluster authentication entry

    Args:
        uuid (UUID): UUID
        name (str): Name

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
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[KubernetesAuthenticationIssuerConfig | KubernetesError]:
    """Get a cluster authentication entry

    Args:
        uuid (UUID): UUID
        name (str): Name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesAuthenticationIssuerConfig | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> KubernetesAuthenticationIssuerConfig | KubernetesError | None:
    """Get a cluster authentication entry

    Args:
        uuid (UUID): UUID
        name (str): Name

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
        )
    ).parsed
