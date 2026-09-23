from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.tag import Tag
from ...models.tag_error import TagError
from ...models.tag_error_400 import TagError400
from ...models.tag_error_403 import TagError403
from ...models.tag_error_404 import TagError404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: Tag | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/tag/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Tag | TagError | TagError400 | TagError403 | TagError404:
    if response.status_code == 200:
        response_200 = Tag.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TagError400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = TagError403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = TagError404.from_dict(response.json())

        return response_404

    response_default = TagError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Tag | TagError | TagError400 | TagError403 | TagError404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Tag | Unset = UNSET,
) -> Response[Tag | TagError | TagError400 | TagError403 | TagError404]:
    """Modify existing tag

     Changes attributes of an existing tag

    Args:
        name (str): Short name used to identify a tag.
        body (Tag | Unset): Container object for a single tag resource. Example: {'tag': {'name':
            'PROD', 'description': 'Production servers', 'servers': {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tag | TagError | TagError400 | TagError403 | TagError404]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Tag | Unset = UNSET,
) -> Tag | TagError | TagError400 | TagError403 | TagError404 | None:
    """Modify existing tag

     Changes attributes of an existing tag

    Args:
        name (str): Short name used to identify a tag.
        body (Tag | Unset): Container object for a single tag resource. Example: {'tag': {'name':
            'PROD', 'description': 'Production servers', 'servers': {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tag | TagError | TagError400 | TagError403 | TagError404
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Tag | Unset = UNSET,
) -> Response[Tag | TagError | TagError400 | TagError403 | TagError404]:
    """Modify existing tag

     Changes attributes of an existing tag

    Args:
        name (str): Short name used to identify a tag.
        body (Tag | Unset): Container object for a single tag resource. Example: {'tag': {'name':
            'PROD', 'description': 'Production servers', 'servers': {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tag | TagError | TagError400 | TagError403 | TagError404]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Tag | Unset = UNSET,
) -> Tag | TagError | TagError400 | TagError403 | TagError404 | None:
    """Modify existing tag

     Changes attributes of an existing tag

    Args:
        name (str): Short name used to identify a tag.
        body (Tag | Unset): Container object for a single tag resource. Example: {'tag': {'name':
            'PROD', 'description': 'Production servers', 'servers': {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565']}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tag | TagError | TagError400 | TagError403 | TagError404
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
