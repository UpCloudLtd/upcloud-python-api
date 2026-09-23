from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.audit_logs_audit_log import AuditLogsAuditLog
from ...models.audit_logs_error_response import AuditLogsErrorResponse
from ...types import Response


def _get_kwargs(
    cloud_event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/audit-logs/{cloud_event_id}".format(
            cloud_event_id=quote(str(cloud_event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditLogsAuditLog | AuditLogsErrorResponse:
    if response.status_code == 200:
        response_200 = AuditLogsAuditLog.from_dict(response.json())

        return response_200

    response_default = AuditLogsErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditLogsAuditLog | AuditLogsErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AuditLogsAuditLog | AuditLogsErrorResponse]:
    """Get event details

     Returns details of a single audit log event by its cloud event ID.

    Args:
        cloud_event_id (str): Cloud event ID (ULID format)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsAuditLog | AuditLogsErrorResponse]
    """

    kwargs = _get_kwargs(
        cloud_event_id=cloud_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cloud_event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AuditLogsAuditLog | AuditLogsErrorResponse | None:
    """Get event details

     Returns details of a single audit log event by its cloud event ID.

    Args:
        cloud_event_id (str): Cloud event ID (ULID format)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsAuditLog | AuditLogsErrorResponse
    """

    return sync_detailed(
        cloud_event_id=cloud_event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cloud_event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AuditLogsAuditLog | AuditLogsErrorResponse]:
    """Get event details

     Returns details of a single audit log event by its cloud event ID.

    Args:
        cloud_event_id (str): Cloud event ID (ULID format)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsAuditLog | AuditLogsErrorResponse]
    """

    kwargs = _get_kwargs(
        cloud_event_id=cloud_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cloud_event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AuditLogsAuditLog | AuditLogsErrorResponse | None:
    """Get event details

     Returns details of a single audit log event by its cloud event ID.

    Args:
        cloud_event_id (str): Cloud event ID (ULID format)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsAuditLog | AuditLogsErrorResponse
    """

    return (
        await asyncio_detailed(
            cloud_event_id=cloud_event_id,
            client=client,
        )
    ).parsed
