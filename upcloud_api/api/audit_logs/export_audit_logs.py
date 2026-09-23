from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.audit_logs_error_response import AuditLogsErrorResponse
from ...models.audit_logs_format_parameter import AuditLogsFormatParameter
from ...models.audit_logs_response import AuditLogsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: AuditLogsFormatParameter | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/audit-logs/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditLogsErrorResponse | AuditLogsResponse:
    if response.status_code == 200:
        response_200 = AuditLogsResponse.from_dict(response.json())

        return response_200

    response_default = AuditLogsErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditLogsErrorResponse | AuditLogsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    format_: AuditLogsFormatParameter | Unset = UNSET,
) -> Response[AuditLogsErrorResponse | AuditLogsResponse]:
    """Export audit logs

     Export all audit logs for the authenticated account as CSV or JSON (up to 180 day limit). Note: Use
    the format parameter to specify output format; only JSON schema is documented here.

    Args:
        format_ (AuditLogsFormatParameter | Unset): Export format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsErrorResponse | AuditLogsResponse]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    format_: AuditLogsFormatParameter | Unset = UNSET,
) -> AuditLogsErrorResponse | AuditLogsResponse | None:
    """Export audit logs

     Export all audit logs for the authenticated account as CSV or JSON (up to 180 day limit). Note: Use
    the format parameter to specify output format; only JSON schema is documented here.

    Args:
        format_ (AuditLogsFormatParameter | Unset): Export format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsErrorResponse | AuditLogsResponse
    """

    return sync_detailed(
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    format_: AuditLogsFormatParameter | Unset = UNSET,
) -> Response[AuditLogsErrorResponse | AuditLogsResponse]:
    """Export audit logs

     Export all audit logs for the authenticated account as CSV or JSON (up to 180 day limit). Note: Use
    the format parameter to specify output format; only JSON schema is documented here.

    Args:
        format_ (AuditLogsFormatParameter | Unset): Export format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsErrorResponse | AuditLogsResponse]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    format_: AuditLogsFormatParameter | Unset = UNSET,
) -> AuditLogsErrorResponse | AuditLogsResponse | None:
    """Export audit logs

     Export all audit logs for the authenticated account as CSV or JSON (up to 180 day limit). Note: Use
    the format parameter to specify output format; only JSON schema is documented here.

    Args:
        format_ (AuditLogsFormatParameter | Unset): Export format

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsErrorResponse | AuditLogsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
        )
    ).parsed
