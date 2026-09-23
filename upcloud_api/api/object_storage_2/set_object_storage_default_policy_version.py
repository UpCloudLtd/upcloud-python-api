from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_policy_detail_response import ObjectStorage2PolicyDetailResponse
from ...models.object_storage_2_policy_set_default_version import ObjectStorage2PolicySetDefaultVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    policy_name: str,
    *,
    body: ObjectStorage2PolicySetDefaultVersion | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/object-storage-2/{service_uuid}/policies/{policy_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            policy_name=quote(str(policy_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse:
    if response.status_code == 200:
        response_200 = ObjectStorage2PolicyDetailResponse.from_dict(response.json())

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    policy_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2PolicySetDefaultVersion | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse]:
    """Set default policy version

     Sets the default version for a policy. Note: This is mapped from ModifyPolicyVersion handler.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        body (ObjectStorage2PolicySetDefaultVersion | Unset): Schema for setting a default version
            of a policy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        policy_name=policy_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    policy_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2PolicySetDefaultVersion | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse | None:
    """Set default policy version

     Sets the default version for a policy. Note: This is mapped from ModifyPolicyVersion handler.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        body (ObjectStorage2PolicySetDefaultVersion | Unset): Schema for setting a default version
            of a policy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        policy_name=policy_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    policy_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2PolicySetDefaultVersion | Unset = UNSET,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse]:
    """Set default policy version

     Sets the default version for a policy. Note: This is mapped from ModifyPolicyVersion handler.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        body (ObjectStorage2PolicySetDefaultVersion | Unset): Schema for setting a default version
            of a policy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        policy_name=policy_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    policy_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2PolicySetDefaultVersion | Unset = UNSET,
) -> ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse | None:
    """Set default policy version

     Sets the default version for a policy. Note: This is mapped from ModifyPolicyVersion handler.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        body (ObjectStorage2PolicySetDefaultVersion | Unset): Schema for setting a default version
            of a policy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2PolicyDetailResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            policy_name=policy_name,
            client=client,
            body=body,
        )
    ).parsed
