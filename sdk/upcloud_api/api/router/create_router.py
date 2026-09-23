from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.router import Router
from ...models.router_create import RouterCreate
from ...models.router_error import RouterError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RouterCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/router",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Router | RouterError:
    if response.status_code == 201:
        response_201 = Router.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = RouterError.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = RouterError.from_dict(response.json())

        return response_409

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
    *,
    client: AuthenticatedClient | Client,
    body: RouterCreate | Unset = UNSET,
) -> Response[Router | RouterError]:
    """Create router

     Creates a new router.
    Routers can be used to connect multiple Private Networks. Cloud Servers on any attached network can
    communicate
    directly with each other.

    Args:
        body (RouterCreate | Unset): Request schema for creating a router Example: {'router':
            {'name': 'Example router', 'static_routes': [{'name': 'static-route-0', 'nexthop':
            '192.168.1.1', 'route': '0.0.0.0/0'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Router | RouterError]
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
    body: RouterCreate | Unset = UNSET,
) -> Router | RouterError | None:
    """Create router

     Creates a new router.
    Routers can be used to connect multiple Private Networks. Cloud Servers on any attached network can
    communicate
    directly with each other.

    Args:
        body (RouterCreate | Unset): Request schema for creating a router Example: {'router':
            {'name': 'Example router', 'static_routes': [{'name': 'static-route-0', 'nexthop':
            '192.168.1.1', 'route': '0.0.0.0/0'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Router | RouterError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RouterCreate | Unset = UNSET,
) -> Response[Router | RouterError]:
    """Create router

     Creates a new router.
    Routers can be used to connect multiple Private Networks. Cloud Servers on any attached network can
    communicate
    directly with each other.

    Args:
        body (RouterCreate | Unset): Request schema for creating a router Example: {'router':
            {'name': 'Example router', 'static_routes': [{'name': 'static-route-0', 'nexthop':
            '192.168.1.1', 'route': '0.0.0.0/0'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Router | RouterError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RouterCreate | Unset = UNSET,
) -> Router | RouterError | None:
    """Create router

     Creates a new router.
    Routers can be used to connect multiple Private Networks. Cloud Servers on any attached network can
    communicate
    directly with each other.

    Args:
        body (RouterCreate | Unset): Request schema for creating a router Example: {'router':
            {'name': 'Example router', 'static_routes': [{'name': 'static-route-0', 'nexthop':
            '192.168.1.1', 'route': '0.0.0.0/0'}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Router | RouterError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
