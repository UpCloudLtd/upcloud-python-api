from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_network_request import CreateNetworkRequest
from ...models.network import Network
from ...models.network_error import NetworkError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateNetworkRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/network",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Network | NetworkError:
    if response.status_code == 201:
        response_201 = Network.from_dict(response.json())

        return response_201

    response_default = NetworkError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Network | NetworkError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNetworkRequest | Unset = UNSET,
) -> Response[Network | NetworkError]:
    """Create SDN network

     Creates a new SDN private network that cloud servers from the same zone can be attached to.

    Args:
        body (CreateNetworkRequest | Unset): Request schema for creating a network Example:
            {'network': {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2', 'ip_networks':
            {'ip_network': [{'family': 'IPv4', 'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Network | NetworkError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNetworkRequest | Unset = UNSET,
) -> Network | NetworkError | None:
    """Create SDN network

     Creates a new SDN private network that cloud servers from the same zone can be attached to.

    Args:
        body (CreateNetworkRequest | Unset): Request schema for creating a network Example:
            {'network': {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2', 'ip_networks':
            {'ip_network': [{'family': 'IPv4', 'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Network | NetworkError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNetworkRequest | Unset = UNSET,
) -> Response[Network | NetworkError]:
    """Create SDN network

     Creates a new SDN private network that cloud servers from the same zone can be attached to.

    Args:
        body (CreateNetworkRequest | Unset): Request schema for creating a network Example:
            {'network': {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2', 'ip_networks':
            {'ip_network': [{'family': 'IPv4', 'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Network | NetworkError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateNetworkRequest | Unset = UNSET,
) -> Network | NetworkError | None:
    """Create SDN network

     Creates a new SDN private network that cloud servers from the same zone can be attached to.

    Args:
        body (CreateNetworkRequest | Unset): Request schema for creating a network Example:
            {'network': {'type': 'private', 'name': 'backend-net', 'zone': 'fi-hel2', 'ip_networks':
            {'ip_network': [{'family': 'IPv4', 'address': '10.0.0.0/24', 'dhcp': 'yes'}]}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Network | NetworkError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
