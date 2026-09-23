from enum import StrEnum


class RouterModifyRouterStaticRoutesItemNexthopType1(StrEnum):
    NO_NEXTHOP = "no-nexthop"

    def __str__(self) -> str:
        return str(self.value)
