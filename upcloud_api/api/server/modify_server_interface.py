from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.server_error_400 import ServerError400
from ...models.server_error_403 import ServerError403
from ...models.server_error_404 import ServerError404
from ...models.server_error_409 import ServerError409
from ...models.server_interface_response import ServerInterfaceResponse
from ...models.server_modify_interface import ServerModifyInterface
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    index: int,
    *,
    body: ServerModifyInterface | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/server/{uuid}/networking/interface/{index}".format(
            uuid=quote(str(uuid), safe=""),
            index=quote(str(index), safe=""),
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
    if response.status_code == 200:
        response_200 = ServerInterfaceResponse.from_dict(response.json())

        return response_200

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
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerModifyInterface | Unset = UNSET,
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
]:
    """Modify a network interface

     Modify the IP addresses, source IP filtering, boot setting, or index of a network interface on a
    stopped Cloud Server. Changing the interface network or type is not supported.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        body (ServerModifyInterface | Unset): Modify network interface request Example:
            {'interface': {'bootable': 'yes', 'index': 5, 'source_ip_filtering': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        index=index,
        body=body,
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
    body: ServerModifyInterface | Unset = UNSET,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse | None:
    """Modify a network interface

     Modify the IP addresses, source IP filtering, boot setting, or index of a network interface on a
    stopped Cloud Server. Changing the interface network or type is not supported.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        body (ServerModifyInterface | Unset): Modify network interface request Example:
            {'interface': {'bootable': 'yes', 'index': 5, 'source_ip_filtering': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
    """

    return sync_detailed(
        uuid=uuid,
        index=index,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerModifyInterface | Unset = UNSET,
) -> Response[
    ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
]:
    """Modify a network interface

     Modify the IP addresses, source IP filtering, boot setting, or index of a network interface on a
    stopped Cloud Server. Changing the interface network or type is not supported.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        body (ServerModifyInterface | Unset): Modify network interface request Example:
            {'interface': {'bootable': 'yes', 'index': 5, 'source_ip_filtering': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        index=index,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    index: int,
    *,
    client: AuthenticatedClient | Client,
    body: ServerModifyInterface | Unset = UNSET,
) -> ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse | None:
    """Modify a network interface

     Modify the IP addresses, source IP filtering, boot setting, or index of a network interface on a
    stopped Cloud Server. Changing the interface network or type is not supported.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        index (int):
        body (ServerModifyInterface | Unset): Modify network interface request Example:
            {'interface': {'bootable': 'yes', 'index': 5, 'source_ip_filtering': 'no'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | ServerError400 | ServerError403 | ServerError404 | ServerError409 | ServerInterfaceResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            index=index,
            client=client,
            body=body,
        )
    ).parsed
