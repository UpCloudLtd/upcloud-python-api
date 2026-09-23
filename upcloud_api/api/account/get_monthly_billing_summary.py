from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_billing_summary_response import AccountBillingSummaryResponse
from ...models.account_error import AccountError
from ...types import Response


def _get_kwargs(
    year: str,
    month: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/account/billing_summary/{year}-{month}".format(
            year=quote(str(year), safe=""),
            month=quote(str(month), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountBillingSummaryResponse | AccountError:
    if response.status_code == 200:
        response_200 = AccountBillingSummaryResponse.from_dict(response.json())

        return response_200

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountBillingSummaryResponse | AccountError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountBillingSummaryResponse | AccountError]:
    """Get monthly billing summary

     Returns a billing summary for the specified month. The API user must have permission to read billing
    details. This endpoint is deprecated; use the monthly billing summary with resource details instead.

    Args:
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountBillingSummaryResponse | AccountError]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> AccountBillingSummaryResponse | AccountError | None:
    """Get monthly billing summary

     Returns a billing summary for the specified month. The API user must have permission to read billing
    details. This endpoint is deprecated; use the monthly billing summary with resource details instead.

    Args:
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountBillingSummaryResponse | AccountError
    """

    return sync_detailed(
        year=year,
        month=month,
        client=client,
    ).parsed


async def asyncio_detailed(
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountBillingSummaryResponse | AccountError]:
    """Get monthly billing summary

     Returns a billing summary for the specified month. The API user must have permission to read billing
    details. This endpoint is deprecated; use the monthly billing summary with resource details instead.

    Args:
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountBillingSummaryResponse | AccountError]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> AccountBillingSummaryResponse | AccountError | None:
    """Get monthly billing summary

     Returns a billing summary for the specified month. The API user must have permission to read billing
    details. This endpoint is deprecated; use the monthly billing summary with resource details instead.

    Args:
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountBillingSummaryResponse | AccountError
    """

    return (
        await asyncio_detailed(
            year=year,
            month=month,
            client=client,
        )
    ).parsed
