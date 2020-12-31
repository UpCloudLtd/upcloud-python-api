import itertools
from time import sleep
from datetime import datetime
from dateutil import tz

from upcloud_api import UpCloudClientError, UpCloudAPIError


def assignIfExists(opts, default=None, **kwargs):
    """
    Helper for assigning object attributes from API responses.
    """
    for opt in opts:
        if(opt in kwargs):
            return kwargs[opt]
    return default


def try_it_n_times(operation, expected_error_codes, custom_error='operation failed', n=10):
    """
    Try a given operation (API call) n times.

    Raises if the API call fails with an error_code that is not expected.
    Raises if the API call has not succeeded within n attempts.
    Waits 3 seconds betwee each attempt.
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


def get_raw_data_from_file(file):
    """
    Helper function to get raw file data for uploading.
    """
    with open(file, 'rb') as file:
        data = file.read()
    file.close()
    return data

def convert_datetime_string_to_object(datetime_string):
    """
    Helper function to convert datetime string to object with local timezone
    """
    local_tz = tz.tzlocal()
    datetime_object = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    return datetime_object.replace(tzinfo=local_tz, microsecond=0).isoformat()
