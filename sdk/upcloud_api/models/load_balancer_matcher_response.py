from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_matcher_response_type import LoadBalancerMatcherResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_match_backend_response import LoadBalancerMatchBackendResponse
    from ..models.load_balancer_match_int_response import LoadBalancerMatchIntResponse
    from ..models.load_balancer_match_ip_response import LoadBalancerMatchIpResponse
    from ..models.load_balancer_match_string_response import LoadBalancerMatchStringResponse
    from ..models.load_balancer_match_string_with_arg_response import LoadBalancerMatchStringWithArgResponse


T = TypeVar("T", bound="LoadBalancerMatcherResponse")


@_attrs_define
class LoadBalancerMatcherResponse:
    """Defines a matcher used to evaluate specific conditions in requests or responses.

    Example:
        {'type': 'src_ip', 'inverse': False, 'match_src_ip': {'value': '192.168.1.0/24'}}

    Attributes:
        type_ (LoadBalancerMatcherResponseType): Type of matcher defining which aspect of the request or response to
            evaluate.
        inverse (bool): Indicates whether to invert the match result (true) or use it as-is (false).
        match_src_ip (LoadBalancerMatchIpResponse | Unset): Defines a match condition based on the source IP address or
            subnet. Used when the matcher type is 'src_ip'. Example: {'value': '192.168.1.0/24'}.
        match_src_port (LoadBalancerMatchIntResponse | Unset): Defines integer matching criteria for requests or
            responses. Example: {'method': 'greater_or_equal', 'value': 100, 'range_start': 0, 'range_end': 1024}.
        match_body_size (LoadBalancerMatchIntResponse | Unset): Defines integer matching criteria for requests or
            responses. Example: {'method': 'greater_or_equal', 'value': 100, 'range_start': 0, 'range_end': 1024}.
        match_cookie (LoadBalancerMatchStringWithArgResponse | Unset): Extends MatchString with an additional 'name'
            parameter, used for matchers that require a key-value pair (e.g., matching headers, cookies, or URL parameters).
            Example: {'name': 'Authorization', 'method': 'contains', 'value': '/api', 'ignore_case': True}.
        match_header (LoadBalancerMatchStringWithArgResponse | Unset): Extends MatchString with an additional 'name'
            parameter, used for matchers that require a key-value pair (e.g., matching headers, cookies, or URL parameters).
            Example: {'name': 'Authorization', 'method': 'contains', 'value': '/api', 'ignore_case': True}.
        match_url_param (LoadBalancerMatchStringWithArgResponse | Unset): Extends MatchString with an additional 'name'
            parameter, used for matchers that require a key-value pair (e.g., matching headers, cookies, or URL parameters).
            Example: {'name': 'Authorization', 'method': 'contains', 'value': '/api', 'ignore_case': True}.
        match_request_header (LoadBalancerMatchStringWithArgResponse | Unset): Extends MatchString with an additional
            'name' parameter, used for matchers that require a key-value pair (e.g., matching headers, cookies, or URL
            parameters). Example: {'name': 'Authorization', 'method': 'contains', 'value': '/api', 'ignore_case': True}.
        match_response_header (LoadBalancerMatchStringWithArgResponse | Unset): Extends MatchString with an additional
            'name' parameter, used for matchers that require a key-value pair (e.g., matching headers, cookies, or URL
            parameters). Example: {'name': 'Authorization', 'method': 'contains', 'value': '/api', 'ignore_case': True}.
        match_http_status (LoadBalancerMatchIntResponse | Unset): Defines integer matching criteria for requests or
            responses. Example: {'method': 'greater_or_equal', 'value': 100, 'range_start': 0, 'range_end': 1024}.
        match_http_method (LoadBalancerMatchStringResponse | Unset): Defines a string-based match condition, used for
            matching values such as paths, headers, URLs, or hostnames. Example: {'method': 'contains', 'value': '/api',
            'ignore_case': True}.
        match_path (LoadBalancerMatchStringResponse | Unset): Defines a string-based match condition, used for matching
            values such as paths, headers, URLs, or hostnames. Example: {'method': 'contains', 'value': '/api',
            'ignore_case': True}.
        match_url (LoadBalancerMatchStringResponse | Unset): Defines a string-based match condition, used for matching
            values such as paths, headers, URLs, or hostnames. Example: {'method': 'contains', 'value': '/api',
            'ignore_case': True}.
        match_host (LoadBalancerMatchStringResponse | Unset): Defines a string-based match condition, used for matching
            values such as paths, headers, URLs, or hostnames. Example: {'method': 'contains', 'value': '/api',
            'ignore_case': True}.
        match_url_query (LoadBalancerMatchStringResponse | Unset): Defines a string-based match condition, used for
            matching values such as paths, headers, URLs, or hostnames. Example: {'method': 'contains', 'value': '/api',
            'ignore_case': True}.
        match_num_members_up (LoadBalancerMatchBackendResponse | Unset): Defines a backend health matcher used to
            compare the number of healthy (up) members in a specific backend against a threshold value. Used when the
            matcher type is 'num_members_up'. Example: {'backend': 'backend-1', 'method': 'greater_or_equal', 'value': 2,
            'range_start': 0, 'range_end': 10}.
    """

    type_: LoadBalancerMatcherResponseType
    inverse: bool
    match_src_ip: LoadBalancerMatchIpResponse | Unset = UNSET
    match_src_port: LoadBalancerMatchIntResponse | Unset = UNSET
    match_body_size: LoadBalancerMatchIntResponse | Unset = UNSET
    match_cookie: LoadBalancerMatchStringWithArgResponse | Unset = UNSET
    match_header: LoadBalancerMatchStringWithArgResponse | Unset = UNSET
    match_url_param: LoadBalancerMatchStringWithArgResponse | Unset = UNSET
    match_request_header: LoadBalancerMatchStringWithArgResponse | Unset = UNSET
    match_response_header: LoadBalancerMatchStringWithArgResponse | Unset = UNSET
    match_http_status: LoadBalancerMatchIntResponse | Unset = UNSET
    match_http_method: LoadBalancerMatchStringResponse | Unset = UNSET
    match_path: LoadBalancerMatchStringResponse | Unset = UNSET
    match_url: LoadBalancerMatchStringResponse | Unset = UNSET
    match_host: LoadBalancerMatchStringResponse | Unset = UNSET
    match_url_query: LoadBalancerMatchStringResponse | Unset = UNSET
    match_num_members_up: LoadBalancerMatchBackendResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        inverse = self.inverse

        match_src_ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_src_ip, Unset):
            match_src_ip = self.match_src_ip.to_dict()

        match_src_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_src_port, Unset):
            match_src_port = self.match_src_port.to_dict()

        match_body_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_body_size, Unset):
            match_body_size = self.match_body_size.to_dict()

        match_cookie: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_cookie, Unset):
            match_cookie = self.match_cookie.to_dict()

        match_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_header, Unset):
            match_header = self.match_header.to_dict()

        match_url_param: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_url_param, Unset):
            match_url_param = self.match_url_param.to_dict()

        match_request_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_request_header, Unset):
            match_request_header = self.match_request_header.to_dict()

        match_response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_response_header, Unset):
            match_response_header = self.match_response_header.to_dict()

        match_http_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_http_status, Unset):
            match_http_status = self.match_http_status.to_dict()

        match_http_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_http_method, Unset):
            match_http_method = self.match_http_method.to_dict()

        match_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_path, Unset):
            match_path = self.match_path.to_dict()

        match_url: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_url, Unset):
            match_url = self.match_url.to_dict()

        match_host: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_host, Unset):
            match_host = self.match_host.to_dict()

        match_url_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_url_query, Unset):
            match_url_query = self.match_url_query.to_dict()

        match_num_members_up: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_num_members_up, Unset):
            match_num_members_up = self.match_num_members_up.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "inverse": inverse,
            }
        )
        if match_src_ip is not UNSET:
            field_dict["match_src_ip"] = match_src_ip
        if match_src_port is not UNSET:
            field_dict["match_src_port"] = match_src_port
        if match_body_size is not UNSET:
            field_dict["match_body_size"] = match_body_size
        if match_cookie is not UNSET:
            field_dict["match_cookie"] = match_cookie
        if match_header is not UNSET:
            field_dict["match_header"] = match_header
        if match_url_param is not UNSET:
            field_dict["match_url_param"] = match_url_param
        if match_request_header is not UNSET:
            field_dict["match_request_header"] = match_request_header
        if match_response_header is not UNSET:
            field_dict["match_response_header"] = match_response_header
        if match_http_status is not UNSET:
            field_dict["match_http_status"] = match_http_status
        if match_http_method is not UNSET:
            field_dict["match_http_method"] = match_http_method
        if match_path is not UNSET:
            field_dict["match_path"] = match_path
        if match_url is not UNSET:
            field_dict["match_url"] = match_url
        if match_host is not UNSET:
            field_dict["match_host"] = match_host
        if match_url_query is not UNSET:
            field_dict["match_url_query"] = match_url_query
        if match_num_members_up is not UNSET:
            field_dict["match_num_members_up"] = match_num_members_up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_match_backend_response import LoadBalancerMatchBackendResponse  # noqa: PLC0415
        from ..models.load_balancer_match_int_response import LoadBalancerMatchIntResponse  # noqa: PLC0415
        from ..models.load_balancer_match_ip_response import LoadBalancerMatchIpResponse  # noqa: PLC0415
        from ..models.load_balancer_match_string_response import LoadBalancerMatchStringResponse  # noqa: PLC0415
        from ..models.load_balancer_match_string_with_arg_response import (
            LoadBalancerMatchStringWithArgResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = LoadBalancerMatcherResponseType(d.pop("type"))

        inverse = d.pop("inverse")

        _match_src_ip = d.pop("match_src_ip", UNSET)
        match_src_ip: LoadBalancerMatchIpResponse | Unset
        if isinstance(_match_src_ip, Unset):
            match_src_ip = UNSET
        else:
            match_src_ip = LoadBalancerMatchIpResponse.from_dict(_match_src_ip)

        _match_src_port = d.pop("match_src_port", UNSET)
        match_src_port: LoadBalancerMatchIntResponse | Unset
        if isinstance(_match_src_port, Unset):
            match_src_port = UNSET
        else:
            match_src_port = LoadBalancerMatchIntResponse.from_dict(_match_src_port)

        _match_body_size = d.pop("match_body_size", UNSET)
        match_body_size: LoadBalancerMatchIntResponse | Unset
        if isinstance(_match_body_size, Unset):
            match_body_size = UNSET
        else:
            match_body_size = LoadBalancerMatchIntResponse.from_dict(_match_body_size)

        _match_cookie = d.pop("match_cookie", UNSET)
        match_cookie: LoadBalancerMatchStringWithArgResponse | Unset
        if isinstance(_match_cookie, Unset):
            match_cookie = UNSET
        else:
            match_cookie = LoadBalancerMatchStringWithArgResponse.from_dict(_match_cookie)

        _match_header = d.pop("match_header", UNSET)
        match_header: LoadBalancerMatchStringWithArgResponse | Unset
        if isinstance(_match_header, Unset):
            match_header = UNSET
        else:
            match_header = LoadBalancerMatchStringWithArgResponse.from_dict(_match_header)

        _match_url_param = d.pop("match_url_param", UNSET)
        match_url_param: LoadBalancerMatchStringWithArgResponse | Unset
        if isinstance(_match_url_param, Unset):
            match_url_param = UNSET
        else:
            match_url_param = LoadBalancerMatchStringWithArgResponse.from_dict(_match_url_param)

        _match_request_header = d.pop("match_request_header", UNSET)
        match_request_header: LoadBalancerMatchStringWithArgResponse | Unset
        if isinstance(_match_request_header, Unset):
            match_request_header = UNSET
        else:
            match_request_header = LoadBalancerMatchStringWithArgResponse.from_dict(_match_request_header)

        _match_response_header = d.pop("match_response_header", UNSET)
        match_response_header: LoadBalancerMatchStringWithArgResponse | Unset
        if isinstance(_match_response_header, Unset):
            match_response_header = UNSET
        else:
            match_response_header = LoadBalancerMatchStringWithArgResponse.from_dict(_match_response_header)

        _match_http_status = d.pop("match_http_status", UNSET)
        match_http_status: LoadBalancerMatchIntResponse | Unset
        if isinstance(_match_http_status, Unset):
            match_http_status = UNSET
        else:
            match_http_status = LoadBalancerMatchIntResponse.from_dict(_match_http_status)

        _match_http_method = d.pop("match_http_method", UNSET)
        match_http_method: LoadBalancerMatchStringResponse | Unset
        if isinstance(_match_http_method, Unset):
            match_http_method = UNSET
        else:
            match_http_method = LoadBalancerMatchStringResponse.from_dict(_match_http_method)

        _match_path = d.pop("match_path", UNSET)
        match_path: LoadBalancerMatchStringResponse | Unset
        if isinstance(_match_path, Unset):
            match_path = UNSET
        else:
            match_path = LoadBalancerMatchStringResponse.from_dict(_match_path)

        _match_url = d.pop("match_url", UNSET)
        match_url: LoadBalancerMatchStringResponse | Unset
        if isinstance(_match_url, Unset):
            match_url = UNSET
        else:
            match_url = LoadBalancerMatchStringResponse.from_dict(_match_url)

        _match_host = d.pop("match_host", UNSET)
        match_host: LoadBalancerMatchStringResponse | Unset
        if isinstance(_match_host, Unset):
            match_host = UNSET
        else:
            match_host = LoadBalancerMatchStringResponse.from_dict(_match_host)

        _match_url_query = d.pop("match_url_query", UNSET)
        match_url_query: LoadBalancerMatchStringResponse | Unset
        if isinstance(_match_url_query, Unset):
            match_url_query = UNSET
        else:
            match_url_query = LoadBalancerMatchStringResponse.from_dict(_match_url_query)

        _match_num_members_up = d.pop("match_num_members_up", UNSET)
        match_num_members_up: LoadBalancerMatchBackendResponse | Unset
        if isinstance(_match_num_members_up, Unset):
            match_num_members_up = UNSET
        else:
            match_num_members_up = LoadBalancerMatchBackendResponse.from_dict(_match_num_members_up)

        load_balancer_matcher_response = cls(
            type_=type_,
            inverse=inverse,
            match_src_ip=match_src_ip,
            match_src_port=match_src_port,
            match_body_size=match_body_size,
            match_cookie=match_cookie,
            match_header=match_header,
            match_url_param=match_url_param,
            match_request_header=match_request_header,
            match_response_header=match_response_header,
            match_http_status=match_http_status,
            match_http_method=match_http_method,
            match_path=match_path,
            match_url=match_url,
            match_host=match_host,
            match_url_query=match_url_query,
            match_num_members_up=match_num_members_up,
        )

        return load_balancer_matcher_response
