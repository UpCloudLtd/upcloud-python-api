from enum import StrEnum


class LoadBalancerMatcherResponseType(StrEnum):
    BODY_SIZE = "body_size"
    COOKIE = "cookie"
    HEADER = "header"
    HOST = "host"
    HTTP_METHOD = "http_method"
    HTTP_STATUS = "http_status"
    NUM_MEMBERS_UP = "num_members_up"
    PATH = "path"
    REQUEST_HEADER = "request_header"
    RESPONSE_HEADER = "response_header"
    SRC_IP = "src_ip"
    SRC_PORT = "src_port"
    URL = "url"
    URL_PARAM = "url_param"
    URL_QUERY = "url_query"

    def __str__(self) -> str:
        return str(self.value)
