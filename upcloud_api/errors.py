
class UpCloudAPIError(Exception):
    """Custom Error class for UpCloud API error responses.

    Each API call returns an `error_code` and `error_message` that
    are available as attributes via instances of this class.
    """
    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message

    def __str__(self):
        return '{0} {1}'.format(self.error_code, self.error_message)
