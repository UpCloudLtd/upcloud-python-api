from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...models.object_storage_2_policy_version_response import ObjectStorage2PolicyVersionResponse
from ...types import Response


def _get_kwargs(
    service_uuid: UUID,
    policy_name: str,
    policy_version: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/object-storage-2/{service_uuid}/policies/{policy_name}/versions/{policy_version}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            policy_name=quote(str(policy_name), safe=""),
            policy_version=quote(str(policy_version), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse:
    if response.status_code == 200:
        response_200 = ObjectStorage2PolicyVersionResponse.from_dict(response.json())

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    policy_name: str,
    policy_version: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse]:
    """Get policy version

     Get a single policy version by the given {service_uuid}, {policy_name}, and {policy_version}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        policy_version (str): The version identifier of a policy (e.g., v1, v2).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        policy_name=policy_name,
        policy_version=policy_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    policy_name: str,
    policy_version: str,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse | None:
    """Get policy version

     Get a single policy version by the given {service_uuid}, {policy_name}, and {policy_version}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        policy_version (str): The version identifier of a policy (e.g., v1, v2).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        policy_name=policy_name,
        policy_version=policy_version,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    policy_name: str,
    policy_version: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse]:
    """Get policy version

     Get a single policy version by the given {service_uuid}, {policy_name}, and {policy_version}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        policy_version (str): The version identifier of a policy (e.g., v1, v2).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        policy_name=policy_name,
        policy_version=policy_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    policy_name: str,
    policy_version: str,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse | None:
    """Get policy version

     Get a single policy version by the given {service_uuid}, {policy_name}, and {policy_version}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        policy_name (str): A resource name.
        policy_version (str): The version identifier of a policy (e.g., v1, v2).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2ErrorResponse | ObjectStorage2PolicyVersionResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            policy_name=policy_name,
            policy_version=policy_version,
            client=client,
        )
    ).parsed
