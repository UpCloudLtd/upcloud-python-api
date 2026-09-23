from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_rule import LoadBalancerRule
from ...models.load_balancer_rule_create import LoadBalancerRuleCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    frontend_name: str,
    *,
    body: LoadBalancerRuleCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/load-balancer/{service_uuid}/frontends/{frontend_name}/rules".format(
            service_uuid=quote(str(service_uuid), safe=""),
            frontend_name=quote(str(frontend_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerRule:
    if response.status_code == 201:
        response_201 = LoadBalancerRule.from_dict(response.json())

        return response_201

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerRuleCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerRule]:
    """Create load balancer rule

     Creates a new rule by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        body (LoadBalancerRuleCreate | Unset): Load Balancer Forwarding Rule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerRule]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerRuleCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerRule | None:
    """Create load balancer rule

     Creates a new rule by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        body (LoadBalancerRuleCreate | Unset): Load Balancer Forwarding Rule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerRule
    """

    return sync_detailed(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerRuleCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerRule]:
    """Create load balancer rule

     Creates a new rule by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        body (LoadBalancerRuleCreate | Unset): Load Balancer Forwarding Rule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerRule]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        frontend_name=frontend_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    frontend_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerRuleCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerRule | None:
    """Create load balancer rule

     Creates a new rule by given {service-uuid} and {frontend-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        frontend_name (str): The name of the frontend.
        body (LoadBalancerRuleCreate | Unset): Load Balancer Forwarding Rule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerRule
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            frontend_name=frontend_name,
            client=client,
            body=body,
        )
    ).parsed
