from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.gateway_error_response import GatewayErrorResponse
from ...models.gateway_label_modify_request import GatewayLabelModifyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    label_key: str,
    *,
    body: GatewayLabelModifyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/gateway/{service_uuid}/labels/{label_key}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GatewayErrorResponse:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    response_default = GatewayErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GatewayErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayLabelModifyRequest | Unset = UNSET,
) -> Response[Any | GatewayErrorResponse]:
    """Modify Service Label

     Modify service label configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        label_key (str): The key of a label.
        body (GatewayLabelModifyRequest | Unset): Gateway label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        label_key=label_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayLabelModifyRequest | Unset = UNSET,
) -> Any | GatewayErrorResponse | None:
    """Modify Service Label

     Modify service label configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        label_key (str): The key of a label.
        body (GatewayLabelModifyRequest | Unset): Gateway label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GatewayErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        label_key=label_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayLabelModifyRequest | Unset = UNSET,
) -> Response[Any | GatewayErrorResponse]:
    """Modify Service Label

     Modify service label configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        label_key (str): The key of a label.
        body (GatewayLabelModifyRequest | Unset): Gateway label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GatewayErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        label_key=label_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: GatewayLabelModifyRequest | Unset = UNSET,
) -> Any | GatewayErrorResponse | None:
    """Modify Service Label

     Modify service label configuration.

    Args:
        service_uuid (UUID): The unique identifier for the resource.
        label_key (str): The key of a label.
        body (GatewayLabelModifyRequest | Unset): Gateway label

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GatewayErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            label_key=label_key,
            client=client,
            body=body,
        )
    ).parsed
