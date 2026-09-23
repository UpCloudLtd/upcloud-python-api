from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.tag_error import TagError
from ...models.tag_error_400 import TagError400
from ...models.tag_error_403 import TagError403
from ...models.tag_error_404 import TagError404
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/tag/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TagError | TagError400 | TagError403 | TagError404:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | TagError | TagError400 | TagError403 | TagError404]:
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
) -> Response[Any | TagError | TagError400 | TagError403 | TagError404]:
    """Delete a tag

     Deletes a specific tag.

    Args:
        name (str): Short name used to identify a tag.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TagError | TagError400 | TagError403 | TagError404]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TagError | TagError400 | TagError403 | TagError404 | None:
    """Delete a tag

     Deletes a specific tag.

    Args:
        name (str): Short name used to identify a tag.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TagError | TagError400 | TagError403 | TagError404
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TagError | TagError400 | TagError403 | TagError404]:
    """Delete a tag

     Deletes a specific tag.

    Args:
        name (str): Short name used to identify a tag.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TagError | TagError400 | TagError403 | TagError404]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TagError | TagError400 | TagError403 | TagError404 | None:
    """Delete a tag

     Deletes a specific tag.

    Args:
        name (str): Short name used to identify a tag.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TagError | TagError400 | TagError403 | TagError404
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
