from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import UpCloudResource
from upcloud_api.utils import assignIfExists


class StorageImport(UpCloudResource):
    """
    Class representation of UpCloud Storage import.
    """

    ATTRIBUTES = {
        'client_content_length': None,
        'client_content_type': None,
        'completed': None,
        'created': None,
        'error_code': None,
        'error_message': None,
        'md5sum': None,
        'read_bytes': None,
        'sha256sum': None,
        'source': None,
        'source_location': None,
        'state': None,
        'uuid': None,
        'written_bytes': None,
        'direct_upload_url': None
    }
