from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...types import Response


def _get_kwargs(
    bundle_uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/load-balancer/certificate-bundles/{bundle_uuid}".format(
            bundle_uuid=quote(str(bundle_uuid), safe=""),
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
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LoadBalancerErrorResponse]:
    """Delete load balancer certificate bundle

     Deletes existing certificate bundle by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LoadBalancerErrorResponse]
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
) -> Any | LoadBalancerErrorResponse | None:
    """Delete load balancer certificate bundle

     Deletes existing certificate bundle by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LoadBalancerErrorResponse
    """

    return sync_detailed(
        bundle_uuid=bundle_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    bundle_uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LoadBalancerErrorResponse]:
    """Delete load balancer certificate bundle

     Deletes existing certificate bundle by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LoadBalancerErrorResponse]
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
) -> Any | LoadBalancerErrorResponse | None:
    """Delete load balancer certificate bundle

     Deletes existing certificate bundle by given {bundle-uuid}.

    Args:
        bundle_uuid (UUID): The UUID of the certificate bundle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LoadBalancerErrorResponse
    """

    return (
        await asyncio_detailed(
            bundle_uuid=bundle_uuid,
            client=client,
        )
    ).parsed
