from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.server_label import ServerLabel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/server/labels",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServerError | list[ServerLabel]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasget_all_server_labels_item_data in _response_200:
            componentsschemasget_all_server_labels_item = ServerLabel.from_dict(
                componentsschemasget_all_server_labels_item_data
            )

            response_200.append(componentsschemasget_all_server_labels_item)

        return response_200

    response_default = ServerError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServerError | list[ServerLabel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerError | list[ServerLabel]]:
    """List Cloud Server labels

     Returns the unique label key-value pairs used by Cloud Servers accessible to the current account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | list[ServerLabel]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ServerError | list[ServerLabel] | None:
    """List Cloud Server labels

     Returns the unique label key-value pairs used by Cloud Servers accessible to the current account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | list[ServerLabel]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ServerError | list[ServerLabel]]:
    """List Cloud Server labels

     Returns the unique label key-value pairs used by Cloud Servers accessible to the current account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerError | list[ServerLabel]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ServerError | list[ServerLabel] | None:
    """List Cloud Server labels

     Returns the unique label key-value pairs used by Cloud Servers accessible to the current account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerError | list[ServerLabel]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
