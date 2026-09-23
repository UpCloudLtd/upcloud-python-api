from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.currency_currencies import CurrencyCurrencies
from ...models.currency_error import CurrencyError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/currency",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CurrencyCurrencies | CurrencyError:
    if response.status_code == 200:
        response_200 = CurrencyCurrencies.from_dict(response.json())

        return response_200

    response_default = CurrencyError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CurrencyCurrencies | CurrencyError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CurrencyCurrencies | CurrencyError]:
    """List currencies

     Retrieves a list of supported currencies and their exchange rates relative to the account credit
    currency.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrencyCurrencies | CurrencyError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> CurrencyCurrencies | CurrencyError | None:
    """List currencies

     Retrieves a list of supported currencies and their exchange rates relative to the account credit
    currency.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrencyCurrencies | CurrencyError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[CurrencyCurrencies | CurrencyError]:
    """List currencies

     Retrieves a list of supported currencies and their exchange rates relative to the account credit
    currency.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrencyCurrencies | CurrencyError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> CurrencyCurrencies | CurrencyError | None:
    """List currencies

     Retrieves a list of supported currencies and their exchange rates relative to the account credit
    currency.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrencyCurrencies | CurrencyError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
