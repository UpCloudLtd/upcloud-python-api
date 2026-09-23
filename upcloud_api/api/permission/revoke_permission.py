from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.permission import Permission
from ...models.permission_error import PermissionError_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Permission | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/permission/revoke",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PermissionError_:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = PermissionError_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PermissionError_]:
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
) -> Response[Any | PermissionError_]:
    """Revoke permission

     Revokes a permission for a sub-account to access a resource owned by the main account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionError_]
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
) -> Any | PermissionError_ | None:
    """Revoke permission

     Revokes a permission for a sub-account to access a resource owned by the main account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionError_
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
) -> Response[Any | PermissionError_]:
    """Revoke permission

     Revokes a permission for a sub-account to access a resource owned by the main account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionError_]
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
) -> Any | PermissionError_ | None:
    """Revoke permission

     Revokes a permission for a sub-account to access a resource owned by the main account.

    Args:
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionError_
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
