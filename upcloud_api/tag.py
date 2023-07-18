from upcloud_api.server import Server
from upcloud_api.upcloud_resource import UpCloudResource


class Tag(UpCloudResource):
    """
    Class representation of the API's tags. Extends UpCloudResource.

    Attributes
    ----------
    name -- unique name for the tag
    description -- optional description
    servers -- list of Server objects (with only uuid populated)
               can be instantiated with UUID strings or Server objects
    """

    ATTRIBUTES = {'name': None, 'description': None, 'servers': []}

    def __init__(self, name: str, description=None, servers=None, **kwargs) -> None:
        """Init with Tag('tagname', 'description', [servers]) syntax."""
        if servers is None:
            servers = []
        super().__init__(name=name, description=description, servers=servers, **kwargs)

    def _reset(self, **kwargs) -> None:
        """
        Reset the objects attributes.

        Accepts servers as either un-flattened or flattened UUID strings or Server objects.
        """
        super()._reset(**kwargs)

        # backup name for changing it (look: Tag.save)
        self._api_name = self.name

        # flatten { servers: { server: [] } }
        if 'server' in self.servers:
            self.servers = kwargs['servers']['server']

        # convert UUIDs into server objects
        if self.servers and isinstance(self.servers[0], str):
            self.servers = [Server(uuid=server, populated=False) for server in self.servers]

    @property
    def server_uuids(self):
        """
        Return the tag's servers as UUIDs.
        Useful for forming API requests.
        """
        return [server.uuid for server in self.servers]

    def save(self) -> None:
        """
        Save any changes made to the tag.
        """
        tag_dict = self.cloud_manager._modify_tag(
            self._api_name, self.description, self.server_uuids, self.name
        )
        self._reset(**tag_dict)

    def destroy(self):
        """
        Destroy the tag at the API.
        """
        self.cloud_manager.delete_tag(self.name)

    def to_dict(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.
        """
        return {
            'name': self.name,
            'description': self.description or '',
            'servers': {'server': self.server_uuids},
        }

    def __str__(self) -> str:
        """
        String representation of Tag.
        Can be used to add tags into API requests: str(tag).
        """
        return self.name
