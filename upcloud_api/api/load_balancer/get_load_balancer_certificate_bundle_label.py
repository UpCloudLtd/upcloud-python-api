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
    label_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/certificate-bundles/{bundle_uuid}/labels/{label_key}".format(
            bundle_uuid=quote(str(bundle_uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerLabelResponse:
    if response.status_code == 200:
        response_200 = LoadBalancerLabelResponse.from_dict(response.json())

        return response_200

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
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]:
    """Get load balancer certificate bundle label

     Returns label details by given {bundle-uuid} and {label-key}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        label_key (str): The label key parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]
    """

    kwargs = _get_kwargs(
        bundle_uuid=bundle_uuid,
        label_key=label_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | LoadBalancerLabelResponse | None:
    """Get load balancer certificate bundle label

     Returns label details by given {bundle-uuid} and {label-key}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        label_key (str): The label key parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerLabelResponse
    """

    return sync_detailed(
        bundle_uuid=bundle_uuid,
        label_key=label_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    bundle_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]:
    """Get load balancer certificate bundle label

     Returns label details by given {bundle-uuid} and {label-key}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        label_key (str): The label key parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerLabelResponse]
    """

    kwargs = _get_kwargs(
        bundle_uuid=bundle_uuid,
        label_key=label_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerErrorResponse | LoadBalancerLabelResponse | None:
    """Get load balancer certificate bundle label

     Returns label details by given {bundle-uuid} and {label-key}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.
        label_key (str): The label key parameter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerLabelResponse
    """

    return (
        await asyncio_detailed(
            bundle_uuid=bundle_uuid,
            label_key=label_key,
            client=client,
        )
    ).parsed
