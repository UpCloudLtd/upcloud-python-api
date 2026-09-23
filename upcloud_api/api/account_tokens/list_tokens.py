from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_tokens_problem import AccountTokensProblem
from ...models.account_tokens_problem_401 import AccountTokensProblem401
from ...models.account_tokens_token import AccountTokensToken
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    gui: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["gui"] = gui

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/account/tokens",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasaccount_tokens_list_tokens_response_item_data in _response_200:
            componentsschemasaccount_tokens_list_tokens_response_item = AccountTokensToken.from_dict(
                componentsschemasaccount_tokens_list_tokens_response_item_data
            )

            response_200.append(componentsschemasaccount_tokens_list_tokens_response_item)

        return response_200

    if response.status_code == 401:
        response_401 = AccountTokensProblem401.from_dict(response.json())

        return response_401

    response_default = AccountTokensProblem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    gui: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]]:
    """List API tokens

     List all tokens for the currently authorized account.
    The tokens are returned in a paged format, with the default page size being 20.
    The maximum page size is 100.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        gui (bool | Unset):  Example: True.
        sort (str | Unset):  Example: +name,-created_at.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        gui=gui,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    gui: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken] | None:
    """List API tokens

     List all tokens for the currently authorized account.
    The tokens are returned in a paged format, with the default page size being 20.
    The maximum page size is 100.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        gui (bool | Unset):  Example: True.
        sort (str | Unset):  Example: +name,-created_at.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        gui=gui,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    gui: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]]:
    """List API tokens

     List all tokens for the currently authorized account.
    The tokens are returned in a paged format, with the default page size being 20.
    The maximum page size is 100.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        gui (bool | Unset):  Example: True.
        sort (str | Unset):  Example: +name,-created_at.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        gui=gui,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    gui: bool | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken] | None:
    """List API tokens

     List all tokens for the currently authorized account.
    The tokens are returned in a paged format, with the default page size being 20.
    The maximum page size is 100.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        gui (bool | Unset):  Example: True.
        sort (str | Unset):  Example: +name,-created_at.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountTokensProblem | AccountTokensProblem401 | list[AccountTokensToken]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            gui=gui,
            sort=sort,
        )
    ).parsed
