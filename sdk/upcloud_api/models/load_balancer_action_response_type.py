from enum import StrEnum


class LoadBalancerActionResponseType(StrEnum):
    HTTP_REDIRECT = "http_redirect"
    HTTP_RETURN = "http_return"
    HTTP_REWRITE_PATH = "http_rewrite_path"
    HTTP_REWRITE_URI = "http_rewrite_uri"
    SET_FORWARDED_HEADERS = "set_forwarded_headers"
    SET_REQUEST_HEADER = "set_request_header"
    SET_RESPONSE_HEADER = "set_response_header"
    TCP_REJECT = "tcp_reject"
    USE_BACKEND = "use_backend"

    def __str__(self) -> str:
        return str(self.value)
