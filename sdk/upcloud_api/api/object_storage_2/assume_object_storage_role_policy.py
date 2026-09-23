from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.object_storage_2_assume_role_policy_request import ObjectStorage2AssumeRolePolicyRequest
from ...models.object_storage_2_assume_role_policy_response import ObjectStorage2AssumeRolePolicyResponse
from ...models.object_storage_2_error_response import ObjectStorage2ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    role_name: str,
    *,
    body: ObjectStorage2AssumeRolePolicyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/1.3/object-storage-2/{service_uuid}/roles/{role_name}/assume-role-policy".format(
            service_uuid=quote(str(service_uuid), safe=""),
            role_name=quote(str(role_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse:
    if response.status_code == 200:
        response_200 = ObjectStorage2AssumeRolePolicyResponse.from_dict(response.json())

        return response_200

    response_default = ObjectStorage2ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2AssumeRolePolicyRequest | Unset = UNSET,
) -> Response[ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse]:
    """Assume Role Policy

     Assume a role policy by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2AssumeRolePolicyRequest | Unset): Schema for the request to assume a
            role with a policy document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        role_name=role_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2AssumeRolePolicyRequest | Unset = UNSET,
) -> ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse | None:
    """Assume Role Policy

     Assume a role policy by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2AssumeRolePolicyRequest | Unset): Schema for the request to assume a
            role with a policy document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse
    """

    return sync_detailed(
        service_uuid=service_uuid,
        role_name=role_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2AssumeRolePolicyRequest | Unset = UNSET,
) -> Response[ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse]:
    """Assume Role Policy

     Assume a role policy by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2AssumeRolePolicyRequest | Unset): Schema for the request to assume a
            role with a policy document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        role_name=role_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    role_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectStorage2AssumeRolePolicyRequest | Unset = UNSET,
) -> ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse | None:
    """Assume Role Policy

     Assume a role policy by the given {service_uuid}, and {role_name}.

    Args:
        service_uuid (UUID): The unique identifier for the service.
        role_name (str): A resource name.
        body (ObjectStorage2AssumeRolePolicyRequest | Unset): Schema for the request to assume a
            role with a policy document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorage2AssumeRolePolicyResponse | ObjectStorage2ErrorResponse
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            role_name=role_name,
            client=client,
            body=body,
        )
    ).parsed
