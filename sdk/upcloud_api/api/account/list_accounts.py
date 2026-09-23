from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_error import AccountError
from ...models.accounts import Accounts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["label"] = label

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/account/list",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountError | Accounts:
    if response.status_code == 200:
        response_200 = Accounts.from_dict(response.json())

        return response_200

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountError | Accounts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
) -> Response[AccountError | Accounts]:
    """List accounts

     Returns the main account and its subaccounts. Account listing is available only to the main account.

    Args:
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | Accounts]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
) -> AccountError | Accounts | None:
    """List accounts

     Returns the main account and its subaccounts. Account listing is available only to the main account.

    Args:
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | Accounts
    """

    return sync_detailed(
        client=client,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
) -> Response[AccountError | Accounts]:
    """List accounts

     Returns the main account and its subaccounts. Account listing is available only to the main account.

    Args:
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | Accounts]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    label: str | Unset = UNSET,
) -> AccountError | Accounts | None:
    """List accounts

     Returns the main account and its subaccounts. Account listing is available only to the main account.

    Args:
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | Accounts
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
        )
    ).parsed
