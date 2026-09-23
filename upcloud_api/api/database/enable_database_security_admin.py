from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_open_search_security_plugin_status_response import (
    DatabaseOpenSearchSecurityPluginStatusResponse,
)
from ...models.database_service_security_enable import DatabaseServiceSecurityEnable
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: DatabaseServiceSecurityEnable | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/database/{uuid}/security/admin".format(
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
) -> DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse:
    if response.status_code == 201:
        response_201 = DatabaseOpenSearchSecurityPluginStatusResponse.from_dict(response.json())

        return response_201

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse]:
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
    body: DatabaseServiceSecurityEnable | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse]:
    """Enable Security management admin (OpenSearch)

     Enables Security management admin for the OpenSearch Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceSecurityEnable | Unset): Schema for enabling security on a service
            instance

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse]
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
    body: DatabaseServiceSecurityEnable | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse | None:
    """Enable Security management admin (OpenSearch)

     Enables Security management admin for the OpenSearch Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceSecurityEnable | Unset): Schema for enabling security on a service
            instance

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse
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
    body: DatabaseServiceSecurityEnable | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse]:
    """Enable Security management admin (OpenSearch)

     Enables Security management admin for the OpenSearch Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceSecurityEnable | Unset): Schema for enabling security on a service
            instance

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse]
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
    body: DatabaseServiceSecurityEnable | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse | None:
    """Enable Security management admin (OpenSearch)

     Enables Security management admin for the OpenSearch Managed Database service {uuid}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        body (DatabaseServiceSecurityEnable | Unset): Schema for enabling security on a service
            instance

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseOpenSearchSecurityPluginStatusResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
