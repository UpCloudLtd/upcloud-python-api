from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.load_balancer_dns_challenge_domain_response import LoadBalancerDnsChallengeDomainResponse
from ...models.load_balancer_error_response import LoadBalancerErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/1.3/load-balancer/certificate-bundles/dns-challenge-domain",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse:
    if response.status_code == 200:
        response_200 = LoadBalancerDnsChallengeDomainResponse.from_dict(response.json())

        return response_200

    response_default = LoadBalancerErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse]:
    """Get load balancer DNS challenge domain

     Returns DNS challenge domain.

    This can be used to validate domain ownership using the ACME challenge method. To validate your
    domain, you need to add CNAME record to the domain provided by this API to your DNS settings. The
    name/host of the CNAME record should be _acme-challenge or _acme-challenge.mysubdomain if you are
    setting up a subdomain called mysubdomain. The target/points to of the record needs to be set to the
    value returned by this API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse | None:
    """Get load balancer DNS challenge domain

     Returns DNS challenge domain.

    This can be used to validate domain ownership using the ACME challenge method. To validate your
    domain, you need to add CNAME record to the domain provided by this API to your DNS settings. The
    name/host of the CNAME record should be _acme-challenge or _acme-challenge.mysubdomain if you are
    setting up a subdomain called mysubdomain. The target/points to of the record needs to be set to the
    value returned by this API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse]:
    """Get load balancer DNS challenge domain

     Returns DNS challenge domain.

    This can be used to validate domain ownership using the ACME challenge method. To validate your
    domain, you need to add CNAME record to the domain provided by this API to your DNS settings. The
    name/host of the CNAME record should be _acme-challenge or _acme-challenge.mysubdomain if you are
    setting up a subdomain called mysubdomain. The target/points to of the record needs to be set to the
    value returned by this API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse | None:
    """Get load balancer DNS challenge domain

     Returns DNS challenge domain.

    This can be used to validate domain ownership using the ACME challenge method. To validate your
    domain, you need to add CNAME record to the domain provided by this API to your DNS settings. The
    name/host of the CNAME record should be _acme-challenge or _acme-challenge.mysubdomain if you are
    setting up a subdomain called mysubdomain. The target/points to of the record needs to be set to the
    value returned by this API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadBalancerDnsChallengeDomainResponse | LoadBalancerErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
