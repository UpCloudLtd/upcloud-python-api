from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_error import KubernetesError
from ...models.kubernetes_node_group import KubernetesNodeGroup
from ...models.kubernetes_node_group_patch import KubernetesNodeGroupPatch
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    name: str,
    *,
    body: KubernetesNodeGroupPatch | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/kubernetes/{uuid}/node-groups/{name}".format(
            uuid=quote(str(uuid), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KubernetesError | KubernetesNodeGroup:
    if response.status_code == 200:
        response_200 = KubernetesNodeGroup.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = KubernetesError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = KubernetesError.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = KubernetesError.from_dict(response.json())

        return response_422

    response_default = KubernetesError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[KubernetesError | KubernetesNodeGroup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroupPatch | Unset = UNSET,
) -> Response[KubernetesError | KubernetesNodeGroup]:
    """Modify node group

     Modifies an existing node group of a cluster. Cluster is identified by given `{uuid}` and node group
    by `{node_group_name}`.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesNodeGroupPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesError | KubernetesNodeGroup]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroupPatch | Unset = UNSET,
) -> KubernetesError | KubernetesNodeGroup | None:
    """Modify node group

     Modifies an existing node group of a cluster. Cluster is identified by given `{uuid}` and node group
    by `{node_group_name}`.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesNodeGroupPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesError | KubernetesNodeGroup
    """

    return sync_detailed(
        uuid=uuid,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroupPatch | Unset = UNSET,
) -> Response[KubernetesError | KubernetesNodeGroup]:
    """Modify node group

     Modifies an existing node group of a cluster. Cluster is identified by given `{uuid}` and node group
    by `{node_group_name}`.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesNodeGroupPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesError | KubernetesNodeGroup]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroupPatch | Unset = UNSET,
) -> KubernetesError | KubernetesNodeGroup | None:
    """Modify node group

     Modifies an existing node group of a cluster. Cluster is identified by given `{uuid}` and node group
    by `{node_group_name}`.

    Args:
        uuid (UUID): UUID
        name (str): Name
        body (KubernetesNodeGroupPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesError | KubernetesNodeGroup
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
