from enum import StrEnum


class FileStorageErrorResponseType(StrEnum):
    HTTPSDEVELOPERS_UPCLOUD_COM1_3ERRORSERROR_GENERAL_FAILURE = (
        "https://developers.upcloud.com/1.3/errors#ERROR_GENERAL_FAILURE"
    )
    HTTPSDEVELOPERS_UPCLOUD_COM1_3ERRORSERROR_INSUFFICIENT_CREDITS = (
        "https://developers.upcloud.com/1.3/errors#ERROR_INSUFFICIENT_CREDITS"
    )
    HTTPSDEVELOPERS_UPCLOUD_COM1_3ERRORSERROR_INVALID_REQUEST = (
        "https://developers.upcloud.com/1.3/errors#ERROR_INVALID_REQUEST"
    )
    HTTPSDEVELOPERS_UPCLOUD_COM1_3ERRORSERROR_RESOURCE_NOT_FOUND = (
        "https://developers.upcloud.com/1.3/errors#ERROR_RESOURCE_NOT_FOUND"
    )

    def __str__(self) -> str:
        return str(self.value)
