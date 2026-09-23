from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_resolver import LoadBalancerResolver
from ...models.load_balancer_resolver_modify import LoadBalancerResolverModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    resolver_name: str,
    *,
    body: LoadBalancerResolverModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/load-balancer/{service_uuid}/resolvers/{resolver_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            resolver_name=quote(str(resolver_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerResolver:
    if response.status_code == 200:
        response_200 = LoadBalancerResolver.from_dict(response.json())

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerResolver]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    resolver_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerResolverModify | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerResolver]:
    """Modify load balancer resolver

     Modifies existing resolver by given {service-uuid} and {resolver-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        resolver_name (str): The name of the resolver.
        body (LoadBalancerResolverModify | Unset): Load Balancer Resolver Example: {'name':
            'default-resolver', 'nameservers': ['1.1.1.1:53', '8.8.8.8:53'], 'retries': 3, 'timeout':
            5, 'timeout_retry': 3, 'cache_valid': 300, 'cache_invalid': 60}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerResolver]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        resolver_name=resolver_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    resolver_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerResolverModify | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerResolver | None:
    """Modify load balancer resolver

     Modifies existing resolver by given {service-uuid} and {resolver-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        resolver_name (str): The name of the resolver.
        body (LoadBalancerResolverModify | Unset): Load Balancer Resolver Example: {'name':
            'default-resolver', 'nameservers': ['1.1.1.1:53', '8.8.8.8:53'], 'retries': 3, 'timeout':
            5, 'timeout_retry': 3, 'cache_valid': 300, 'cache_invalid': 60}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerResolver
    """

    return sync_detailed(
        service_uuid=service_uuid,
        resolver_name=resolver_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    resolver_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerResolverModify | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerResolver]:
    """Modify load balancer resolver

     Modifies existing resolver by given {service-uuid} and {resolver-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        resolver_name (str): The name of the resolver.
        body (LoadBalancerResolverModify | Unset): Load Balancer Resolver Example: {'name':
            'default-resolver', 'nameservers': ['1.1.1.1:53', '8.8.8.8:53'], 'retries': 3, 'timeout':
            5, 'timeout_retry': 3, 'cache_valid': 300, 'cache_invalid': 60}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerResolver]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        resolver_name=resolver_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    resolver_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerResolverModify | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerResolver | None:
    """Modify load balancer resolver

     Modifies existing resolver by given {service-uuid} and {resolver-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        resolver_name (str): The name of the resolver.
        body (LoadBalancerResolverModify | Unset): Load Balancer Resolver Example: {'name':
            'default-resolver', 'nameservers': ['1.1.1.1:53', '8.8.8.8:53'], 'retries': 3, 'timeout':
            5, 'timeout_retry': 3, 'cache_valid': 300, 'cache_invalid': 60}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerResolver
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            resolver_name=resolver_name,
            client=client,
            body=body,
        )
    ).parsed
