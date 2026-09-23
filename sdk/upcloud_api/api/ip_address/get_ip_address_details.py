from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ip_address_error import IpAddressError
from ...models.ip_address_response import IpAddressResponse
from ...types import Response


def _get_kwargs(
    address: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/ip_address/{address}".format(
            address=quote(str(address), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IpAddressError | IpAddressResponse:
    if response.status_code == 200:
        response_200 = IpAddressResponse.from_dict(response.json())

        return response_200

    response_default = IpAddressError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IpAddressError | IpAddressResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IpAddressError | IpAddressResponse]:
    """Get IP address

     Retrieves details of a specific IP address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IpAddressError | IpAddressResponse]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: AuthenticatedClient | Client,
) -> IpAddressError | IpAddressResponse | None:
    """Get IP address

     Retrieves details of a specific IP address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IpAddressError | IpAddressResponse
    """

    return sync_detailed(
        address=address,
        client=client,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[IpAddressError | IpAddressResponse]:
    """Get IP address

     Retrieves details of a specific IP address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IpAddressError | IpAddressResponse]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: AuthenticatedClient | Client,
) -> IpAddressError | IpAddressResponse | None:
    """Get IP address

     Retrieves details of a specific IP address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IpAddressError | IpAddressResponse
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
        )
    ).parsed
