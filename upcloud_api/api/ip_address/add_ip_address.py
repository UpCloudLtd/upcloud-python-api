from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.add_ip_address_request import AddIpAddressRequest
from ...models.ip_address_error import IpAddressError
from ...models.ip_address_request import IpAddressRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AddIpAddressRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/ip_address",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IpAddressError | IpAddressRequest:
    if response.status_code == 201:
        response_201 = IpAddressRequest.from_dict(response.json())

        return response_201

    response_default = IpAddressError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IpAddressError | IpAddressRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddIpAddressRequest | Unset = UNSET,
) -> Response[IpAddressError | IpAddressRequest]:
    """Add an IP address

     Adds a new IP address.

    Args:
        body (AddIpAddressRequest | Unset): Schema for adding an IP address to a server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IpAddressError | IpAddressRequest]
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
    body: AddIpAddressRequest | Unset = UNSET,
) -> IpAddressError | IpAddressRequest | None:
    """Add an IP address

     Adds a new IP address.

    Args:
        body (AddIpAddressRequest | Unset): Schema for adding an IP address to a server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IpAddressError | IpAddressRequest
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddIpAddressRequest | Unset = UNSET,
) -> Response[IpAddressError | IpAddressRequest]:
    """Add an IP address

     Adds a new IP address.

    Args:
        body (AddIpAddressRequest | Unset): Schema for adding an IP address to a server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IpAddressError | IpAddressRequest]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddIpAddressRequest | Unset = UNSET,
) -> IpAddressError | IpAddressRequest | None:
    """Add an IP address

     Adds a new IP address.

    Args:
        body (AddIpAddressRequest | Unset): Schema for adding an IP address to a server

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IpAddressError | IpAddressRequest
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
