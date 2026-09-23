from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.permission import Permission
from ...models.permission_error import PermissionError_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Permission | Unset = UNSET,
    skip_target_check: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["skip_target_check"] = skip_target_check

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/permission/grant",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Permission | PermissionError_:
    if response.status_code == 200:
        response_200 = Permission.from_dict(response.json())

        return response_200

    response_default = PermissionError_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Permission | PermissionError_]:
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
    skip_target_check: bool | Unset = UNSET,
) -> Response[Permission | PermissionError_]:
    """Grant permission

     Grants a permission for a sub-account to access a resource owned by the main account.

    Args:
        skip_target_check (bool | Unset):
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Permission | PermissionError_]
    """

    kwargs = _get_kwargs(
        body=body,
        skip_target_check=skip_target_check,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
    skip_target_check: bool | Unset = UNSET,
) -> Permission | PermissionError_ | None:
    """Grant permission

     Grants a permission for a sub-account to access a resource owned by the main account.

    Args:
        skip_target_check (bool | Unset):
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Permission | PermissionError_
    """

    return sync_detailed(
        client=client,
        body=body,
        skip_target_check=skip_target_check,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
    skip_target_check: bool | Unset = UNSET,
) -> Response[Permission | PermissionError_]:
    """Grant permission

     Grants a permission for a sub-account to access a resource owned by the main account.

    Args:
        skip_target_check (bool | Unset):
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Permission | PermissionError_]
    """

    kwargs = _get_kwargs(
        body=body,
        skip_target_check=skip_target_check,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: Permission | Unset = UNSET,
    skip_target_check: bool | Unset = UNSET,
) -> Permission | PermissionError_ | None:
    """Grant permission

     Grants a permission for a sub-account to access a resource owned by the main account.

    Args:
        skip_target_check (bool | Unset):
        body (Permission | Unset): A single permission object.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Permission | PermissionError_
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            skip_target_check=skip_target_check,
        )
    ).parsed
