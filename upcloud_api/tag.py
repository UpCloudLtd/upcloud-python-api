from __future__ import unicode_literals
from __future__ import absolute_import

import six

from upcloud_api import Server, UpCloudResource


class Tag(UpCloudResource):
    """
    Class representation of UpCloud Tag.

    - name: unique name for the tag.
    - description: optional description
    - servers:
        list of Server objects (with only uuid populated).
        Can be instantiated with UUID strings or Server objects.
    """

    ATTRIBUTES = {
        'name': None,
        'description': None,
        'servers': []
    }

    def __init__(self, name, description=None, servers=[], **kwargs):
        """Init with Tag('tagname', 'description', [servers]) syntax."""
        super(Tag, self).__init__(name=name, description=description, servers=servers, **kwargs)

    def _reset(self, **kwargs):
        """
        Reset the objects attributes.

        Accepts servers as either unflattened or flattened UUID strings or Server objects.
        """
        super(Tag, self)._reset(**kwargs)

        # backup name for changing it (look: Tag.save)
        self._api_name = self.name

        # flatten { servers: { server: [] } }
        if 'server' in self.servers:
            self.servers = kwargs['servers']['server']

        # convert UUIDs into server objects
        if self.servers and isinstance(self.servers[0], six.string_types):
            self.servers = [Server(uuid=server, populated=False) for server in self.servers]

    def save(self):
        tag_dict = self.cloud_manager._modify_tag(self._api_name,
                                                  self.description,
                                                  self.server_uuids,
                                                  self.name)
        self._reset(**tag_dict)

    def destroy(self):
        self.cloud_manager.delete_tag(self.name)

    @property
    def server_uuids(self):
        """return the tag's servers as UUIDs."""
        return [server.uuid for server in self.servers]

    def __str__(self):
        return self.name

    def to_dict(self):
        body = dict()
        body['tag'] = dict()

        if self.name:
            body['tag']['name'] = self.name

        if self.description:
            body['tag']['description'] = self.description

        if self.servers:
            body['tag']['servers'] = dict()
            body['tag']['servers']['server'] = [str(server) for server in self.servers]
        return body
