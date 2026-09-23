from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ip_address_error import IpAddressError
from ...models.ip_address_request import IpAddressRequest
from ...models.modify_ip_address_request_v10 import ModifyIpAddressRequestV10
from ...types import UNSET, Response, Unset


def _get_kwargs(
    address: str,
    *,
    body: ModifyIpAddressRequestV10 | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/ip_address/{address}".format(
            address=quote(str(address), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IpAddressError | IpAddressRequest:
    if response.status_code == 202:
        response_202 = IpAddressRequest.from_dict(response.json())

        return response_202

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
    address: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyIpAddressRequestV10 | Unset = UNSET,
) -> Response[IpAddressError | IpAddressRequest]:
    """Modify IP address

     Modifies attributes of a specific IP address.

    Args:
        address (str): IP address Example: 10.0.0.20.
        body (ModifyIpAddressRequestV10 | Unset): Request schema for modifying an IP address
            Example: {'ip_address': {'ptr_record': 'host.example.com'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IpAddressError | IpAddressRequest]
    """

    kwargs = _get_kwargs(
        address=address,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyIpAddressRequestV10 | Unset = UNSET,
) -> IpAddressError | IpAddressRequest | None:
    """Modify IP address

     Modifies attributes of a specific IP address.

    Args:
        address (str): IP address Example: 10.0.0.20.
        body (ModifyIpAddressRequestV10 | Unset): Request schema for modifying an IP address
            Example: {'ip_address': {'ptr_record': 'host.example.com'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IpAddressError | IpAddressRequest
    """

    return sync_detailed(
        address=address,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyIpAddressRequestV10 | Unset = UNSET,
) -> Response[IpAddressError | IpAddressRequest]:
    """Modify IP address

     Modifies attributes of a specific IP address.

    Args:
        address (str): IP address Example: 10.0.0.20.
        body (ModifyIpAddressRequestV10 | Unset): Request schema for modifying an IP address
            Example: {'ip_address': {'ptr_record': 'host.example.com'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IpAddressError | IpAddressRequest]
    """

    kwargs = _get_kwargs(
        address=address,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModifyIpAddressRequestV10 | Unset = UNSET,
) -> IpAddressError | IpAddressRequest | None:
    """Modify IP address

     Modifies attributes of a specific IP address.

    Args:
        address (str): IP address Example: 10.0.0.20.
        body (ModifyIpAddressRequestV10 | Unset): Request schema for modifying an IP address
            Example: {'ip_address': {'ptr_record': 'host.example.com'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IpAddressError | IpAddressRequest
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
            body=body,
        )
    ).parsed
