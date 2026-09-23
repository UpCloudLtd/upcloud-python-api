from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_billing_summary import AccountBillingSummary
from ...models.account_error import AccountError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: str,
    month: str,
    *,
    username: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["username"] = username

    params["resource_id"] = resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/account/billing/summary/{year}-{month}".format(
            year=quote(str(year), safe=""),
            month=quote(str(month), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountBillingSummary | AccountError:
    if response.status_code == 200:
        response_200 = AccountBillingSummary.from_dict(response.json())

        return response_200

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountBillingSummary | AccountError]:
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
    username: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
) -> Response[AccountBillingSummary | AccountError]:
    """Get monthly billing summary with resource details

     Returns a billing summary grouped by resource, including billing detail changes during the specified
    month. The API user must have permission to read billing details.

    Args:
        year (str):
        month (str):
        username (str | Unset): Username for an account.
        resource_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountBillingSummary | AccountError]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
        username=username,
        resource_id=resource_id,
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
    username: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
) -> AccountBillingSummary | AccountError | None:
    """Get monthly billing summary with resource details

     Returns a billing summary grouped by resource, including billing detail changes during the specified
    month. The API user must have permission to read billing details.

    Args:
        year (str):
        month (str):
        username (str | Unset): Username for an account.
        resource_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountBillingSummary | AccountError
    """

    return sync_detailed(
        year=year,
        month=month,
        client=client,
        username=username,
        resource_id=resource_id,
    ).parsed


async def asyncio_detailed(
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
    username: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
) -> Response[AccountBillingSummary | AccountError]:
    """Get monthly billing summary with resource details

     Returns a billing summary grouped by resource, including billing detail changes during the specified
    month. The API user must have permission to read billing details.

    Args:
        year (str):
        month (str):
        username (str | Unset): Username for an account.
        resource_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountBillingSummary | AccountError]
    """

    kwargs = _get_kwargs(
        year=year,
        month=month,
        username=username,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: str,
    month: str,
    *,
    client: AuthenticatedClient | Client,
    username: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
) -> AccountBillingSummary | AccountError | None:
    """Get monthly billing summary with resource details

     Returns a billing summary grouped by resource, including billing detail changes during the specified
    month. The API user must have permission to read billing details.

    Args:
        year (str):
        month (str):
        username (str | Unset): Username for an account.
        resource_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountBillingSummary | AccountError
    """

    return (
        await asyncio_detailed(
            year=year,
            month=month,
            client=client,
            username=username,
            resource_id=resource_id,
        )
    ).parsed
