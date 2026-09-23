from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.database_error_response import DatabaseErrorResponse
from ...models.database_label_modify import DatabaseLabelModify
from ...models.database_label_response import DatabaseLabelResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    label_key: str,
    *,
    body: DatabaseLabelModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/database/{uuid}/labels/{label_key}".format(
            uuid=quote(str(uuid), safe=""),
            label_key=quote(str(label_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatabaseErrorResponse | DatabaseLabelResponse:
    if response.status_code == 200:
        response_200 = DatabaseLabelResponse.from_dict(response.json())

        return response_200

    response_default = DatabaseErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatabaseErrorResponse | DatabaseLabelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseLabelModify | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseLabelResponse]:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        label_key (str): The key of a label.
        body (DatabaseLabelModify | Unset): Schema for modifying a label with a key and/or value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseLabelResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        label_key=label_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseLabelModify | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseLabelResponse | None:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        label_key (str): The key of a label.
        body (DatabaseLabelModify | Unset): Schema for modifying a label with a key and/or value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseLabelResponse
    """

    return sync_detailed(
        uuid=uuid,
        label_key=label_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseLabelModify | Unset = UNSET,
) -> Response[DatabaseErrorResponse | DatabaseLabelResponse]:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        label_key (str): The key of a label.
        body (DatabaseLabelModify | Unset): Schema for modifying a label with a key and/or value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseErrorResponse | DatabaseLabelResponse]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        label_key=label_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    label_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatabaseLabelModify | Unset = UNSET,
) -> DatabaseErrorResponse | DatabaseLabelResponse | None:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        uuid (UUID): The unique identifier for the integration.
        label_key (str): The key of a label.
        body (DatabaseLabelModify | Unset): Schema for modifying a label with a key and/or value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseErrorResponse | DatabaseLabelResponse
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            label_key=label_key,
            client=client,
            body=body,
        )
    ).parsed
