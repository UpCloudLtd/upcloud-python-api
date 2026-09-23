from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.vnc_keymap_error import VncKeymapError
from ...models.vnc_keymap_keymaps import VncKeymapKeymaps
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/vnc_keymap",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> VncKeymapError | VncKeymapKeymaps:
    if response.status_code == 200:
        response_200 = VncKeymapKeymaps.from_dict(response.json())

        return response_200

    response_default = VncKeymapError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[VncKeymapError | VncKeymapKeymaps]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[VncKeymapError | VncKeymapKeymaps]:
    """List VNC keymaps

     Retrieves a list of supported VNC keymaps.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VncKeymapError | VncKeymapKeymaps]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> VncKeymapError | VncKeymapKeymaps | None:
    """List VNC keymaps

     Retrieves a list of supported VNC keymaps.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VncKeymapError | VncKeymapKeymaps
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[VncKeymapError | VncKeymapKeymaps]:
    """List VNC keymaps

     Retrieves a list of supported VNC keymaps.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VncKeymapError | VncKeymapKeymaps]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> VncKeymapError | VncKeymapKeymaps | None:
    """List VNC keymaps

     Retrieves a list of supported VNC keymaps.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VncKeymapError | VncKeymapKeymaps
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
