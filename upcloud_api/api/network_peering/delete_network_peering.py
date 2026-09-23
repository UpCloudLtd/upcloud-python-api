from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_peering_error import NetworkPeeringError
from ...types import Response


def _get_kwargs(
    peering_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/network-peering/{peering_uuid}".format(
            peering_uuid=quote(str(peering_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | NetworkPeeringError:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = NetworkPeeringError.from_dict(response.json())

        return response_404

    response_default = NetworkPeeringError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | NetworkPeeringError]:
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
) -> Response[Any | NetworkPeeringError]:
    """Delete peering

     Deletes a network peering. It is required that the peering is in `disabled` state before delete is
    possible.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NetworkPeeringError]
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
) -> Any | NetworkPeeringError | None:
    """Delete peering

     Deletes a network peering. It is required that the peering is in `disabled` state before delete is
    possible.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NetworkPeeringError
    """

    return sync_detailed(
        peering_uuid=peering_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    peering_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | NetworkPeeringError]:
    """Delete peering

     Deletes a network peering. It is required that the peering is in `disabled` state before delete is
    possible.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NetworkPeeringError]
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
) -> Any | NetworkPeeringError | None:
    """Delete peering

     Deletes a network peering. It is required that the peering is in `disabled` state before delete is
    possible.

    Args:
        peering_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NetworkPeeringError
    """

    return (
        await asyncio_detailed(
            peering_uuid=peering_uuid,
            client=client,
        )
    ).parsed
