from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_create_interface_request import NetworkCreateInterfaceRequest
from ...models.network_error import NetworkError
from ...models.network_interface import NetworkInterface
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NetworkCreateInterfaceRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/network/interface",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NetworkError | NetworkInterface:
    if response.status_code == 201:
        response_201 = NetworkInterface.from_dict(response.json())

        return response_201

    response_default = NetworkError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NetworkError | NetworkInterface]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NetworkCreateInterfaceRequest | Unset = UNSET,
) -> Response[NetworkError | NetworkInterface]:
    """Create interface

     Creates a new network interface.

    Args:
        body (NetworkCreateInterfaceRequest | Unset): Request schema for creating a network
            interface Example: {'main_account_id': 123456, 'interface': {'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'source_ip_filtering': 'yes', 'bootable': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkError | NetworkInterface]
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
    body: NetworkCreateInterfaceRequest | Unset = UNSET,
) -> NetworkError | NetworkInterface | None:
    """Create interface

     Creates a new network interface.

    Args:
        body (NetworkCreateInterfaceRequest | Unset): Request schema for creating a network
            interface Example: {'main_account_id': 123456, 'interface': {'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'source_ip_filtering': 'yes', 'bootable': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkError | NetworkInterface
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NetworkCreateInterfaceRequest | Unset = UNSET,
) -> Response[NetworkError | NetworkInterface]:
    """Create interface

     Creates a new network interface.

    Args:
        body (NetworkCreateInterfaceRequest | Unset): Request schema for creating a network
            interface Example: {'main_account_id': 123456, 'interface': {'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'source_ip_filtering': 'yes', 'bootable': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkError | NetworkInterface]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NetworkCreateInterfaceRequest | Unset = UNSET,
) -> NetworkError | NetworkInterface | None:
    """Create interface

     Creates a new network interface.

    Args:
        body (NetworkCreateInterfaceRequest | Unset): Request schema for creating a network
            interface Example: {'main_account_id': 123456, 'interface': {'type': 'private', 'network':
            '8f6d1ec2-8f5e-4b67-8fcb-6fa9c1a8a001', 'source_ip_filtering': 'yes', 'bootable': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkError | NetworkInterface
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
