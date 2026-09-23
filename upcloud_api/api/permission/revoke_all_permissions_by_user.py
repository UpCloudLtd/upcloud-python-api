from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.permission_error import PermissionError_
from ...types import Response


def _get_kwargs(
    user: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/permission/revoke-all-from-user/{user}".format(
            user=quote(str(user), safe=""),
        ),
    }

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
    user: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PermissionError_]:
    """Revoke all permissions by user

     Revokes all permissions for a specific sub-account to access any resources owned by the main
    account.

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionError_]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PermissionError_ | None:
    """Revoke all permissions by user

     Revokes all permissions for a specific sub-account to access any resources owned by the main
    account.

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionError_
    """

    return sync_detailed(
        user=user,
        client=client,
    ).parsed


async def asyncio_detailed(
    user: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PermissionError_]:
    """Revoke all permissions by user

     Revokes all permissions for a specific sub-account to access any resources owned by the main
    account.

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionError_]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PermissionError_ | None:
    """Revoke all permissions by user

     Revokes all permissions for a specific sub-account to access any resources owned by the main
    account.

    Args:
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionError_
    """

    return (
        await asyncio_detailed(
            user=user,
            client=client,
        )
    ).parsed
