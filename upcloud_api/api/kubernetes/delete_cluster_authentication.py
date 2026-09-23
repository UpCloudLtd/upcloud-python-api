from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.kubernetes_error import KubernetesError
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/1.3/kubernetes/{uuid}/authentication/{name}".format(
            uuid=quote(str(uuid), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | KubernetesError:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | KubernetesError]:
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
) -> Response[Any | KubernetesError]:
    """Delete a cluster authentication entry

     Removes an OIDC authentication issuer configuration by name.

    Args:
        uuid (UUID): UUID
        name (str): Name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
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
) -> Any | KubernetesError | None:
    """Delete a cluster authentication entry

     Removes an OIDC authentication issuer configuration by name.

    Args:
        uuid (UUID): UUID
        name (str): Name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | KubernetesError
    """

    return sync_detailed(
        uuid=uuid,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | KubernetesError]:
    """Delete a cluster authentication entry

     Removes an OIDC authentication issuer configuration by name.

    Args:
        uuid (UUID): UUID
        name (str): Name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | KubernetesError]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | KubernetesError | None:
    """Delete a cluster authentication entry

     Removes an OIDC authentication issuer configuration by name.

    Args:
        uuid (UUID): UUID
        name (str): Name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | KubernetesError
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            name=name,
            client=client,
        )
    ).parsed
