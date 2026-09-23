from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_group import ServerGroup
from ...models.server_group_error import ServerGroupError
from ...models.server_group_modify import ServerGroupModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ServerGroupModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/server-group/{uuid}".format(
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
) -> ServerGroup | ServerGroupError:
    if response.status_code == 200:
        response_200 = ServerGroup.from_dict(response.json())

        return response_200

    response_default = ServerGroupError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServerGroup | ServerGroupError]:
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
    body: ServerGroupModify | Unset = UNSET,
) -> Response[ServerGroup | ServerGroupError]:
    """Modify server group

     Modifies an existing server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerGroupModify | Unset): A schema for creating/modifying a server group Example:
            {'server_group': {'title': 'edge-cluster-a', 'servers': {'servers':
            ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'labels': {'label': [{'key': 'env', 'value':
            'prod'}]}, 'anti_affinity': 'yes'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerGroup | ServerGroupError]
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
    body: ServerGroupModify | Unset = UNSET,
) -> ServerGroup | ServerGroupError | None:
    """Modify server group

     Modifies an existing server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerGroupModify | Unset): A schema for creating/modifying a server group Example:
            {'server_group': {'title': 'edge-cluster-a', 'servers': {'servers':
            ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'labels': {'label': [{'key': 'env', 'value':
            'prod'}]}, 'anti_affinity': 'yes'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerGroup | ServerGroupError
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
    body: ServerGroupModify | Unset = UNSET,
) -> Response[ServerGroup | ServerGroupError]:
    """Modify server group

     Modifies an existing server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerGroupModify | Unset): A schema for creating/modifying a server group Example:
            {'server_group': {'title': 'edge-cluster-a', 'servers': {'servers':
            ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'labels': {'label': [{'key': 'env', 'value':
            'prod'}]}, 'anti_affinity': 'yes'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerGroup | ServerGroupError]
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
    body: ServerGroupModify | Unset = UNSET,
) -> ServerGroup | ServerGroupError | None:
    """Modify server group

     Modifies an existing server group.

    Args:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        body (ServerGroupModify | Unset): A schema for creating/modifying a server group Example:
            {'server_group': {'title': 'edge-cluster-a', 'servers': {'servers':
            ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'labels': {'label': [{'key': 'env', 'value':
            'prod'}]}, 'anti_affinity': 'yes'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerGroup | ServerGroupError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
