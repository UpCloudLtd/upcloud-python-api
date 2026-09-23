from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.router_error import RouterError
from ...models.router_label import RouterLabel
from ...models.routers import Routers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    label: RouterLabel | Unset = UNSET,
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
        "url": "/1.3/router",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RouterError | Routers:
    if response.status_code == 200:
        response_200 = Routers.from_dict(response.json())

        return response_200

    response_default = RouterError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RouterError | Routers]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: RouterLabel | Unset = UNSET,
) -> Response[RouterError | Routers]:
    """List routers

     Returns a list of all available routers associated with the current account.

    It is also possible to filter routers with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only routers that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (RouterLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouterError | Routers]
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
    label: RouterLabel | Unset = UNSET,
) -> RouterError | Routers | None:
    """List routers

     Returns a list of all available routers associated with the current account.

    It is also possible to filter routers with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only routers that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (RouterLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouterError | Routers
    """

    return sync_detailed(
        client=client,
        label=label,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    label: RouterLabel | Unset = UNSET,
) -> Response[RouterError | Routers]:
    """List routers

     Returns a list of all available routers associated with the current account.

    It is also possible to filter routers with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only routers that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (RouterLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouterError | Routers]
    """

    kwargs = _get_kwargs(
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    label: RouterLabel | Unset = UNSET,
) -> RouterError | Routers | None:
    """List routers

     Returns a list of all available routers associated with the current account.

    It is also possible to filter routers with label URL parameters, e.g.
    `?label=env` or `?label=env%3Dprod`. URL parameter can be given multiple
    times to add more filters (e.g. `?label=env%3Dprod&label=v2`), where
    only routers that match all labels are returned.
    Label keys are matched case insensitively.

    Args:
        label (RouterLabel | Unset): A key/value pair to label and categorize resources Example:
            {'key': 'env', 'value': 'production'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouterError | Routers
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
        )
    ).parsed
