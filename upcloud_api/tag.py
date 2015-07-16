from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict, str
from future import standard_library
standard_library.install_aliases()

from upcloud_api import Server
from time import sleep


class Tag():
    """
    UpCloud Tag object
    - name: unique name for the tag.
    - description: optional description
    - servers:
        list of Server objects (with only uuid populated).
        Can be instantiated with UUID strings or Server objects.
    """

    def __init__(self, name, description=None, servers=None, cloud_manager=None, **kwargs):
        self.cloud_manager = cloud_manager
        self.__reset(name=name, description=description, servers=servers)


    def __str__(self):
        return self.name


    def __reset(self, **kwargs):
        """
        Reset the objects attributes.
        Accepts servers as either unflattened or flattened UUID strings or Server objects.
        """

        # name is required and should be stored in a hidden attribute for .save()
        if 'name' in kwargs:
            self._api_name = kwargs['name']
        else:
            raise Exception('`name` is requred')

        # flatten { servers: { server: [] } }
        if 'servers' in kwargs and kwargs['servers'] and 'server' in kwargs['servers']:
            servers = kwargs['servers']['server']
        else:
            servers = kwargs['servers']

        # convert UUIDs into server objects
        if servers and isinstance(servers[0], str):
            kwargs['servers'] = [ Server(uuid=server, populated=False) for server in servers ]
        else:
            kwargs['servers'] = servers

        for key, val in kwargs.items():
            setattr(self, key, val)


    def save(self):
        tag_dict = self.cloud_manager._modify_tag(self._api_name, self.description, self.server_uuids, self.name)
        self.__reset(**tag_dict)


    def destroy(self):
        self.cloud_manager.delete_tag(self.name)


    @property
    def server_uuids(self):
        """ return the tag's servers as UUIDs """
        return [ server.uuid for server in self.servers ]


    @classmethod
    def _prepare_tag_body(cls, name, description, servers):
        body = dict()
        body['tag'] = dict()
        if name:        body['tag']['name'] = name
        if description: body['tag']['description'] = description
        if servers:
            body['tag']['servers'] = dict()
            body['tag']['servers']['server'] = servers
        return body
