from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_label_create import LoadBalancerLabelCreate
from ...models.load_balancer_label_response import LoadBalancerLabelResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bundle_uuid: UUID,
    *,
    body: LoadBalancerLabelCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/load-balancer/certificate-bundles/{bundle_uuid}/labels".format(
            bundle_uuid=quote(str(bundle_uuid), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerLabelResponse:
    if response.status_code == 201:
        response_201 = LoadBalancerLabelResponse.from_dict(response.json())

        return response_201

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerLabelCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]:
    """Create load balancer certificate bundle label

     Creates a new label by given {bundle-uuid}.

    Labels used for certificate bundles filtering.

    Certificate bundle labels usage examples
    Below are some examples of what certain GET requests might look like.

    exact match: GET /1.3/load-balancer/certificate-bundles?label=env%3Dstaging
    existence: GET /1.3/load-balancer/certificate-bundles?label=env
    multiple: GET /1.3/load-balancer/certificate-bundles?label=env&label=foo%3Dbar

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        body (LoadBalancerLabelCreate | Unset): Load Balancer Label Example: {'key':
            'environment', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]
    """

    kwargs = _get_kwargs(
        bundle_uuid=bundle_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerLabelCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerLabelResponse | None:
    """Create load balancer certificate bundle label

     Creates a new label by given {bundle-uuid}.

    Labels used for certificate bundles filtering.

    Certificate bundle labels usage examples
    Below are some examples of what certain GET requests might look like.

    exact match: GET /1.3/load-balancer/certificate-bundles?label=env%3Dstaging
    existence: GET /1.3/load-balancer/certificate-bundles?label=env
    multiple: GET /1.3/load-balancer/certificate-bundles?label=env&label=foo%3Dbar

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        body (LoadBalancerLabelCreate | Unset): Load Balancer Label Example: {'key':
            'environment', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerLabelResponse
    """

    return sync_detailed(
        bundle_uuid=bundle_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerLabelCreate | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]:
    """Create load balancer certificate bundle label

     Creates a new label by given {bundle-uuid}.

    Labels used for certificate bundles filtering.

    Certificate bundle labels usage examples
    Below are some examples of what certain GET requests might look like.

    exact match: GET /1.3/load-balancer/certificate-bundles?label=env%3Dstaging
    existence: GET /1.3/load-balancer/certificate-bundles?label=env
    multiple: GET /1.3/load-balancer/certificate-bundles?label=env&label=foo%3Dbar

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        body (LoadBalancerLabelCreate | Unset): Load Balancer Label Example: {'key':
            'environment', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]
    """

    kwargs = _get_kwargs(
        bundle_uuid=bundle_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerLabelCreate | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerLabelResponse | None:
    """Create load balancer certificate bundle label

     Creates a new label by given {bundle-uuid}.

    Labels used for certificate bundles filtering.

    Certificate bundle labels usage examples
    Below are some examples of what certain GET requests might look like.

    exact match: GET /1.3/load-balancer/certificate-bundles?label=env%3Dstaging
    existence: GET /1.3/load-balancer/certificate-bundles?label=env
    multiple: GET /1.3/load-balancer/certificate-bundles?label=env&label=foo%3Dbar

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        body (LoadBalancerLabelCreate | Unset): Load Balancer Label Example: {'key':
            'environment', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerLabelResponse
    """

    return (
        await asyncio_detailed(
            bundle_uuid=bundle_uuid,
            client=client,
            body=body,
        )
    ).parsed
