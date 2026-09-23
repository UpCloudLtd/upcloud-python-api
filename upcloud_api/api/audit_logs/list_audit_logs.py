import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.audit_logs_actions_parameter_item import AuditLogsActionsParameterItem
from ...models.audit_logs_error_response import AuditLogsErrorResponse
from ...models.audit_logs_origins_parameter_item import AuditLogsOriginsParameterItem
from ...models.audit_logs_resource_types_parameter_item import AuditLogsResourceTypesParameterItem
from ...models.audit_logs_response import AuditLogsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    actions: list[AuditLogsActionsParameterItem] | Unset = UNSET,
    origins: list[AuditLogsOriginsParameterItem] | Unset = UNSET,
    resource_types: list[AuditLogsResourceTypesParameterItem] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["offset"] = offset

    json_actions: list[str] | Unset = UNSET
    if not isinstance(actions, Unset):
        json_actions = []
        for componentsschemasaudit_logs_actions_parameter_item_data in actions:
            componentsschemasaudit_logs_actions_parameter_item = (
                componentsschemasaudit_logs_actions_parameter_item_data.value
            )
            json_actions.append(componentsschemasaudit_logs_actions_parameter_item)

    params["actions"] = json_actions

    json_origins: list[str] | Unset = UNSET
    if not isinstance(origins, Unset):
        json_origins = []
        for componentsschemasaudit_logs_origins_parameter_item_data in origins:
            componentsschemasaudit_logs_origins_parameter_item = (
                componentsschemasaudit_logs_origins_parameter_item_data.value
            )
            json_origins.append(componentsschemasaudit_logs_origins_parameter_item)

    params["origins"] = json_origins

    json_resource_types: list[str] | Unset = UNSET
    if not isinstance(resource_types, Unset):
        json_resource_types = []
        for componentsschemasaudit_logs_resource_types_parameter_item_data in resource_types:
            componentsschemasaudit_logs_resource_types_parameter_item = (
                componentsschemasaudit_logs_resource_types_parameter_item_data.value
            )
            json_resource_types.append(componentsschemasaudit_logs_resource_types_parameter_item)

    params["resource_types"] = json_resource_types

    json_created_after: str | Unset = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created_after"] = json_created_after

    json_created_before: str | Unset = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/audit-logs",
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
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    actions: list[AuditLogsActionsParameterItem] | Unset = UNSET,
    origins: list[AuditLogsOriginsParameterItem] | Unset = UNSET,
    resource_types: list[AuditLogsResourceTypesParameterItem] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
) -> Response[AuditLogsErrorResponse | AuditLogsResponse]:
    """List audit logs

     Returns a list of audit log rows according to the query parameters. Note that this endpoint is
    paginated by default and the list is limited in results.

    Pagination
    Upcloud-Total-Count header is included in the response to indicate the total number of audit logs
    available with the current query parameters (excluding limit and offset). The total count can be
    used for a number of pagination strategies. limit and offset query parameters can be used to finally
    paginate the results.

    Args:
        q (str | Unset): Search string
        limit (int | Unset): Number of results to return
        offset (int | Unset): Page for retrieved results. Note: 0 and 1 retrieve the same first
            page results. (default 0)
        actions (list[AuditLogsActionsParameterItem] | Unset): List of actions to filter by
        origins (list[AuditLogsOriginsParameterItem] | Unset): List of origins to filter by
        resource_types (list[AuditLogsResourceTypesParameterItem] | Unset): List of resource types
            to filter by
        created_after (datetime.datetime | Unset): List audit logs created after the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z
        created_before (datetime.datetime | Unset): List audit logs created before the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsErrorResponse | AuditLogsResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        offset=offset,
        actions=actions,
        origins=origins,
        resource_types=resource_types,
        created_after=created_after,
        created_before=created_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    actions: list[AuditLogsActionsParameterItem] | Unset = UNSET,
    origins: list[AuditLogsOriginsParameterItem] | Unset = UNSET,
    resource_types: list[AuditLogsResourceTypesParameterItem] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
) -> AuditLogsErrorResponse | AuditLogsResponse | None:
    """List audit logs

     Returns a list of audit log rows according to the query parameters. Note that this endpoint is
    paginated by default and the list is limited in results.

    Pagination
    Upcloud-Total-Count header is included in the response to indicate the total number of audit logs
    available with the current query parameters (excluding limit and offset). The total count can be
    used for a number of pagination strategies. limit and offset query parameters can be used to finally
    paginate the results.

    Args:
        q (str | Unset): Search string
        limit (int | Unset): Number of results to return
        offset (int | Unset): Page for retrieved results. Note: 0 and 1 retrieve the same first
            page results. (default 0)
        actions (list[AuditLogsActionsParameterItem] | Unset): List of actions to filter by
        origins (list[AuditLogsOriginsParameterItem] | Unset): List of origins to filter by
        resource_types (list[AuditLogsResourceTypesParameterItem] | Unset): List of resource types
            to filter by
        created_after (datetime.datetime | Unset): List audit logs created after the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z
        created_before (datetime.datetime | Unset): List audit logs created before the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsErrorResponse | AuditLogsResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
        offset=offset,
        actions=actions,
        origins=origins,
        resource_types=resource_types,
        created_after=created_after,
        created_before=created_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    actions: list[AuditLogsActionsParameterItem] | Unset = UNSET,
    origins: list[AuditLogsOriginsParameterItem] | Unset = UNSET,
    resource_types: list[AuditLogsResourceTypesParameterItem] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
) -> Response[AuditLogsErrorResponse | AuditLogsResponse]:
    """List audit logs

     Returns a list of audit log rows according to the query parameters. Note that this endpoint is
    paginated by default and the list is limited in results.

    Pagination
    Upcloud-Total-Count header is included in the response to indicate the total number of audit logs
    available with the current query parameters (excluding limit and offset). The total count can be
    used for a number of pagination strategies. limit and offset query parameters can be used to finally
    paginate the results.

    Args:
        q (str | Unset): Search string
        limit (int | Unset): Number of results to return
        offset (int | Unset): Page for retrieved results. Note: 0 and 1 retrieve the same first
            page results. (default 0)
        actions (list[AuditLogsActionsParameterItem] | Unset): List of actions to filter by
        origins (list[AuditLogsOriginsParameterItem] | Unset): List of origins to filter by
        resource_types (list[AuditLogsResourceTypesParameterItem] | Unset): List of resource types
            to filter by
        created_after (datetime.datetime | Unset): List audit logs created after the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z
        created_before (datetime.datetime | Unset): List audit logs created before the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogsErrorResponse | AuditLogsResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
        offset=offset,
        actions=actions,
        origins=origins,
        resource_types=resource_types,
        created_after=created_after,
        created_before=created_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    actions: list[AuditLogsActionsParameterItem] | Unset = UNSET,
    origins: list[AuditLogsOriginsParameterItem] | Unset = UNSET,
    resource_types: list[AuditLogsResourceTypesParameterItem] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
) -> AuditLogsErrorResponse | AuditLogsResponse | None:
    """List audit logs

     Returns a list of audit log rows according to the query parameters. Note that this endpoint is
    paginated by default and the list is limited in results.

    Pagination
    Upcloud-Total-Count header is included in the response to indicate the total number of audit logs
    available with the current query parameters (excluding limit and offset). The total count can be
    used for a number of pagination strategies. limit and offset query parameters can be used to finally
    paginate the results.

    Args:
        q (str | Unset): Search string
        limit (int | Unset): Number of results to return
        offset (int | Unset): Page for retrieved results. Note: 0 and 1 retrieve the same first
            page results. (default 0)
        actions (list[AuditLogsActionsParameterItem] | Unset): List of actions to filter by
        origins (list[AuditLogsOriginsParameterItem] | Unset): List of origins to filter by
        resource_types (list[AuditLogsResourceTypesParameterItem] | Unset): List of resource types
            to filter by
        created_after (datetime.datetime | Unset): List audit logs created after the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z
        created_before (datetime.datetime | Unset): List audit logs created before the given
            timestamp (including the time of timestamp). Format: ISO timestamp eg.
            2024-01-01T23:45:56Z

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogsErrorResponse | AuditLogsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
            offset=offset,
            actions=actions,
            origins=origins,
            resource_types=resource_types,
            created_after=created_after,
            created_before=created_before,
        )
    ).parsed
