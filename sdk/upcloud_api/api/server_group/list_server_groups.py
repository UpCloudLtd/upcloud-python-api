from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_group_error import ServerGroupError
from ...models.server_group_label import ServerGroupLabel
from ...models.server_groups import ServerGroups
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label: ServerGroupLabel | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_label: dict[str, Any] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label.to_dict()
    if not isinstance(json_label, Unset):
        params.update(json_label)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/server-group",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerGroupError | ServerGroups:
    if response.status_code == 200:
        response_200 = ServerGroups.from_dict(response.json())

        return response_200

    response_default = ServerGroupError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServerGroupError | ServerGroups]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: ServerGroupLabel | Unset = UNSET,
) -> Response[ServerGroupError | ServerGroups]:
    """List server groups

     Retrieves a list of server groups.

    Args:
        label (ServerGroupLabel | Unset): A key/value pair to label and categorize resources
            Example: {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerGroupError | ServerGroups]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    label: ServerGroupLabel | Unset = UNSET,
) -> ServerGroupError | ServerGroups | None:
    """List server groups

     Retrieves a list of server groups.

    Args:
        label (ServerGroupLabel | Unset): A key/value pair to label and categorize resources
            Example: {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerGroupError | ServerGroups
    """

    return sync_detailed(
        client=client,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: ServerGroupLabel | Unset = UNSET,
) -> Response[ServerGroupError | ServerGroups]:
    """List server groups

     Retrieves a list of server groups.

    Args:
        label (ServerGroupLabel | Unset): A key/value pair to label and categorize resources
            Example: {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerGroupError | ServerGroups]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    label: ServerGroupLabel | Unset = UNSET,
) -> ServerGroupError | ServerGroups | None:
    """List server groups

     Retrieves a list of server groups.

    Args:
        label (ServerGroupLabel | Unset): A key/value pair to label and categorize resources
            Example: {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerGroupError | ServerGroups
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
        )
    ).parsed
