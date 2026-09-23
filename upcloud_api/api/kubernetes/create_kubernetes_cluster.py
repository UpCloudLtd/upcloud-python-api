from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_cluster import KubernetesCluster
from ...models.kubernetes_error import KubernetesError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: KubernetesCluster | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/1.3/kubernetes",
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

    if response.status_code == 422:
        response_422 = KubernetesError.from_dict(response.json())

        return response_422

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
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesCluster | Unset = UNSET,
) -> Response[KubernetesCluster | KubernetesError]:
    """Create cluster

     Creates a new Kubernetes cluster.

    Args:
        body (KubernetesCluster | Unset): Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesCluster | KubernetesError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesCluster | Unset = UNSET,
) -> KubernetesCluster | KubernetesError | None:
    """Create cluster

     Creates a new Kubernetes cluster.

    Args:
        body (KubernetesCluster | Unset): Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesCluster | KubernetesError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesCluster | Unset = UNSET,
) -> Response[KubernetesCluster | KubernetesError]:
    """Create cluster

     Creates a new Kubernetes cluster.

    Args:
        body (KubernetesCluster | Unset): Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KubernetesCluster | KubernetesError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: KubernetesCluster | Unset = UNSET,
) -> KubernetesCluster | KubernetesError | None:
    """Create cluster

     Creates a new Kubernetes cluster.

    Args:
        body (KubernetesCluster | Unset): Kubernetes cluster

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KubernetesCluster | KubernetesError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
