from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_error import KubernetesError
from ...models.kubernetes_node_group import KubernetesNodeGroup
from ...types import Response


def _get_kwargs(
    uuid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/kubernetes/{uuid}/node-groups".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KubernetesError | list[KubernetesNodeGroup]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemaskubernetes_node_groups_item_data in _response_200:
            componentsschemaskubernetes_node_groups_item = KubernetesNodeGroup.from_dict(
                componentsschemaskubernetes_node_groups_item_data
            )

            response_200.append(componentsschemaskubernetes_node_groups_item)

        return response_200

    if response.status_code == 401:
        response_401 = KubernetesError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = KubernetesError.from_dict(response.json())

        return response_404

    response_default = KubernetesError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[KubernetesError | list[KubernetesNodeGroup]]:
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
) -> Response[KubernetesError | list[KubernetesNodeGroup]]:
    """List node groups

     Returns a list of available node groups of an existing Kubernetes cluster. Cluster is identified by
    given `{uuid}`.

    A node group is a uniform set of worker nodes attached to a cluster.

    Args:
        uuid (UUID): UUID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesError | list[KubernetesNodeGroup]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> KubernetesError | list[KubernetesNodeGroup] | None:
    """List node groups

     Returns a list of available node groups of an existing Kubernetes cluster. Cluster is identified by
    given `{uuid}`.

    A node group is a uniform set of worker nodes attached to a cluster.

    Args:
        uuid (UUID): UUID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesError | list[KubernetesNodeGroup]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[KubernetesError | list[KubernetesNodeGroup]]:
    """List node groups

     Returns a list of available node groups of an existing Kubernetes cluster. Cluster is identified by
    given `{uuid}`.

    A node group is a uniform set of worker nodes attached to a cluster.

    Args:
        uuid (UUID): UUID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesError | list[KubernetesNodeGroup]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> KubernetesError | list[KubernetesNodeGroup] | None:
    """List node groups

     Returns a list of available node groups of an existing Kubernetes cluster. Cluster is identified by
    given `{uuid}`.

    A node group is a uniform set of worker nodes attached to a cluster.

    Args:
        uuid (UUID): UUID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesError | list[KubernetesNodeGroup]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
