from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from upcloud_api import IPAddress, Server, Storage
from upcloud_api.utils import assignIfExists


class ServerManager(object):
    """
    Functions for managing IP-addresses. Intended to be used as a mixin for CloudManager.
    """

    def get_servers(self, populate=False, tags_has_one=None, tags_has_all=None):
        """
        Return a list of (populated or unpopulated) Server instances.

        - populate = False (default) => 1 API request, returns unpopulated Server instances.
        - populate = True => Does 1 + n API requests (n = # of servers),
                             returns populated Server instances.

        New in 0.3.0: the list can be filtered with tags:
        - tags_has_one: list of Tag objects or strings
          returns servers that have at least one of the given tags

        - tags_has_all: list of Tag objects or strings
          returns servers that have all of the tags
        """
        if tags_has_all and tags_has_one:
            raise Exception('only one of (tags_has_all, tags_has_one) is allowed.')

        request = '/server'
        if tags_has_all:
            tags_has_all = [str(tag) for tag in tags_has_all]
            taglist = ':'.join(tags_has_all)
            request = '/server/tag/{0}'.format(taglist)

        if tags_has_one:
            tags_has_one = [str(tag) for tag in tags_has_one]
            taglist = ','.join(tags_has_one)
            request = '/server/tag/{0}'.format(taglist)

        servers = self.get_request(request)['servers']['server']

        server_list = list()
        for server in servers:
            server_list.append(Server(server, cloud_manager=self))

        if populate:
            for server_instance in server_list:
                server_instance.populate()

        return server_list

    def get_server(self, UUID):
        """
        Return a (populated) Server instance.
        """
        server, IPAddresses, storages = self.get_server_data(UUID)

        return Server(
            server,
            ip_addresses=IPAddresses,
            storage_devices=storages,
            populated=True,
            cloud_manager=self
        )

    def get_server_by_ip(self, ip_address):
        """
        Return a (populated) Server instance by its IP.

        Uses GET '/ip_address/x.x.x.x' to retrieve machine UUID using IP-address.
        """
        data = self.get_request('/ip_address/{0}'.format(ip_address))
        UUID = data['ip_address']['server']
        return self.get_server(UUID)

    def create_server(self, server):
        """
        Create a server and its storages based on a (locally created) Server object.

        Populates the given Server instance with the API response.

        0.3.0: also supports giving the entire POST body as a dict that is directly
        serialised into JSON. Refer to the REST API documentation for correct format.

        Example:
        server1 = Server( core_number = 1,
              memory_amount = 1024,
              hostname = "my.example.1",
              zone = "uk-lon1",
              storage_devices = [
                Storage(os = "01000000-0000-4000-8000-000030060200", size=10, tier=maxiops, title='The OS drive'),
                Storage(size=10),
                Storage()
              title = "My Example Server"
            ])
        manager.create_server(server1)

        One storage should contain an OS. Otherwise storage fields are optional.
        - size defaults to 10,
        - title defaults to hostname + " OS disk" and hostname + " storage disk id"
          (id is a running starting from 1)
        - tier defaults to maxiops
        - valid operating systems are:
          "CentOS 6.10", "CentOS 7.6"
          "Ubuntu 12.04", "01000000-0000-4000-8000-000030060200"
          "Windows 2012", "Windows 2016"
        """
        if isinstance(server, Server):
            body = server.prepare_post_body()
        else:
            server = Server._create_server_obj(server, cloud_manager=self)
            body = server.prepare_post_body()

        res = self.post_request('/server', body)

        server_to_return = server
        server_to_return._reset(
            res['server'],
            cloud_manager=self,
            populated=True
        )
        return server_to_return

    def modify_server(self, UUID, **kwargs):
        """
        modify_server allows updating the server's updateable_fields.

        Note: Server's IP-addresses and Storages are managed by their own add/remove methods.
        """
        body = dict()
        body['server'] = {}
        for arg in kwargs:
            if arg not in Server.updateable_fields:
                Exception('{0} is not an updateable field'.format(arg))
            body['server'][arg] = kwargs[arg]

        res = self.put_request('/server/{0}'.format(UUID), body)
        server = res['server']

        # Populate subobjects
        IPAddresses = IPAddress._create_ip_address_objs(server.pop('ip_addresses'),
                                                          cloud_manager=self)

        storages = Storage._create_storage_objs(server.pop('storage_devices'),
                                                cloud_manager=self)

        return Server(
            server,
            ip_addresses=IPAddresses,
            storage_devices=storages,
            populated=True,
            cloud_manager=self
        )

    def delete_server(self, UUID):
        """
        DELETE '/server/UUID'. Permanently destroys the virtual machine.

        DOES NOT remove the storage disks.

        Returns an empty object.
        """
        return self.delete_request('/server/{0}'.format(UUID))

    def get_server_data(self, UUID):
        """
        Return '/server/uuid' data in Python dict.

        Creates object representations of any IP-address and Storage.
        """
        data = self.get_request('/server/{0}'.format(UUID))
        server = data['server']

        # Populate subobjects
        IPAddresses = IPAddress._create_ip_address_objs(server.pop('ip_addresses'),
                                                          cloud_manager=self)

        storages = Storage._create_storage_objs(server.pop('storage_devices'),
                                                cloud_manager=self)

        return server, IPAddresses, storages
