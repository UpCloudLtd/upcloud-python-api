class UpCloudClientError(Exception):
    """
    Base exception for UpCloud API client.

    All exceptions thrown by the client should be of the type UpCloudClientError
    or at least one of its subclasses.
    """

    pass


class UpCloudAPIError(UpCloudClientError):
    """
    Custom Error class for UpCloud API error responses.

    Each API call returns an `error_code` and `error_message` that
    are available as attributes via instances of this class.
    """

    def __init__(self, error_code, error_message):
        """
        Initialize API error with an error code and message.
        """
        self.error_code = error_code
        self.error_message = error_message

    def __str__(self):
        return f'{self.error_code} {self.error_message}'
