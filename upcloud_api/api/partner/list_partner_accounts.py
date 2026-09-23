from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.partner_account import PartnerAccount
from ...models.partner_error import PartnerError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/partner/accounts",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PartnerError | list[PartnerAccount]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemaspartner_accounts_item_data in _response_200:
            componentsschemaspartner_accounts_item = PartnerAccount.from_dict(
                componentsschemaspartner_accounts_item_data
            )

            response_200.append(componentsschemaspartner_accounts_item)

        return response_200

    response_default = PartnerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PartnerError | list[PartnerAccount]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PartnerError | list[PartnerAccount]]:
    """Get account list

     Returns list of accounts associated with the partner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerError | list[PartnerAccount]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> PartnerError | list[PartnerAccount] | None:
    """Get account list

     Returns list of accounts associated with the partner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerError | list[PartnerAccount]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PartnerError | list[PartnerAccount]]:
    """Get account list

     Returns list of accounts associated with the partner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerError | list[PartnerAccount]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> PartnerError | list[PartnerAccount] | None:
    """Get account list

     Returns list of accounts associated with the partner.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerError | list[PartnerAccount]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
