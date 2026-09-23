from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_add_ip_address import ServerAddIpAddress
from ...models.server_boolean_yesno import ServerBooleanYesno
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_ip_address_interface_response import ServerIpAddressInterfaceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    index: int,
    *,
    body: ServerAddIpAddress | Unset = UNSET,
    force: ServerBooleanYesno | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_force: str | Unset = UNSET
    if not isinstance(force, Unset):
        json_force = force.value

    params["force"] = json_force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/server/{uuid}/networking/interface/{index}/ip_address".format(
            uuid=quote(str(uuid), safe=""),
            index=quote(str(index), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse:
    if response.status_code == 201:
        response_201 = ServerIpAddressInterfaceResponse.from_dict(response.json())

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
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddIpAddress | Unset = UNSET,
    force: ServerBooleanYesno | Unset = UNSET,
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse
]:
    """Add an IP address to a network interface

     Add an IPv4 or IPv6 address to a private network interface. The interface cannot contain addresses
    from both families and can have at most five addresses.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        force (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        body (ServerAddIpAddress | Unset): Add IP address to a network interface request Example:
            {'ip_address': {'address': '10.0.0.30', 'family': 'IPv4'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        index=index,
        body=body,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddIpAddress | Unset = UNSET,
    force: ServerBooleanYesno | Unset = UNSET,
) -> (
    ServerError
    | ServerError400
    | ServerError403
    | ServerError404
    | ServerError409
    | ServerIpAddressInterfaceResponse
    | None
):
    """Add an IP address to a network interface

     Add an IPv4 or IPv6 address to a private network interface. The interface cannot contain addresses
    from both families and can have at most five addresses.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        force (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        body (ServerAddIpAddress | Unset): Add IP address to a network interface request Example:
            {'ip_address': {'address': '10.0.0.30', 'family': 'IPv4'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse
    """

    return sync_detailed(
        uuid=uuid,
        index=index,
        client=client,
        body=body,
        force=force,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddIpAddress | Unset = UNSET,
    force: ServerBooleanYesno | Unset = UNSET,
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse
]:
    """Add an IP address to a network interface

     Add an IPv4 or IPv6 address to a private network interface. The interface cannot contain addresses
    from both families and can have at most five addresses.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        force (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        body (ServerAddIpAddress | Unset): Add IP address to a network interface request Example:
            {'ip_address': {'address': '10.0.0.30', 'family': 'IPv4'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        index=index,
        body=body,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerAddIpAddress | Unset = UNSET,
    force: ServerBooleanYesno | Unset = UNSET,
) -> (
    ServerError
    | ServerError400
    | ServerError403
    | ServerError404
    | ServerError409
    | ServerIpAddressInterfaceResponse
    | None
):
    """Add an IP address to a network interface

     Add an IPv4 or IPv6 address to a private network interface. The interface cannot contain addresses
    from both families and can have at most five addresses.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        force (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        body (ServerAddIpAddress | Unset): Add IP address to a network interface request Example:
            {'ip_address': {'address': '10.0.0.30', 'family': 'IPv4'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerIpAddressInterfaceResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            index=index,
            client=client,
            body=body,
            force=force,
        )
    ).parsed
