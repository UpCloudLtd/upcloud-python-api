from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_error import KubernetesError
from ...models.kubernetes_node_group import KubernetesNodeGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: KubernetesNodeGroup | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/kubernetes/{uuid}/node-groups".format(
            uuid=quote(str(uuid), safe=""),
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
    if response.status_code == 201:
        response_201 = KubernetesNodeGroup.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroup | Unset = UNSET,
) -> Response[KubernetesError | KubernetesNodeGroup]:
    """Create node group

     Creates a new node group to an existing Kubernetes cluster. Cluster is identified by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesNodeGroup | Unset): Node group for a Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesError | KubernetesNodeGroup]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroup | Unset = UNSET,
) -> KubernetesError | KubernetesNodeGroup | None:
    """Create node group

     Creates a new node group to an existing Kubernetes cluster. Cluster is identified by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesNodeGroup | Unset): Node group for a Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesError | KubernetesNodeGroup
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroup | Unset = UNSET,
) -> Response[KubernetesError | KubernetesNodeGroup]:
    """Create node group

     Creates a new node group to an existing Kubernetes cluster. Cluster is identified by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesNodeGroup | Unset): Node group for a Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesError | KubernetesNodeGroup]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesNodeGroup | Unset = UNSET,
) -> KubernetesError | KubernetesNodeGroup | None:
    """Create node group

     Creates a new node group to an existing Kubernetes cluster. Cluster is identified by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesNodeGroup | Unset): Node group for a Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesError | KubernetesNodeGroup
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
