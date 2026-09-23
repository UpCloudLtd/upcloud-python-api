from enum import StrEnum


class DatabaseServicePropertiesPgLogLinePrefix(StrEnum):
    VALUE_0 = "'pid=%p,user=%u,db=%d,app=%a,client=%h '"
    VALUE_1 = "'pid=%p,user=%u,db=%d,app=%a,client=%h,txid=%x,qid=%Q '"
    VALUE_2 = "'%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '"
    VALUE_3 = "'%m [%p] %q[user=%u,db=%d,app=%a] '"

    def __str__(self) -> str:
        return str(self.value)
