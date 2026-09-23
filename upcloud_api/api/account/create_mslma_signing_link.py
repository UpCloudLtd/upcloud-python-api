from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_create_ms_lma_signing_link_response import AccountCreateMsLmaSigningLinkResponse
from ...models.account_error import AccountError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/account/ms_lma",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountCreateMsLmaSigningLinkResponse | AccountError:
    if response.status_code == 201:
        response_201 = AccountCreateMsLmaSigningLinkResponse.from_dict(response.json())

        return response_201

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountCreateMsLmaSigningLinkResponse | AccountError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountCreateMsLmaSigningLinkResponse | AccountError]:
    """Create Microsoft LMA signing link

     Create a new Microsoft LMA signing link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountCreateMsLmaSigningLinkResponse | AccountError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> AccountCreateMsLmaSigningLinkResponse | AccountError | None:
    """Create Microsoft LMA signing link

     Create a new Microsoft LMA signing link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountCreateMsLmaSigningLinkResponse | AccountError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountCreateMsLmaSigningLinkResponse | AccountError]:
    """Create Microsoft LMA signing link

     Create a new Microsoft LMA signing link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountCreateMsLmaSigningLinkResponse | AccountError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> AccountCreateMsLmaSigningLinkResponse | AccountError | None:
    """Create Microsoft LMA signing link

     Create a new Microsoft LMA signing link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountCreateMsLmaSigningLinkResponse | AccountError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
