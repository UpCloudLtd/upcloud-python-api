from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_add_interface import ServerAddInterface
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_interface_response import ServerInterfaceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ServerAddInterface | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/server/{uuid}/networking/interface".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse:
    if response.status_code == 201:
        response_201 = ServerInterfaceResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ServerError400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ServerError403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ServerError404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ServerError409.from_dict(response.json())

        return response_409

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddInterface | Unset = UNSET,
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
]:
    """Add a network interface

     Add a network interface to a stopped Cloud Server. A private interface must identify the SDN network
    to attach. The combined limit of network interfaces and storage devices is 24.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAddInterface | Unset): Add network interface request Example: {'interface':
            {'ip_addresses': {'ip_address': [{'address': '10.0.0.20', 'dhcp_provided': 'yes',
            'family': 'IPv4'}]}, 'network': '0374ce47-4303-4490-987d-32dc96cfd79b',
            'source_ip_filtering': 'yes', 'type': 'private'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddInterface | Unset = UNSET,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse | None:
    """Add a network interface

     Add a network interface to a stopped Cloud Server. A private interface must identify the SDN network
    to attach. The combined limit of network interfaces and storage devices is 24.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAddInterface | Unset): Add network interface request Example: {'interface':
            {'ip_addresses': {'ip_address': [{'address': '10.0.0.20', 'dhcp_provided': 'yes',
            'family': 'IPv4'}]}, 'network': '0374ce47-4303-4490-987d-32dc96cfd79b',
            'source_ip_filtering': 'yes', 'type': 'private'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddInterface | Unset = UNSET,
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
]:
    """Add a network interface

     Add a network interface to a stopped Cloud Server. A private interface must identify the SDN network
    to attach. The combined limit of network interfaces and storage devices is 24.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAddInterface | Unset): Add network interface request Example: {'interface':
            {'ip_addresses': {'ip_address': [{'address': '10.0.0.20', 'dhcp_provided': 'yes',
            'family': 'IPv4'}]}, 'network': '0374ce47-4303-4490-987d-32dc96cfd79b',
            'source_ip_filtering': 'yes', 'type': 'private'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddInterface | Unset = UNSET,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse | None:
    """Add a network interface

     Add a network interface to a stopped Cloud Server. A private interface must identify the SDN network
    to attach. The combined limit of network interfaces and storage devices is 24.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerAddInterface | Unset): Add network interface request Example: {'interface':
            {'ip_addresses': {'ip_address': [{'address': '10.0.0.20', 'dhcp_provided': 'yes',
            'family': 'IPv4'}]}, 'network': '0374ce47-4303-4490-987d-32dc96cfd79b',
            'source_ip_filtering': 'yes', 'type': 'private'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
