from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.audit_logs_error_response import AuditLogsErrorResponse
from ...models.audit_logs_filter_options_response import AuditLogsFilterOptionsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/audit-logs/filter-options",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditLogsErrorResponse | AuditLogsFilterOptionsResponse:
    if response.status_code == 200:
        response_200 = AuditLogsFilterOptionsResponse.from_dict(response.json())

        return response_200

    response_default = AuditLogsErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditLogsErrorResponse | AuditLogsFilterOptionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AuditLogsErrorResponse | AuditLogsFilterOptionsResponse]:
    """Get filter options

     Returns lists of available resource types, actions, and origins for filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsErrorResponse | AuditLogsFilterOptionsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> AuditLogsErrorResponse | AuditLogsFilterOptionsResponse | None:
    """Get filter options

     Returns lists of available resource types, actions, and origins for filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsErrorResponse | AuditLogsFilterOptionsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AuditLogsErrorResponse | AuditLogsFilterOptionsResponse]:
    """Get filter options

     Returns lists of available resource types, actions, and origins for filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsErrorResponse | AuditLogsFilterOptionsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> AuditLogsErrorResponse | AuditLogsFilterOptionsResponse | None:
    """Get filter options

     Returns lists of available resource types, actions, and origins for filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsErrorResponse | AuditLogsFilterOptionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
