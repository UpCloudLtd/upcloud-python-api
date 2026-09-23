from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.zone_error import ZoneError
from ...models.zone_vlans import ZoneVlans
from ...types import Response


def _get_kwargs(
    zone: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/zone/{zone}/vlans".format(
            zone=quote(str(zone), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ZoneError | ZoneVlans:
    if response.status_code == 200:
        response_200 = ZoneVlans.from_dict(response.json())

        return response_200

    response_default = ZoneError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ZoneError | ZoneVlans]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    zone: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ZoneError | ZoneVlans]:
    """List VLANs in a zone

     Retrieves a list of VLANs in a specific zone.

    Args:
        zone (str): Zone identifier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ZoneError | ZoneVlans]
    """

    kwargs = _get_kwargs(
        zone=zone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    zone: str,
    *,
    client: AuthenticatedClient | Client,
) -> ZoneError | ZoneVlans | None:
    """List VLANs in a zone

     Retrieves a list of VLANs in a specific zone.

    Args:
        zone (str): Zone identifier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ZoneError | ZoneVlans
    """

    return sync_detailed(
        zone=zone,
        client=client,
    ).parsed


async def asyncio_detailed(
    zone: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ZoneError | ZoneVlans]:
    """List VLANs in a zone

     Retrieves a list of VLANs in a specific zone.

    Args:
        zone (str): Zone identifier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ZoneError | ZoneVlans]
    """

    kwargs = _get_kwargs(
        zone=zone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    zone: str,
    *,
    client: AuthenticatedClient | Client,
) -> ZoneError | ZoneVlans | None:
    """List VLANs in a zone

     Retrieves a list of VLANs in a specific zone.

    Args:
        zone (str): Zone identifier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ZoneError | ZoneVlans
    """

    return (
        await asyncio_detailed(
            zone=zone,
            client=client,
        )
    ).parsed
