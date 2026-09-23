from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_peering import NetworkPeering
from ...models.network_peering_error import NetworkPeeringError
from ...models.network_peering_modify import NetworkPeeringModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    peering_uuid: UUID,
    *,
    body: NetworkPeeringModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/network-peering/{peering_uuid}".format(
            peering_uuid=quote(str(peering_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NetworkPeering | NetworkPeeringError:
    if response.status_code == 200:
        response_200 = NetworkPeering.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = NetworkPeeringError.from_dict(response.json())

        return response_400

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
    body: NetworkPeeringModify | Unset = UNSET,
) -> Response[NetworkPeering | NetworkPeeringError]:
    """Modify peering

     Modifies attributes of an existing network peering.

    Args:
        peering_uuid (UUID):
        body (NetworkPeeringModify | Unset): Describes the mutable properties when modifying a
            network-peering Example: {'configured_status': 'disabled', 'name': 'Peering A->B
            modified'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeering | NetworkPeeringError]
    """

    kwargs = _get_kwargs(
        peering_uuid=peering_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: NetworkPeeringModify | Unset = UNSET,
) -> NetworkPeering | NetworkPeeringError | None:
    """Modify peering

     Modifies attributes of an existing network peering.

    Args:
        peering_uuid (UUID):
        body (NetworkPeeringModify | Unset): Describes the mutable properties when modifying a
            network-peering Example: {'configured_status': 'disabled', 'name': 'Peering A->B
            modified'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkPeering | NetworkPeeringError
    """

    return sync_detailed(
        peering_uuid=peering_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: NetworkPeeringModify | Unset = UNSET,
) -> Response[NetworkPeering | NetworkPeeringError]:
    """Modify peering

     Modifies attributes of an existing network peering.

    Args:
        peering_uuid (UUID):
        body (NetworkPeeringModify | Unset): Describes the mutable properties when modifying a
            network-peering Example: {'configured_status': 'disabled', 'name': 'Peering A->B
            modified'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkPeering | NetworkPeeringError]
    """

    kwargs = _get_kwargs(
        peering_uuid=peering_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: NetworkPeeringModify | Unset = UNSET,
) -> NetworkPeering | NetworkPeeringError | None:
    """Modify peering

     Modifies attributes of an existing network peering.

    Args:
        peering_uuid (UUID):
        body (NetworkPeeringModify | Unset): Describes the mutable properties when modifying a
            network-peering Example: {'configured_status': 'disabled', 'name': 'Peering A->B
            modified'}.

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
            body=body,
        )
    ).parsed
