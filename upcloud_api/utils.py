import itertools
from time import sleep

from upcloud_api.errors import UpCloudAPIError, UpCloudClientError


def try_it_n_times(operation, expected_error_codes, custom_error='operation failed', n=10):
    """
    Try a given operation (API call) n times.

    Raises if the API call fails with an error_code that is not expected.
    Raises if the API call has not succeeded within n attempts.
    Waits 3 seconds between each attempt.
    """
    for i in itertools.count():
        try:
            operation()
            break
        except UpCloudAPIError as e:
            if e.error_code not in expected_error_codes:
                raise e
            sleep(3)
        if i >= n - 1:
            raise UpCloudClientError(custom_error)
