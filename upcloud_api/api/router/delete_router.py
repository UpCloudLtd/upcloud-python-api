from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.router_error import RouterError
from ...types import Response


def _get_kwargs(
    router: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/router/{router}".format(
            router=quote(str(router), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RouterError:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = RouterError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = RouterError.from_dict(response.json())

        return response_409

    response_default = RouterError.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RouterError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    router: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouterError]:
    """Delete router

     Deletes a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouterError]
    """

    kwargs = _get_kwargs(
        router=router,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    router: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouterError | None:
    """Delete router

     Deletes a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouterError
    """

    return sync_detailed(
        router=router,
        client=client,
    ).parsed


async def asyncio_detailed(
    router: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouterError]:
    """Delete router

     Deletes a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouterError]
    """

    kwargs = _get_kwargs(
        router=router,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    router: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouterError | None:
    """Delete router

     Deletes a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouterError
    """

    return (
        await asyncio_detailed(
            router=router,
            client=client,
        )
    ).parsed
