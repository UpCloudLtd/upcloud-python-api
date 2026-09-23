from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    network_name: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/database/{uuid}/networks/{network_name}".format(
            uuid=quote(str(uuid), safe=""),
            network_name=quote(str(network_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DatabaseErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DatabaseErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DatabaseErrorResponse]:
    """Delete network

     Detaches an existing SDN network from a Managed Database service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        network_name=network_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DatabaseErrorResponse | None:
    """Delete network

     Detaches an existing SDN network from a Managed Database service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DatabaseErrorResponse
    """

    return sync_detailed(
        uuid=uuid,
        network_name=network_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DatabaseErrorResponse]:
    """Delete network

     Detaches an existing SDN network from a Managed Database service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DatabaseErrorResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        network_name=network_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    network_name: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DatabaseErrorResponse | None:
    """Delete network

     Detaches an existing SDN network from a Managed Database service by its {uuid} and {network_name}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        network_name (UUID): The unique identifier for the integration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DatabaseErrorResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            network_name=network_name,
            client=client,
        )
    ).parsed
