from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_backend import LoadBalancerBackend
from ...models.load_balancer_backend_create import LoadBalancerBackendCreate
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    *,
    body: LoadBalancerBackendCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/load-balancer/{service_uuid}/backends".format(
            service_uuid=quote(str(service_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerBackend | LoadBalancerErrorResponse:
    if response.status_code == 201:
        response_201 = LoadBalancerBackend.from_dict(response.json())

        return response_201

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerBackend | LoadBalancerErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerBackendCreate | Unset = UNSET,
) -> Response[LoadBalancerBackend | LoadBalancerErrorResponse]:
    """Create load balancer backend

     Creates a new backend by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerBackendCreate | Unset): Load Balancer Backend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerBackend | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerBackendCreate | Unset = UNSET,
) -> LoadBalancerBackend | LoadBalancerErrorResponse | None:
    """Create load balancer backend

     Creates a new backend by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerBackendCreate | Unset): Load Balancer Backend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerBackend | LoadBalancerErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerBackendCreate | Unset = UNSET,
) -> Response[LoadBalancerBackend | LoadBalancerErrorResponse]:
    """Create load balancer backend

     Creates a new backend by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerBackendCreate | Unset): Load Balancer Backend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerBackend | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerBackendCreate | Unset = UNSET,
) -> LoadBalancerBackend | LoadBalancerErrorResponse | None:
    """Create load balancer backend

     Creates a new backend by given {service-uuid}.

    Args:
        service_uuid (UUID): The UUID of the service.
        body (LoadBalancerBackendCreate | Unset): Load Balancer Backend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerBackend | LoadBalancerErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            client=client,
            body=body,
        )
    ).parsed
