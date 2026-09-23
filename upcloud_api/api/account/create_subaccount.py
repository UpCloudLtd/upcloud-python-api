from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_error import AccountError
from ...models.create_subaccount_request import CreateSubaccountRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSubaccountRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/account/sub",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountError | Any:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountError | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubaccountRequest | Unset = UNSET,
) -> Response[AccountError | Any]:
    """Create subaccount

     Creates a subaccount for the authenticated main account.

    Args:
        body (CreateSubaccountRequest | Unset): Request for creating a subaccount. Example:
            {'sub_account': {'first_name': 'first', 'last_name': 'last', 'company': 'my company name',
            'address': 'my address', 'postal_code': '00130', 'city': 'Helsinki', 'state': '',
            'country': 'FIN', 'phone': '+358.31245434', 'email': 'user@example.com', 'vat_number': 'my
            vat number', 'timezone': 'Europe/Helsinki', 'username': 'myusername', 'password':
            'mysecr3tPassword', 'currency': 'EUR', 'language': 'en', 'roles': {'role': ['technical',
            'billing', 'aux_billing']}, 'allow_gui': 'no', 'allow_api': 'yes', 'network_access':
            {'network': []}, 'server_access': {'server': []}, 'storage_access': {'storage': []},
            'tag_access': {'tag': []}, 'ip_filters': {'ip_filter': []}, 'labels': [{'key':
            'department', 'value': 'it'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | Any]
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
    body: CreateSubaccountRequest | Unset = UNSET,
) -> AccountError | Any | None:
    """Create subaccount

     Creates a subaccount for the authenticated main account.

    Args:
        body (CreateSubaccountRequest | Unset): Request for creating a subaccount. Example:
            {'sub_account': {'first_name': 'first', 'last_name': 'last', 'company': 'my company name',
            'address': 'my address', 'postal_code': '00130', 'city': 'Helsinki', 'state': '',
            'country': 'FIN', 'phone': '+358.31245434', 'email': 'user@example.com', 'vat_number': 'my
            vat number', 'timezone': 'Europe/Helsinki', 'username': 'myusername', 'password':
            'mysecr3tPassword', 'currency': 'EUR', 'language': 'en', 'roles': {'role': ['technical',
            'billing', 'aux_billing']}, 'allow_gui': 'no', 'allow_api': 'yes', 'network_access':
            {'network': []}, 'server_access': {'server': []}, 'storage_access': {'storage': []},
            'tag_access': {'tag': []}, 'ip_filters': {'ip_filter': []}, 'labels': [{'key':
            'department', 'value': 'it'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | Any
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubaccountRequest | Unset = UNSET,
) -> Response[AccountError | Any]:
    """Create subaccount

     Creates a subaccount for the authenticated main account.

    Args:
        body (CreateSubaccountRequest | Unset): Request for creating a subaccount. Example:
            {'sub_account': {'first_name': 'first', 'last_name': 'last', 'company': 'my company name',
            'address': 'my address', 'postal_code': '00130', 'city': 'Helsinki', 'state': '',
            'country': 'FIN', 'phone': '+358.31245434', 'email': 'user@example.com', 'vat_number': 'my
            vat number', 'timezone': 'Europe/Helsinki', 'username': 'myusername', 'password':
            'mysecr3tPassword', 'currency': 'EUR', 'language': 'en', 'roles': {'role': ['technical',
            'billing', 'aux_billing']}, 'allow_gui': 'no', 'allow_api': 'yes', 'network_access':
            {'network': []}, 'server_access': {'server': []}, 'storage_access': {'storage': []},
            'tag_access': {'tag': []}, 'ip_filters': {'ip_filter': []}, 'labels': [{'key':
            'department', 'value': 'it'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSubaccountRequest | Unset = UNSET,
) -> AccountError | Any | None:
    """Create subaccount

     Creates a subaccount for the authenticated main account.

    Args:
        body (CreateSubaccountRequest | Unset): Request for creating a subaccount. Example:
            {'sub_account': {'first_name': 'first', 'last_name': 'last', 'company': 'my company name',
            'address': 'my address', 'postal_code': '00130', 'city': 'Helsinki', 'state': '',
            'country': 'FIN', 'phone': '+358.31245434', 'email': 'user@example.com', 'vat_number': 'my
            vat number', 'timezone': 'Europe/Helsinki', 'username': 'myusername', 'password':
            'mysecr3tPassword', 'currency': 'EUR', 'language': 'en', 'roles': {'role': ['technical',
            'billing', 'aux_billing']}, 'allow_gui': 'no', 'allow_api': 'yes', 'network_access':
            {'network': []}, 'server_access': {'server': []}, 'storage_access': {'storage': []},
            'tag_access': {'tag': []}, 'ip_filters': {'ip_filter': []}, 'labels': [{'key':
            'department', 'value': 'it'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
