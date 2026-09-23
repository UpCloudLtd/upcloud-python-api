from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.permission_error import PermissionError_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    target_type: str,
    target_identifier: str,
    *,
    main_account_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["main_account_id"] = main_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/permission/revoke-all-from-target/{target_type}/{target_identifier}".format(
            target_type=quote(str(target_type), safe=""),
            target_identifier=quote(str(target_identifier), safe=""),
        ),
        "params": params,
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
    target_type: str,
    target_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    main_account_id: int | Unset = UNSET,
) -> Response[Any | PermissionError_]:
    """Revoke all permissions by target

     Revokes all permissions for sub-accounts to access a specific resource owned by the main account.

    Args:
        target_type (str):
        target_identifier (str):
        main_account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionError_]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_identifier=target_identifier,
        main_account_id=main_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_type: str,
    target_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    main_account_id: int | Unset = UNSET,
) -> Any | PermissionError_ | None:
    """Revoke all permissions by target

     Revokes all permissions for sub-accounts to access a specific resource owned by the main account.

    Args:
        target_type (str):
        target_identifier (str):
        main_account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionError_
    """

    return sync_detailed(
        target_type=target_type,
        target_identifier=target_identifier,
        client=client,
        main_account_id=main_account_id,
    ).parsed


async def asyncio_detailed(
    target_type: str,
    target_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    main_account_id: int | Unset = UNSET,
) -> Response[Any | PermissionError_]:
    """Revoke all permissions by target

     Revokes all permissions for sub-accounts to access a specific resource owned by the main account.

    Args:
        target_type (str):
        target_identifier (str):
        main_account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionError_]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_identifier=target_identifier,
        main_account_id=main_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_type: str,
    target_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    main_account_id: int | Unset = UNSET,
) -> Any | PermissionError_ | None:
    """Revoke all permissions by target

     Revokes all permissions for sub-accounts to access a specific resource owned by the main account.

    Args:
        target_type (str):
        target_identifier (str):
        main_account_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionError_
    """

    return (
        await asyncio_detailed(
            target_type=target_type,
            target_identifier=target_identifier,
            client=client,
            main_account_id=main_account_id,
        )
    ).parsed
