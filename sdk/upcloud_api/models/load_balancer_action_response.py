from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_action_response_type import LoadBalancerActionResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_action_http_redirect_response import LoadBalancerActionHttpRedirectResponse
    from ..models.load_balancer_action_http_return_response import LoadBalancerActionHttpReturnResponse
    from ..models.load_balancer_action_http_rewrite_path_response import LoadBalancerActionHttpRewritePathResponse
    from ..models.load_balancer_action_http_rewrite_uri_response import LoadBalancerActionHttpRewriteUriResponse
    from ..models.load_balancer_action_set_forwarded_headers_response import (
        LoadBalancerActionSetForwardedHeadersResponse,
    )
    from ..models.load_balancer_action_set_header_response import LoadBalancerActionSetHeaderResponse
    from ..models.load_balancer_action_tcp_reject_response import LoadBalancerActionTcpRejectResponse
    from ..models.load_balancer_action_use_backend_response import LoadBalancerActionUseBackendResponse


T = TypeVar("T", bound="LoadBalancerActionResponse")


@_attrs_define
class LoadBalancerActionResponse:
    """Represents a rule action that defines how matched traffic should be processed or modified within the load balancer.
    Each action type includes a corresponding configuration object.

        Example:
            {'type': 'use_backend', 'action_use_backend': {'backend': 'api-backend'}}

        Attributes:
            type_ (LoadBalancerActionResponseType): Type of action defining how matched requests should be processed or
                modified. Example: use_backend.
            action_use_backend (LoadBalancerActionUseBackendResponse | Unset): Defines the backend target to which the
                request should be routed when the rule matches. Used when the action type is 'use_backend'. Example: {'backend':
                'api-backend'}.
            action_http_return (LoadBalancerActionHttpReturnResponse | Unset): Defines a custom HTTP response returned to
                the client when a rule matches. Used when the action type is 'http_return'. Example: {'status': 403,
                'content_type': 'text/plain', 'payload': 'QWNjZXNzIERlbmllZAo='}.
            action_http_redirect (LoadBalancerActionHttpRedirectResponse | Unset): Defines an HTTP redirection action used
                to redirect incoming requests to a specified URL with a given HTTP status code. Used when the action type is
                'http_redirect'. Example: {'location': 'https://example.com', 'status': 301}.
            action_tcp_reject (LoadBalancerActionTcpRejectResponse | Unset): Defines a TCP rejection action that immediately
                closes incoming connections when a rule matches. Used when the action type is 'tcp_reject'. Example: {}.
            action_set_forwarded_headers (LoadBalancerActionSetForwardedHeadersResponse | Unset): Defines an action that
                automatically adds standard X-Forwarded-* headers (such as X-Forwarded-For and X-Forwarded-Proto) to requests
                before forwarding them to the backend. Used when the action type is 'set_forwarded_headers'. Example: {}.
            action_set_request_header (LoadBalancerActionSetHeaderResponse | Unset): Defines an action that adds or modifies
                an HTTP header in a request or response. Used when the action type is 'set_request_header' or
                'set_response_header'. Example: {'header': 'X-Custom-Header', 'value': 'Processed-By-UpCloud-LB'}.
            action_set_response_header (LoadBalancerActionSetHeaderResponse | Unset): Defines an action that adds or
                modifies an HTTP header in a request or response. Used when the action type is 'set_request_header' or
                'set_response_header'. Example: {'header': 'X-Custom-Header', 'value': 'Processed-By-UpCloud-LB'}.
            action_http_rewrite_path (LoadBalancerActionHttpRewritePathResponse | Unset): Defines an action that rewrites
                the HTTP request path using a regex pattern. Example: {'match_pattern': '^/api/(.*)$', 'rewrite_to':
                '/v2/\\\\1'}.
            action_http_rewrite_uri (LoadBalancerActionHttpRewriteUriResponse | Unset): Defines an action that rewrites the
                HTTP request URI using a regex pattern. Example: {'match_pattern': '^/api/(.*)$', 'rewrite_to': '/v2/\\\\1'}.
    """

    type_: LoadBalancerActionResponseType
    action_use_backend: LoadBalancerActionUseBackendResponse | Unset = UNSET
    action_http_return: LoadBalancerActionHttpReturnResponse | Unset = UNSET
    action_http_redirect: LoadBalancerActionHttpRedirectResponse | Unset = UNSET
    action_tcp_reject: LoadBalancerActionTcpRejectResponse | Unset = UNSET
    action_set_forwarded_headers: LoadBalancerActionSetForwardedHeadersResponse | Unset = UNSET
    action_set_request_header: LoadBalancerActionSetHeaderResponse | Unset = UNSET
    action_set_response_header: LoadBalancerActionSetHeaderResponse | Unset = UNSET
    action_http_rewrite_path: LoadBalancerActionHttpRewritePathResponse | Unset = UNSET
    action_http_rewrite_uri: LoadBalancerActionHttpRewriteUriResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        action_use_backend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_use_backend, Unset):
            action_use_backend = self.action_use_backend.to_dict()

        action_http_return: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_http_return, Unset):
            action_http_return = self.action_http_return.to_dict()

        action_http_redirect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_http_redirect, Unset):
            action_http_redirect = self.action_http_redirect.to_dict()

        action_tcp_reject: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_tcp_reject, Unset):
            action_tcp_reject = self.action_tcp_reject.to_dict()

        action_set_forwarded_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_set_forwarded_headers, Unset):
            action_set_forwarded_headers = self.action_set_forwarded_headers.to_dict()

        action_set_request_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_set_request_header, Unset):
            action_set_request_header = self.action_set_request_header.to_dict()

        action_set_response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_set_response_header, Unset):
            action_set_response_header = self.action_set_response_header.to_dict()

        action_http_rewrite_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_http_rewrite_path, Unset):
            action_http_rewrite_path = self.action_http_rewrite_path.to_dict()

        action_http_rewrite_uri: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_http_rewrite_uri, Unset):
            action_http_rewrite_uri = self.action_http_rewrite_uri.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if action_use_backend is not UNSET:
            field_dict["action_use_backend"] = action_use_backend
        if action_http_return is not UNSET:
            field_dict["action_http_return"] = action_http_return
        if action_http_redirect is not UNSET:
            field_dict["action_http_redirect"] = action_http_redirect
        if action_tcp_reject is not UNSET:
            field_dict["action_tcp_reject"] = action_tcp_reject
        if action_set_forwarded_headers is not UNSET:
            field_dict["action_set_forwarded_headers"] = action_set_forwarded_headers
        if action_set_request_header is not UNSET:
            field_dict["action_set_request_header"] = action_set_request_header
        if action_set_response_header is not UNSET:
            field_dict["action_set_response_header"] = action_set_response_header
        if action_http_rewrite_path is not UNSET:
            field_dict["action_http_rewrite_path"] = action_http_rewrite_path
        if action_http_rewrite_uri is not UNSET:
            field_dict["action_http_rewrite_uri"] = action_http_rewrite_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_http_redirect_response import (
            LoadBalancerActionHttpRedirectResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_http_return_response import (
            LoadBalancerActionHttpReturnResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_http_rewrite_path_response import (
            LoadBalancerActionHttpRewritePathResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_http_rewrite_uri_response import (
            LoadBalancerActionHttpRewriteUriResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_set_forwarded_headers_response import (
            LoadBalancerActionSetForwardedHeadersResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_set_header_response import (
            LoadBalancerActionSetHeaderResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_tcp_reject_response import (
            LoadBalancerActionTcpRejectResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_use_backend_response import (
            LoadBalancerActionUseBackendResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = LoadBalancerActionResponseType(d.pop("type"))

        _action_use_backend = d.pop("action_use_backend", UNSET)
        action_use_backend: LoadBalancerActionUseBackendResponse | Unset
        if isinstance(_action_use_backend, Unset):
            action_use_backend = UNSET
        else:
            action_use_backend = LoadBalancerActionUseBackendResponse.from_dict(_action_use_backend)

        _action_http_return = d.pop("action_http_return", UNSET)
        action_http_return: LoadBalancerActionHttpReturnResponse | Unset
        if isinstance(_action_http_return, Unset):
            action_http_return = UNSET
        else:
            action_http_return = LoadBalancerActionHttpReturnResponse.from_dict(_action_http_return)

        _action_http_redirect = d.pop("action_http_redirect", UNSET)
        action_http_redirect: LoadBalancerActionHttpRedirectResponse | Unset
        if isinstance(_action_http_redirect, Unset):
            action_http_redirect = UNSET
        else:
            action_http_redirect = LoadBalancerActionHttpRedirectResponse.from_dict(_action_http_redirect)

        _action_tcp_reject = d.pop("action_tcp_reject", UNSET)
        action_tcp_reject: LoadBalancerActionTcpRejectResponse | Unset
        if isinstance(_action_tcp_reject, Unset):
            action_tcp_reject = UNSET
        else:
            action_tcp_reject = LoadBalancerActionTcpRejectResponse.from_dict(_action_tcp_reject)

        _action_set_forwarded_headers = d.pop("action_set_forwarded_headers", UNSET)
        action_set_forwarded_headers: LoadBalancerActionSetForwardedHeadersResponse | Unset
        if isinstance(_action_set_forwarded_headers, Unset):
            action_set_forwarded_headers = UNSET
        else:
            action_set_forwarded_headers = LoadBalancerActionSetForwardedHeadersResponse.from_dict(
                _action_set_forwarded_headers
            )

        _action_set_request_header = d.pop("action_set_request_header", UNSET)
        action_set_request_header: LoadBalancerActionSetHeaderResponse | Unset
        if isinstance(_action_set_request_header, Unset):
            action_set_request_header = UNSET
        else:
            action_set_request_header = LoadBalancerActionSetHeaderResponse.from_dict(_action_set_request_header)

        _action_set_response_header = d.pop("action_set_response_header", UNSET)
        action_set_response_header: LoadBalancerActionSetHeaderResponse | Unset
        if isinstance(_action_set_response_header, Unset):
            action_set_response_header = UNSET
        else:
            action_set_response_header = LoadBalancerActionSetHeaderResponse.from_dict(_action_set_response_header)

        _action_http_rewrite_path = d.pop("action_http_rewrite_path", UNSET)
        action_http_rewrite_path: LoadBalancerActionHttpRewritePathResponse | Unset
        if isinstance(_action_http_rewrite_path, Unset):
            action_http_rewrite_path = UNSET
        else:
            action_http_rewrite_path = LoadBalancerActionHttpRewritePathResponse.from_dict(_action_http_rewrite_path)

        _action_http_rewrite_uri = d.pop("action_http_rewrite_uri", UNSET)
        action_http_rewrite_uri: LoadBalancerActionHttpRewriteUriResponse | Unset
        if isinstance(_action_http_rewrite_uri, Unset):
            action_http_rewrite_uri = UNSET
        else:
            action_http_rewrite_uri = LoadBalancerActionHttpRewriteUriResponse.from_dict(_action_http_rewrite_uri)

        load_balancer_action_response = cls(
            type_=type_,
            action_use_backend=action_use_backend,
            action_http_return=action_http_return,
            action_http_redirect=action_http_redirect,
            action_tcp_reject=action_tcp_reject,
            action_set_forwarded_headers=action_set_forwarded_headers,
            action_set_request_header=action_set_request_header,
            action_set_response_header=action_set_response_header,
            action_http_rewrite_path=action_http_rewrite_path,
            action_http_rewrite_uri=action_http_rewrite_uri,
        )

        return load_balancer_action_response
