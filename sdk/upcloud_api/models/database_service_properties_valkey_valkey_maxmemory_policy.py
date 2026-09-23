from enum import StrEnum


class DatabaseServicePropertiesValkeyValkeyMaxmemoryPolicy(StrEnum):
    ALLKEYS_LFU = "allkeys-lfu"
    ALLKEYS_LRU = "allkeys-lru"
    ALLKEYS_RANDOM = "allkeys-random"
    NOEVICTION = "noeviction"
    VOLATILE_LFU = "volatile-lfu"
    VOLATILE_LRU = "volatile-lru"
    VOLATILE_RANDOM = "volatile-random"
    VOLATILE_TTL = "volatile-ttl"

    def __str__(self) -> str:
        return str(self.value)
