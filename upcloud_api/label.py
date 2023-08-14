from upcloud_api.upcloud_resource import UpCloudResource


class Label(UpCloudResource):
    """
    Class representation of UpCloud resource label
    """

    ATTRIBUTES = {
        'key': "",
        'value': "",
    }

    def __init__(self, key="", value="") -> None:
        """
        Initialize label.

        Set both values for label if given
        """
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"{self.key}={self.value}"

    def to_dict(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.
        """
        body = {
            'key': self.key,
            'value': self.value,
        }

        return body
