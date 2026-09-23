from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_project_alert_response import DatabaseProjectAlertResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/database/alerts",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | list[DatabaseProjectAlertResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasdatabase_project_alerts_response_item_data in _response_200:
            componentsschemasdatabase_project_alerts_response_item = DatabaseProjectAlertResponse.from_dict(
                componentsschemasdatabase_project_alerts_response_item_data
            )

            response_200.append(componentsschemasdatabase_project_alerts_response_item)

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | list[DatabaseProjectAlertResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseProjectAlertResponse]]:
    """List all alerts

     Returns all the alerts associated with your Managed Database services.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseProjectAlertResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabaseProjectAlertResponse] | None:
    """List all alerts

     Returns all the alerts associated with your Managed Database services.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseProjectAlertResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatabaseErrorResponse | list[DatabaseProjectAlertResponse]]:
    """List all alerts

     Returns all the alerts associated with your Managed Database services.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | list[DatabaseProjectAlertResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DatabaseErrorResponse | list[DatabaseProjectAlertResponse] | None:
    """List all alerts

     Returns all the alerts associated with your Managed Database services.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | list[DatabaseProjectAlertResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
