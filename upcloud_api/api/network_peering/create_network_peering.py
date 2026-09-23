from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_peering import NetworkPeering
from ...models.network_peering_create import NetworkPeeringCreate
from ...models.network_peering_error import NetworkPeeringError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NetworkPeeringCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/network-peering",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NetworkPeering | NetworkPeeringError:
    if response.status_code == 201:
        response_201 = NetworkPeering.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = NetworkPeeringError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = NetworkPeeringError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = NetworkPeeringError.from_dict(response.json())

        return response_409

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
    *,
    client: AuthenticatedClient | Client,
    body: NetworkPeeringCreate | Unset = UNSET,
) -> Response[NetworkPeering | NetworkPeeringError]:
    """Create peering

     Network peerings are used to enable traffic between two networks that can be on different main
    accounts.
    The peering must be established both ways before it's considered as active. Peering is only
    supported between networks
    of type `private`.

    **Note**: you should only create peering between accounts and networks you trust. There is no limits
    on what traffic
    can flow. The server firewall **has no effect** for `private` type networks.

    It is required that both networks have a *Router* attached to the network.

    Args:
        body (NetworkPeeringCreate | Unset): Describes the mutable properties when creating a
            network-peering between two networks Example: {'configured_status': 'active', 'name':
            'Peering A->B', 'network': {'uuid': '03126dc1-a69f-4bc2-8b24-e31c22d64712'},
            'peer_network': {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeering | NetworkPeeringError]
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
    body: NetworkPeeringCreate | Unset = UNSET,
) -> NetworkPeering | NetworkPeeringError | None:
    """Create peering

     Network peerings are used to enable traffic between two networks that can be on different main
    accounts.
    The peering must be established both ways before it's considered as active. Peering is only
    supported between networks
    of type `private`.

    **Note**: you should only create peering between accounts and networks you trust. There is no limits
    on what traffic
    can flow. The server firewall **has no effect** for `private` type networks.

    It is required that both networks have a *Router* attached to the network.

    Args:
        body (NetworkPeeringCreate | Unset): Describes the mutable properties when creating a
            network-peering between two networks Example: {'configured_status': 'active', 'name':
            'Peering A->B', 'network': {'uuid': '03126dc1-a69f-4bc2-8b24-e31c22d64712'},
            'peer_network': {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeering | NetworkPeeringError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NetworkPeeringCreate | Unset = UNSET,
) -> Response[NetworkPeering | NetworkPeeringError]:
    """Create peering

     Network peerings are used to enable traffic between two networks that can be on different main
    accounts.
    The peering must be established both ways before it's considered as active. Peering is only
    supported between networks
    of type `private`.

    **Note**: you should only create peering between accounts and networks you trust. There is no limits
    on what traffic
    can flow. The server firewall **has no effect** for `private` type networks.

    It is required that both networks have a *Router* attached to the network.

    Args:
        body (NetworkPeeringCreate | Unset): Describes the mutable properties when creating a
            network-peering between two networks Example: {'configured_status': 'active', 'name':
            'Peering A->B', 'network': {'uuid': '03126dc1-a69f-4bc2-8b24-e31c22d64712'},
            'peer_network': {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeering | NetworkPeeringError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NetworkPeeringCreate | Unset = UNSET,
) -> NetworkPeering | NetworkPeeringError | None:
    """Create peering

     Network peerings are used to enable traffic between two networks that can be on different main
    accounts.
    The peering must be established both ways before it's considered as active. Peering is only
    supported between networks
    of type `private`.

    **Note**: you should only create peering between accounts and networks you trust. There is no limits
    on what traffic
    can flow. The server firewall **has no effect** for `private` type networks.

    It is required that both networks have a *Router* attached to the network.

    Args:
        body (NetworkPeeringCreate | Unset): Describes the mutable properties when creating a
            network-peering between two networks Example: {'configured_status': 'active', 'name':
            'Peering A->B', 'network': {'uuid': '03126dc1-a69f-4bc2-8b24-e31c22d64712'},
            'peer_network': {'uuid': '03585987-bf7d-4544-8e9b-5a1b4d74a333'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeering | NetworkPeeringError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
