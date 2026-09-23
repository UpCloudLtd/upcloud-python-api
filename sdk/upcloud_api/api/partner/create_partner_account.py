from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.partner_account import PartnerAccount
from ...models.partner_create_account import PartnerCreateAccount
from ...models.partner_error import PartnerError
from ...models.partner_error_400 import PartnerError400
from ...models.partner_error_403 import PartnerError403
from ...models.partner_error_409 import PartnerError409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PartnerCreateAccount | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/partner/accounts",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409:
    if response.status_code == 201:
        response_201 = PartnerAccount.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PartnerError400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PartnerError403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = PartnerError409.from_dict(response.json())

        return response_409

    response_default = PartnerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerCreateAccount | Unset = UNSET,
) -> Response[PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409]:
    """Create new account

     Creates new UpCloud account that will be linked to partner's existing invoicing.

    Args:
        body (PartnerCreateAccount | Unset): Request payload for creating a partner-managed
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409]
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
    body: PartnerCreateAccount | Unset = UNSET,
) -> PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409 | None:
    """Create new account

     Creates new UpCloud account that will be linked to partner's existing invoicing.

    Args:
        body (PartnerCreateAccount | Unset): Request payload for creating a partner-managed
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerCreateAccount | Unset = UNSET,
) -> Response[PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409]:
    """Create new account

     Creates new UpCloud account that will be linked to partner's existing invoicing.

    Args:
        body (PartnerCreateAccount | Unset): Request payload for creating a partner-managed
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PartnerCreateAccount | Unset = UNSET,
) -> PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409 | None:
    """Create new account

     Creates new UpCloud account that will be linked to partner's existing invoicing.

    Args:
        body (PartnerCreateAccount | Unset): Request payload for creating a partner-managed
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartnerAccount | PartnerError | PartnerError400 | PartnerError403 | PartnerError409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
