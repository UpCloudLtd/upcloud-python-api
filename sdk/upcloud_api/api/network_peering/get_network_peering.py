from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_peering import NetworkPeering
from ...models.network_peering_error import NetworkPeeringError
from ...types import Response


def _get_kwargs(
    peering_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/network-peering/{peering_uuid}".format(
            peering_uuid=quote(str(peering_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NetworkPeering | NetworkPeeringError:
    if response.status_code == 200:
        response_200 = NetworkPeering.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = NetworkPeeringError.from_dict(response.json())

        return response_404

    response_default = NetworkPeeringError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NetworkPeering | NetworkPeeringError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[NetworkPeering | NetworkPeeringError]:
    """Get peering

     Returns the state of an existing network peering.

    Note that the `peer_network` field only contains the network details if the peering has been defined
    by both accounts.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeering | NetworkPeeringError]
    """

    kwargs = _get_kwargs(
        peering_uuid=peering_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> NetworkPeering | NetworkPeeringError | None:
    """Get peering

     Returns the state of an existing network peering.

    Note that the `peer_network` field only contains the network details if the peering has been defined
    by both accounts.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeering | NetworkPeeringError
    """

    return sync_detailed(
        peering_uuid=peering_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[NetworkPeering | NetworkPeeringError]:
    """Get peering

     Returns the state of an existing network peering.

    Note that the `peer_network` field only contains the network details if the peering has been defined
    by both accounts.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeering | NetworkPeeringError]
    """

    kwargs = _get_kwargs(
        peering_uuid=peering_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> NetworkPeering | NetworkPeeringError | None:
    """Get peering

     Returns the state of an existing network peering.

    Note that the `peer_network` field only contains the network details if the peering has been defined
    by both accounts.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeering | NetworkPeeringError
    """

    return (
        await asyncio_detailed(
            peering_uuid=peering_uuid,
            client=client,
        )
    ).parsed
