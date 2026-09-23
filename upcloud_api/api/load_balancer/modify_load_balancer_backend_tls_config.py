from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_tls_config import LoadBalancerTlsConfig
from ...models.load_balancer_tls_config_modify import LoadBalancerTlsConfigModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    body: LoadBalancerTlsConfigModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/load-balancer/{service_uuid}/backends/{backend_name}/tls-configs/{tls_config_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            backend_name=quote(str(backend_name), safe=""),
            tls_config_name=quote(str(tls_config_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerTlsConfig:
    if response.status_code == 200:
        response_200 = LoadBalancerTlsConfig.from_dict(response.json())

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerTlsConfig]:
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
    body: LoadBalancerTlsConfigModify | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerTlsConfig]:
    """Modify load balancer backend TLS config

     Modifies existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.
        body (LoadBalancerTlsConfigModify | Unset): Load Balancer TLS Config Example: {'name':
            'tls-config-1', 'certificate_bundle_uuid': '123e4567-e89b-12d3-a456-426614174000'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerTlsConfig]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        backend_name=backend_name,
        tls_config_name=tls_config_name,
        body=body,
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
    body: LoadBalancerTlsConfigModify | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerTlsConfig | None:
    """Modify load balancer backend TLS config

     Modifies existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.
        body (LoadBalancerTlsConfigModify | Unset): Load Balancer TLS Config Example: {'name':
            'tls-config-1', 'certificate_bundle_uuid': '123e4567-e89b-12d3-a456-426614174000'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerTlsConfig
    """

    return sync_detailed(
        service_uuid=service_uuid,
        backend_name=backend_name,
        tls_config_name=tls_config_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerTlsConfigModify | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerTlsConfig]:
    """Modify load balancer backend TLS config

     Modifies existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.
        body (LoadBalancerTlsConfigModify | Unset): Load Balancer TLS Config Example: {'name':
            'tls-config-1', 'certificate_bundle_uuid': '123e4567-e89b-12d3-a456-426614174000'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerTlsConfig]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        backend_name=backend_name,
        tls_config_name=tls_config_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    backend_name: str,
    tls_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerTlsConfigModify | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerTlsConfig | None:
    """Modify load balancer backend TLS config

     Modifies existing TLS config by given {service-uuid}, {backend-name}, and {tls-config-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        tls_config_name (str): The name of the TLS configuration.
        body (LoadBalancerTlsConfigModify | Unset): Load Balancer TLS Config Example: {'name':
            'tls-config-1', 'certificate_bundle_uuid': '123e4567-e89b-12d3-a456-426614174000'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerTlsConfig
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            backend_name=backend_name,
            tls_config_name=tls_config_name,
            client=client,
            body=body,
        )
    ).parsed
