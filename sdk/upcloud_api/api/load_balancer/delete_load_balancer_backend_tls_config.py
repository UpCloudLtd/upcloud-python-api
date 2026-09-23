from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/load-balancer/{service_uuid}/backends/{backend_name}/tls-configs/{tls_config_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            backend_name=quote(str(backend_name), safe=""),
            tls_config_name=quote(str(tls_config_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LoadBalancerErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LoadBalancerErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LoadBalancerErrorResponse]:
    """Delete load balancer backend TLS config

     Deletes existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        backend_name=backend_name,
        tls_config_name=tls_config_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LoadBalancerErrorResponse | None:
    """Delete load balancer backend TLS config

     Deletes existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LoadBalancerErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        backend_name=backend_name,
        tls_config_name=tls_config_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LoadBalancerErrorResponse]:
    """Delete load balancer backend TLS config

     Deletes existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        backend_name=backend_name,
        tls_config_name=tls_config_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LoadBalancerErrorResponse | None:
    """Delete load balancer backend TLS config

     Deletes existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LoadBalancerErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            backend_name=backend_name,
            tls_config_name=tls_config_name,
            client=client,
        )
    ).parsed
