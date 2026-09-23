from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_certificate_bundle import LoadBalancerCertificateBundle
from ...models.load_balancer_certificate_bundle_create_type_0 import LoadBalancerCertificateBundleCreateType0
from ...models.load_balancer_certificate_bundle_create_type_1 import LoadBalancerCertificateBundleCreateType1
from ...models.load_balancer_certificate_bundle_create_type_2 import LoadBalancerCertificateBundleCreateType2
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LoadBalancerCertificateBundleCreateType0
    | LoadBalancerCertificateBundleCreateType1
    | LoadBalancerCertificateBundleCreateType2
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/load-balancer/certificate-bundles",
    }

    if isinstance(body, LoadBalancerCertificateBundleCreateType0):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, LoadBalancerCertificateBundleCreateType1):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerCertificateBundle | LoadBalancerErrorResponse:
    if response.status_code == 201:
        response_201 = LoadBalancerCertificateBundle.from_dict(response.json())

        return response_201

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerCertificateBundle | LoadBalancerErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerCertificateBundleCreateType0
    | LoadBalancerCertificateBundleCreateType1
    | LoadBalancerCertificateBundleCreateType2
    | Unset = UNSET,
) -> Response[LoadBalancerCertificateBundle | LoadBalancerErrorResponse]:
    """Create load balancer certificate bundle

     Creates a new certificate bundle.

    Args:
        body (LoadBalancerCertificateBundleCreateType0 | LoadBalancerCertificateBundleCreateType1
            | LoadBalancerCertificateBundleCreateType2 | Unset): Load Balancer certificate bundle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerCertificateBundle | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerCertificateBundleCreateType0
    | LoadBalancerCertificateBundleCreateType1
    | LoadBalancerCertificateBundleCreateType2
    | Unset = UNSET,
) -> LoadBalancerCertificateBundle | LoadBalancerErrorResponse | None:
    """Create load balancer certificate bundle

     Creates a new certificate bundle.

    Args:
        body (LoadBalancerCertificateBundleCreateType0 | LoadBalancerCertificateBundleCreateType1
            | LoadBalancerCertificateBundleCreateType2 | Unset): Load Balancer certificate bundle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerCertificateBundle | LoadBalancerErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerCertificateBundleCreateType0
    | LoadBalancerCertificateBundleCreateType1
    | LoadBalancerCertificateBundleCreateType2
    | Unset = UNSET,
) -> Response[LoadBalancerCertificateBundle | LoadBalancerErrorResponse]:
    """Create load balancer certificate bundle

     Creates a new certificate bundle.

    Args:
        body (LoadBalancerCertificateBundleCreateType0 | LoadBalancerCertificateBundleCreateType1
            | LoadBalancerCertificateBundleCreateType2 | Unset): Load Balancer certificate bundle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerCertificateBundle | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerCertificateBundleCreateType0
    | LoadBalancerCertificateBundleCreateType1
    | LoadBalancerCertificateBundleCreateType2
    | Unset = UNSET,
) -> LoadBalancerCertificateBundle | LoadBalancerErrorResponse | None:
    """Create load balancer certificate bundle

     Creates a new certificate bundle.

    Args:
        body (LoadBalancerCertificateBundleCreateType0 | LoadBalancerCertificateBundleCreateType1
            | LoadBalancerCertificateBundleCreateType2 | Unset): Load Balancer certificate bundle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerCertificateBundle | LoadBalancerErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
