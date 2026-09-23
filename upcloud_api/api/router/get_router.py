from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.router import Router
from ...models.router_error import RouterError
from ...types import Response


def _get_kwargs(
    router: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/router/{router}".format(
            router=quote(str(router), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Router | RouterError:
    if response.status_code == 200:
        response_200 = Router.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = RouterError.from_dict(response.json())

        return response_404

    response_default = RouterError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Router | RouterError]:
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
) -> Response[Router | RouterError]:
    """Get router

     Retrieves details of a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Router | RouterError]
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
) -> Router | RouterError | None:
    """Get router

     Retrieves details of a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Router | RouterError
    """

    return sync_detailed(
        router=router,
        client=client,
    ).parsed


async def asyncio_detailed(
    router: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Router | RouterError]:
    """Get router

     Retrieves details of a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Router | RouterError]
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
) -> Router | RouterError | None:
    """Get router

     Retrieves details of a specific router.

    Args:
        router (UUID): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Router | RouterError
    """

    return (
        await asyncio_detailed(
            router=router,
            client=client,
        )
    ).parsed
