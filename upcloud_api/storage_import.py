from upcloud_api.upcloud_resource import UpCloudResource


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
        'direct_upload_url': None,
    }
