from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_label_response import LoadBalancerLabelResponse
from ...types import Response


def _get_kwargs(
    bundle_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/certificate-bundles/{bundle_uuid}/labels".format(
            bundle_uuid=quote(str(bundle_uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemasload_balancer_certificate_bundle_labels_response_item_data in _response_200:
            componentsschemasload_balancer_certificate_bundle_labels_response_item = (
                LoadBalancerLabelResponse.from_dict(
                    componentsschemasload_balancer_certificate_bundle_labels_response_item_data
                )
            )

            response_200.append(componentsschemasload_balancer_certificate_bundle_labels_response_item)

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]]:
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
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]]:
    """List load balancer certificate bundle labels

     Returns a list of available certificate bundle labels by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]]
    """

    kwargs = _get_kwargs(
        bundle_uuid=bundle_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerLabelResponse] | None:
    """List load balancer certificate bundle labels

     Returns a list of available certificate bundle labels by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]
    """

    return sync_detailed(
        bundle_uuid=bundle_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]]:
    """List load balancer certificate bundle labels

     Returns a list of available certificate bundle labels by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]]
    """

    kwargs = _get_kwargs(
        bundle_uuid=bundle_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | list[LoadBalancerLabelResponse] | None:
    """List load balancer certificate bundle labels

     Returns a list of available certificate bundle labels by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | list[LoadBalancerLabelResponse]
    """

    return (
        await asyncio_detailed(
            bundle_uuid=bundle_uuid,
            client=client,
        )
    ).parsed
