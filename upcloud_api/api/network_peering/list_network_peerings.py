from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_peering_error import NetworkPeeringError
from ...models.network_peerings import NetworkPeerings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    uuid: UUID | Unset = UNSET,
    network_uuid_local: UUID | Unset = UNSET,
    network_uuid_peer: UUID | Unset = UNSET,
    label: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_uuid: str | Unset = UNSET
    if not isinstance(uuid, Unset):
        json_uuid = str(uuid)
    params["uuid"] = json_uuid

    json_network_uuid_local: str | Unset = UNSET
    if not isinstance(network_uuid_local, Unset):
        json_network_uuid_local = str(network_uuid_local)
    params["network_uuid_local"] = json_network_uuid_local

    json_network_uuid_peer: str | Unset = UNSET
    if not isinstance(network_uuid_peer, Unset):
        json_network_uuid_peer = str(network_uuid_peer)
    params["network_uuid_peer"] = json_network_uuid_peer

    params["label"] = label

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/network-peering",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NetworkPeeringError | NetworkPeerings:
    if response.status_code == 200:
        response_200 = NetworkPeerings.from_dict(response.json())

        return response_200

    response_default = NetworkPeeringError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NetworkPeeringError | NetworkPeerings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    uuid: UUID | Unset = UNSET,
    network_uuid_local: UUID | Unset = UNSET,
    network_uuid_peer: UUID | Unset = UNSET,
    label: str | Unset = UNSET,
) -> Response[NetworkPeeringError | NetworkPeerings]:
    """List peerings

     Get a list of all peerings within the current account. Only peerings that refer to a network that
    the current
    account has access are returned.

    It is also possible to filter network peering with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. The URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only network peering that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_local (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_peer (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeeringError | NetworkPeerings]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        network_uuid_local=network_uuid_local,
        network_uuid_peer=network_uuid_peer,
        label=label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    uuid: UUID | Unset = UNSET,
    network_uuid_local: UUID | Unset = UNSET,
    network_uuid_peer: UUID | Unset = UNSET,
    label: str | Unset = UNSET,
) -> NetworkPeeringError | NetworkPeerings | None:
    """List peerings

     Get a list of all peerings within the current account. Only peerings that refer to a network that
    the current
    account has access are returned.

    It is also possible to filter network peering with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. The URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only network peering that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_local (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_peer (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeeringError | NetworkPeerings
    """

    return sync_detailed(
        client=client,
        uuid=uuid,
        network_uuid_local=network_uuid_local,
        network_uuid_peer=network_uuid_peer,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    uuid: UUID | Unset = UNSET,
    network_uuid_local: UUID | Unset = UNSET,
    network_uuid_peer: UUID | Unset = UNSET,
    label: str | Unset = UNSET,
) -> Response[NetworkPeeringError | NetworkPeerings]:
    """List peerings

     Get a list of all peerings within the current account. Only peerings that refer to a network that
    the current
    account has access are returned.

    It is also possible to filter network peering with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. The URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only network peering that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_local (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_peer (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeeringError | NetworkPeerings]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        network_uuid_local=network_uuid_local,
        network_uuid_peer=network_uuid_peer,
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    uuid: UUID | Unset = UNSET,
    network_uuid_local: UUID | Unset = UNSET,
    network_uuid_peer: UUID | Unset = UNSET,
    label: str | Unset = UNSET,
) -> NetworkPeeringError | NetworkPeerings | None:
    """List peerings

     Get a list of all peerings within the current account. Only peerings that refer to a network that
    the current
    account has access are returned.

    It is also possible to filter network peering with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. The URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only network peering that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        uuid (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_local (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        network_uuid_peer (UUID | Unset): Universally unique identifier Example:
            0414e0d7-4436-4037-9dd8-6eaf47dce599.
        label (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeeringError | NetworkPeerings
    """

    return (
        await asyncio_detailed(
            client=client,
            uuid=uuid,
            network_uuid_local=network_uuid_local,
            network_uuid_peer=network_uuid_peer,
            label=label,
        )
    ).parsed
