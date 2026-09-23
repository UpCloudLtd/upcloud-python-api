import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.account_error import AccountError
from ...models.account_resource_network_usage import AccountResourceNetworkUsage
from ...models.account_resource_network_usage_type import AccountResourceNetworkUsageType
from ...models.account_usage_accumulate_parameter import AccountUsageAccumulateParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.datetime,
    to: datetime.datetime,
    service: AccountResourceNetworkUsageType | Unset = UNSET,
    zone: str | Unset = UNSET,
    accumulate: AccountUsageAccumulateParameter | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    json_service: str | Unset = UNSET
    if not isinstance(service, Unset):
        json_service = service.value

    params["service"] = json_service

    params["zone"] = zone

    json_accumulate: str | Unset = UNSET
    if not isinstance(accumulate, Unset):
        json_accumulate = accumulate.value

    params["accumulate"] = json_accumulate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/account/network_top_usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountError | AccountResourceNetworkUsage:
    if response.status_code == 200:
        response_200 = AccountResourceNetworkUsage.from_dict(response.json())

        return response_200

    response_default = AccountError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountError | AccountResourceNetworkUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    service: AccountResourceNetworkUsageType | Unset = UNSET,
    zone: str | Unset = UNSET,
    accumulate: AccountUsageAccumulateParameter | Unset = UNSET,
) -> Response[AccountError | AccountResourceNetworkUsage]:
    """Get top network usage

     Returns the resources with the highest network usage.

    Args:
        from_ (datetime.datetime): Datetime in RFC 3339 format
        to (datetime.datetime): Datetime in RFC 3339 format
        service (AccountResourceNetworkUsageType | Unset): Network usage type for resource
        zone (str | Unset): Zone identifier
        accumulate (AccountUsageAccumulateParameter | Unset): Usage accumulator hour or day
            parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | AccountResourceNetworkUsage]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        service=service,
        zone=zone,
        accumulate=accumulate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    service: AccountResourceNetworkUsageType | Unset = UNSET,
    zone: str | Unset = UNSET,
    accumulate: AccountUsageAccumulateParameter | Unset = UNSET,
) -> AccountError | AccountResourceNetworkUsage | None:
    """Get top network usage

     Returns the resources with the highest network usage.

    Args:
        from_ (datetime.datetime): Datetime in RFC 3339 format
        to (datetime.datetime): Datetime in RFC 3339 format
        service (AccountResourceNetworkUsageType | Unset): Network usage type for resource
        zone (str | Unset): Zone identifier
        accumulate (AccountUsageAccumulateParameter | Unset): Usage accumulator hour or day
            parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | AccountResourceNetworkUsage
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        service=service,
        zone=zone,
        accumulate=accumulate,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    service: AccountResourceNetworkUsageType | Unset = UNSET,
    zone: str | Unset = UNSET,
    accumulate: AccountUsageAccumulateParameter | Unset = UNSET,
) -> Response[AccountError | AccountResourceNetworkUsage]:
    """Get top network usage

     Returns the resources with the highest network usage.

    Args:
        from_ (datetime.datetime): Datetime in RFC 3339 format
        to (datetime.datetime): Datetime in RFC 3339 format
        service (AccountResourceNetworkUsageType | Unset): Network usage type for resource
        zone (str | Unset): Zone identifier
        accumulate (AccountUsageAccumulateParameter | Unset): Usage accumulator hour or day
            parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountError | AccountResourceNetworkUsage]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        service=service,
        zone=zone,
        accumulate=accumulate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime,
    to: datetime.datetime,
    service: AccountResourceNetworkUsageType | Unset = UNSET,
    zone: str | Unset = UNSET,
    accumulate: AccountUsageAccumulateParameter | Unset = UNSET,
) -> AccountError | AccountResourceNetworkUsage | None:
    """Get top network usage

     Returns the resources with the highest network usage.

    Args:
        from_ (datetime.datetime): Datetime in RFC 3339 format
        to (datetime.datetime): Datetime in RFC 3339 format
        service (AccountResourceNetworkUsageType | Unset): Network usage type for resource
        zone (str | Unset): Zone identifier
        accumulate (AccountUsageAccumulateParameter | Unset): Usage accumulator hour or day
            parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountError | AccountResourceNetworkUsage
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            service=service,
            zone=zone,
            accumulate=accumulate,
        )
    ).parsed
