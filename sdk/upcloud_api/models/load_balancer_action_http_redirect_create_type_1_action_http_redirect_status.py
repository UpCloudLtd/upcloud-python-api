from enum import IntEnum


class LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectStatus(IntEnum):
    VALUE_301 = 301
    VALUE_302 = 302
    VALUE_303 = 303
    VALUE_307 = 307
    VALUE_308 = 308

    def __str__(self) -> str:
        return str(self.value)
