from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_tokens_create_token_request_type_0 import AccountTokensCreateTokenRequestType0
from ...models.account_tokens_create_token_request_type_1 import AccountTokensCreateTokenRequestType1
from ...models.account_tokens_problem import AccountTokensProblem
from ...models.account_tokens_problem_400 import AccountTokensProblem400
from ...models.account_tokens_problem_401 import AccountTokensProblem401
from ...models.account_tokens_problem_403 import AccountTokensProblem403
from ...models.account_tokens_problem_409 import AccountTokensProblem409
from ...models.account_tokens_token import AccountTokensToken
from ...types import Response


def _get_kwargs(
    *,
    body: AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/account/tokens",
    }

    if isinstance(body, AccountTokensCreateTokenRequestType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AccountTokensProblem
    | AccountTokensProblem400
    | AccountTokensProblem401
    | AccountTokensProblem403
    | AccountTokensProblem409
    | AccountTokensToken
):
    if response.status_code == 201:
        response_201 = AccountTokensToken.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AccountTokensProblem400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AccountTokensProblem401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AccountTokensProblem403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = AccountTokensProblem409.from_dict(response.json())

        return response_409

    response_default = AccountTokensProblem.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AccountTokensProblem
    | AccountTokensProblem400
    | AccountTokensProblem401
    | AccountTokensProblem403
    | AccountTokensProblem409
    | AccountTokensToken
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1,
) -> Response[
    AccountTokensProblem
    | AccountTokensProblem400
    | AccountTokensProblem401
    | AccountTokensProblem403
    | AccountTokensProblem409
    | AccountTokensToken
]:
    """Create an API token

     Create a new API token. Maximum token validity is 24*365h=8760h (~1 year).
    Attribute allowed_ip_prefixes allows defining a list of CIDR/IP addresses from where the token is
    accepted.
    Empty list denies access from everywhere. If unset, the default list will be the IP filters of the
    account. If no IP filters are defined for the account either, the default will be ["0.0.0.0/0",
    "::0/0"], i.e. allow from any address.

    Args:
        body (AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountTokensProblem | AccountTokensProblem400 | AccountTokensProblem401 | AccountTokensProblem403 | AccountTokensProblem409 | AccountTokensToken]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1,
) -> (
    AccountTokensProblem
    | AccountTokensProblem400
    | AccountTokensProblem401
    | AccountTokensProblem403
    | AccountTokensProblem409
    | AccountTokensToken
    | None
):
    """Create an API token

     Create a new API token. Maximum token validity is 24*365h=8760h (~1 year).
    Attribute allowed_ip_prefixes allows defining a list of CIDR/IP addresses from where the token is
    accepted.
    Empty list denies access from everywhere. If unset, the default list will be the IP filters of the
    account. If no IP filters are defined for the account either, the default will be ["0.0.0.0/0",
    "::0/0"], i.e. allow from any address.

    Args:
        body (AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountTokensProblem | AccountTokensProblem400 | AccountTokensProblem401 | AccountTokensProblem403 | AccountTokensProblem409 | AccountTokensToken
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1,
) -> Response[
    AccountTokensProblem
    | AccountTokensProblem400
    | AccountTokensProblem401
    | AccountTokensProblem403
    | AccountTokensProblem409
    | AccountTokensToken
]:
    """Create an API token

     Create a new API token. Maximum token validity is 24*365h=8760h (~1 year).
    Attribute allowed_ip_prefixes allows defining a list of CIDR/IP addresses from where the token is
    accepted.
    Empty list denies access from everywhere. If unset, the default list will be the IP filters of the
    account. If no IP filters are defined for the account either, the default will be ["0.0.0.0/0",
    "::0/0"], i.e. allow from any address.

    Args:
        body (AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountTokensProblem | AccountTokensProblem400 | AccountTokensProblem401 | AccountTokensProblem403 | AccountTokensProblem409 | AccountTokensToken]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1,
) -> (
    AccountTokensProblem
    | AccountTokensProblem400
    | AccountTokensProblem401
    | AccountTokensProblem403
    | AccountTokensProblem409
    | AccountTokensToken
    | None
):
    """Create an API token

     Create a new API token. Maximum token validity is 24*365h=8760h (~1 year).
    Attribute allowed_ip_prefixes allows defining a list of CIDR/IP addresses from where the token is
    accepted.
    Empty list denies access from everywhere. If unset, the default list will be the IP filters of the
    account. If no IP filters are defined for the account either, the default will be ["0.0.0.0/0",
    "::0/0"], i.e. allow from any address.

    Args:
        body (AccountTokensCreateTokenRequestType0 | AccountTokensCreateTokenRequestType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountTokensProblem | AccountTokensProblem400 | AccountTokensProblem401 | AccountTokensProblem403 | AccountTokensProblem409 | AccountTokensToken
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
