from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_tokens_problem import AccountTokensProblem
from ...models.account_tokens_problem_401 import AccountTokensProblem401
from ...models.account_tokens_problem_404 import AccountTokensProblem404
from ...types import Response


def _get_kwargs(
    token_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/account/tokens/{token_uuid}".format(
            token_uuid=quote(str(token_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = AccountTokensProblem401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AccountTokensProblem404.from_dict(response.json())

        return response_404

    response_default = AccountTokensProblem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any]:
    """Revoke a token

     Revoke a specific API token.

    Args:
        token_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any]
    """

    kwargs = _get_kwargs(
        token_uuid=token_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any | None:
    """Revoke a token

     Revoke a specific API token.

    Args:
        token_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any
    """

    return sync_detailed(
        token_uuid=token_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    token_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any]:
    """Revoke a token

     Revoke a specific API token.

    Args:
        token_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any]
    """

    kwargs = _get_kwargs(
        token_uuid=token_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any | None:
    """Revoke a token

     Revoke a specific API token.

    Args:
        token_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountTokensProblem | AccountTokensProblem401 | AccountTokensProblem404 | Any
    """

    return (
        await asyncio_detailed(
            token_uuid=token_uuid,
            client=client,
        )
    ).parsed
