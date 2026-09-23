from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.permission import Permission
from ...models.permission_error import PermissionError_
from ...models.permissions import Permissions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Permission | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/permission",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PermissionError_ | Permissions:
    if response.status_code == 200:
        response_200 = Permissions.from_dict(response.json())

        return response_200

    response_default = PermissionError_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PermissionError_ | Permissions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
) -> Response[PermissionError_ | Permissions]:
    """Replace permissions

     Replaces the entire set of permissions for sub-accounts to access resources owned by the main
    account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionError_ | Permissions]
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
    body: Permission | Unset = UNSET,
) -> PermissionError_ | Permissions | None:
    """Replace permissions

     Replaces the entire set of permissions for sub-accounts to access resources owned by the main
    account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionError_ | Permissions
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
) -> Response[PermissionError_ | Permissions]:
    """Replace permissions

     Replaces the entire set of permissions for sub-accounts to access resources owned by the main
    account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionError_ | Permissions]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
) -> PermissionError_ | Permissions | None:
    """Replace permissions

     Replaces the entire set of permissions for sub-accounts to access resources owned by the main
    account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionError_ | Permissions
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
