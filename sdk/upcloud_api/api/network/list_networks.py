from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.network_error import NetworkError
from ...models.network_label import NetworkLabel
from ...models.networks import Networks
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label: NetworkLabel | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_label: dict[str, Any] | Unset = UNSET
    if not isinstance(label, Unset):
        json_label = label.to_dict()
    if not isinstance(json_label, Unset):
        params.update(json_label)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/network",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> NetworkError | Networks:
    if response.status_code == 200:
        response_200 = Networks.from_dict(response.json())

        return response_200

    response_default = NetworkError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NetworkError | Networks]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: NetworkLabel | Unset = UNSET,
) -> Response[NetworkError | Networks]:
    """List networks

     Get a list of all networks.

    It is also possible to filter networks with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only networks that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (NetworkLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkError | Networks]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    label: NetworkLabel | Unset = UNSET,
) -> NetworkError | Networks | None:
    """List networks

     Get a list of all networks.

    It is also possible to filter networks with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only networks that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (NetworkLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkError | Networks
    """

    return sync_detailed(
        client=client,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: NetworkLabel | Unset = UNSET,
) -> Response[NetworkError | Networks]:
    """List networks

     Get a list of all networks.

    It is also possible to filter networks with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only networks that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (NetworkLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NetworkError | Networks]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    label: NetworkLabel | Unset = UNSET,
) -> NetworkError | Networks | None:
    """List networks

     Get a list of all networks.

    It is also possible to filter networks with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only networks that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (NetworkLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NetworkError | Networks
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
        )
    ).parsed
