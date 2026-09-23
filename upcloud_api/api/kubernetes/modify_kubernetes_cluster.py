from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_cluster import KubernetesCluster
from ...models.kubernetes_cluster_patch import KubernetesClusterPatch
from ...models.kubernetes_error import KubernetesError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: KubernetesClusterPatch | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/1.3/kubernetes/{uuid}".format(
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
) -> KubernetesCluster | KubernetesError:
    if response.status_code == 200:
        response_200 = KubernetesCluster.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = KubernetesError.from_dict(response.json())

        return response_400

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
) -> Response[KubernetesCluster | KubernetesError]:
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
    body: KubernetesClusterPatch | Unset = UNSET,
) -> Response[KubernetesCluster | KubernetesError]:
    """Modify cluster

     Modifies an existing Kubernetes cluster by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesClusterPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesCluster | KubernetesError]
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
    body: KubernetesClusterPatch | Unset = UNSET,
) -> KubernetesCluster | KubernetesError | None:
    """Modify cluster

     Modifies an existing Kubernetes cluster by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesClusterPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesCluster | KubernetesError
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
    body: KubernetesClusterPatch | Unset = UNSET,
) -> Response[KubernetesCluster | KubernetesError]:
    """Modify cluster

     Modifies an existing Kubernetes cluster by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesClusterPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesCluster | KubernetesError]
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
    body: KubernetesClusterPatch | Unset = UNSET,
) -> KubernetesCluster | KubernetesError | None:
    """Modify cluster

     Modifies an existing Kubernetes cluster by given `{uuid}`.

    Args:
        uuid (UUID): UUID
        body (KubernetesClusterPatch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesCluster | KubernetesError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
