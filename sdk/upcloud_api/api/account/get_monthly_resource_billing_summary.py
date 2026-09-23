from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_error import AccountError
from ...models.account_resource_billing_summary_response import AccountResourceBillingSummaryResponse
from ...types import Response


def _get_kwargs(
    resource_id: str,
    year: str,
    month: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/account/resource_billing_summary/{resource_id}/{year}-{month}".format(
            resource_id=quote(str(resource_id), safe=""),
            year=quote(str(year), safe=""),
            month=quote(str(month), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountError | AccountResourceBillingSummaryResponse:
    if response.status_code == 200:
        response_200 = AccountResourceBillingSummaryResponse.from_dict(response.json())

        return response_200

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountError | AccountResourceBillingSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_id: str,
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountError | AccountResourceBillingSummaryResponse]:
    """Get monthly resource billing summary

     Returns a billing summary for one resource during the specified month. The API user must have
    permission to read billing details.

    Args:
        resource_id (str):
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | AccountResourceBillingSummaryResponse]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        year=year,
        month=month,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_id: str,
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> AccountError | AccountResourceBillingSummaryResponse | None:
    """Get monthly resource billing summary

     Returns a billing summary for one resource during the specified month. The API user must have
    permission to read billing details.

    Args:
        resource_id (str):
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | AccountResourceBillingSummaryResponse
    """

    return sync_detailed(
        resource_id=resource_id,
        year=year,
        month=month,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_id: str,
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountError | AccountResourceBillingSummaryResponse]:
    """Get monthly resource billing summary

     Returns a billing summary for one resource during the specified month. The API user must have
    permission to read billing details.

    Args:
        resource_id (str):
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | AccountResourceBillingSummaryResponse]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        year=year,
        month=month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_id: str,
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
) -> AccountError | AccountResourceBillingSummaryResponse | None:
    """Get monthly resource billing summary

     Returns a billing summary for one resource during the specified month. The API user must have
    permission to read billing details.

    Args:
        resource_id (str):
        year (str):
        month (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | AccountResourceBillingSummaryResponse
    """

    return (
        await asyncio_detailed(
            resource_id=resource_id,
            year=year,
            month=month,
            client=client,
        )
    ).parsed
