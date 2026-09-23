from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...models.load_balancer_member import LoadBalancerMember
from ...models.load_balancer_member_modify_type_0 import LoadBalancerMemberModifyType0
from ...models.load_balancer_member_modify_type_1 import LoadBalancerMemberModifyType1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_uuid: UUID,
    backend_name: str,
    member_name: str,
    *,
    body: LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/load-balancer/{service_uuid}/backends/{backend_name}/members/{member_name}".format(
            service_uuid=quote(str(service_uuid), safe=""),
            backend_name=quote(str(backend_name), safe=""),
            member_name=quote(str(member_name), safe=""),
        ),
    }

    if isinstance(body, LoadBalancerMemberModifyType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerErrorResponse | LoadBalancerMember:
    if response.status_code == 200:
        response_200 = LoadBalancerMember.from_dict(response.json())

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerErrorResponse | LoadBalancerMember]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_uuid: UUID,
    backend_name: str,
    member_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerMember]:
    """Modify load balancer member

     Modifies existing member by given {service-uuid}, {backend-name} and {member-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        member_name (str): The name of the member.
        body (LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset): Load
            Balancer backend member

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerMember]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        backend_name=backend_name,
        member_name=member_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_uuid: UUID,
    backend_name: str,
    member_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerMember | None:
    """Modify load balancer member

     Modifies existing member by given {service-uuid}, {backend-name} and {member-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        member_name (str): The name of the member.
        body (LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset): Load
            Balancer backend member

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerMember
    """

    return sync_detailed(
        service_uuid=service_uuid,
        backend_name=backend_name,
        member_name=member_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_uuid: UUID,
    backend_name: str,
    member_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset = UNSET,
) -> Response[LoadBalancerErrorResponse | LoadBalancerMember]:
    """Modify load balancer member

     Modifies existing member by given {service-uuid}, {backend-name} and {member-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        member_name (str): The name of the member.
        body (LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset): Load
            Balancer backend member

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerErrorResponse | LoadBalancerMember]
    """

    kwargs = _get_kwargs(
        service_uuid=service_uuid,
        backend_name=backend_name,
        member_name=member_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_uuid: UUID,
    backend_name: str,
    member_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset = UNSET,
) -> LoadBalancerErrorResponse | LoadBalancerMember | None:
    """Modify load balancer member

     Modifies existing member by given {service-uuid}, {backend-name} and {member-name}.

    Args:
        service_uuid (UUID): The UUID of the service.
        backend_name (str): The name of the backend.
        member_name (str): The name of the member.
        body (LoadBalancerMemberModifyType0 | LoadBalancerMemberModifyType1 | Unset): Load
            Balancer backend member

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerErrorResponse | LoadBalancerMember
    """

    return (
        await asyncio_detailed(
            service_uuid=service_uuid,
            backend_name=backend_name,
            member_name=member_name,
            client=client,
            body=body,
        )
    ).parsed
