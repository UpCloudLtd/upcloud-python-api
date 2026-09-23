from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_label_detail_response import ObjectStorage2LabelDetailResponse
from ...models.object_storage_2_label_modify import ObjectStorage2LabelModify
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    label_key: str,
    *,
    body: ObjectStorage2LabelModify | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/object-storage-2/{service_uuid}/labels/{label_key}".format(
            service_uuid=quote(str(service_uuid), safe=""),
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
) -> ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse:
    if response.status_code == 200:
        response_200 = ObjectStorage2LabelDetailResponse.from_dict(response.json())

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse]:
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
    body: ObjectStorage2LabelModify | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse]:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        label_key (str): The key of a label.
        body (ObjectStorage2LabelModify | Unset): Schema for modifying a label with a key-value
            pair.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse]
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
    body: ObjectStorage2LabelModify | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse | None:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        label_key (str): The key of a label.
        body (ObjectStorage2LabelModify | Unset): Schema for modifying a label with a key-value
            pair.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse
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
    body: ObjectStorage2LabelModify | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse]:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        label_key (str): The key of a label.
        body (ObjectStorage2LabelModify | Unset): Schema for modifying a label with a key-value
            pair.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse]
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
    body: ObjectStorage2LabelModify | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse | None:
    """Modify label

     Modifies existing label by given {service_uuid} and {key}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        label_key (str): The key of a label.
        body (ObjectStorage2LabelModify | Unset): Schema for modifying a label with a key-value
            pair.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2LabelDetailResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            label_key=label_key,
            client=client,
            body=body,
        )
    ).parsed
