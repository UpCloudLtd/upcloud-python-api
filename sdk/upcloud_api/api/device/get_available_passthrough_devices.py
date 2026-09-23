from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.device_error import DeviceError
from ...models.devices import Devices
from ...models.get_available_passthrough_devices_type import GetAvailablePassthroughDevicesType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    zone: str | Unset = UNSET,
    type_: GetAvailablePassthroughDevicesType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["zone"] = zone

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/device/availability",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeviceError | Devices:
    if response.status_code == 200:
        response_200 = Devices.from_dict(response.json())

        return response_200

    response_default = DeviceError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeviceError | Devices]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone: str | Unset = UNSET,
    type_: GetAvailablePassthroughDevicesType | Unset = UNSET,
) -> Response[DeviceError | Devices]:
    """Get available passthrough devices

     Returns a list of available passthrough devices.

    Args:
        zone (str | Unset):
        type_ (GetAvailablePassthroughDevicesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeviceError | Devices]
    """

    kwargs = _get_kwargs(
        zone=zone,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    zone: str | Unset = UNSET,
    type_: GetAvailablePassthroughDevicesType | Unset = UNSET,
) -> DeviceError | Devices | None:
    """Get available passthrough devices

     Returns a list of available passthrough devices.

    Args:
        zone (str | Unset):
        type_ (GetAvailablePassthroughDevicesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeviceError | Devices
    """

    return sync_detailed(
        client=client,
        zone=zone,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone: str | Unset = UNSET,
    type_: GetAvailablePassthroughDevicesType | Unset = UNSET,
) -> Response[DeviceError | Devices]:
    """Get available passthrough devices

     Returns a list of available passthrough devices.

    Args:
        zone (str | Unset):
        type_ (GetAvailablePassthroughDevicesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeviceError | Devices]
    """

    kwargs = _get_kwargs(
        zone=zone,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    zone: str | Unset = UNSET,
    type_: GetAvailablePassthroughDevicesType | Unset = UNSET,
) -> DeviceError | Devices | None:
    """Get available passthrough devices

     Returns a list of available passthrough devices.

    Args:
        zone (str | Unset):
        type_ (GetAvailablePassthroughDevicesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeviceError | Devices
    """

    return (
        await asyncio_detailed(
            client=client,
            zone=zone,
            type_=type_,
        )
    ).parsed
