from upcloud_api.api import API
from upcloud_api.ip_address import IPAddress
from upcloud_api.server import Server
from upcloud_api.server_group import ServerGroup
from upcloud_api.storage import BackupDeletionPolicy, Storage


class ServerManager:
    """
    Functions for managing servers. Intended to be used as a mixin for CloudManager.
    """

    api: API

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
            tag_list = ':'.join(tags_has_all)
            request = f'/server/tag/{tag_list}'

        if tags_has_one:
            tags_has_one = [str(tag) for tag in tags_has_one]
            tag_list = ','.join(tags_has_one)
            request = f'/server/tag/{tag_list}'

        servers = self.api.get_request(request)['servers']['server']

        server_list = list()
        for server in servers:
            server_list.append(Server(server, cloud_manager=self))

        if populate:
            for server_instance in server_list:
                server_instance.populate()

        return server_list

    def get_server(self, uuid: str) -> Server:
        """
        Return a (populated) Server instance.
        """
        server, ip_addresses, storages = self.get_server_data(uuid)

        return Server(
            server,
            ip_addresses=ip_addresses,
            storage_devices=storages,
            populated=True,
            cloud_manager=self,
        )

    def get_server_by_ip(self, ip_address: str):
        """
        Return a (populated) Server instance by its IP.

        Uses GET '/ip_address/x.x.x.x' to retrieve machine UUID using IP-address.
        """
        data = self.api.get_request(f'/ip_address/{ip_address}')
        UUID = data['ip_address']['server']
        return self.get_server(UUID)

    def create_server(self, server: Server) -> Server:
        """
        Create a server and its storages based on a (locally created) Server object.

        Populates the given Server instance with the API response.

        0.3.0: also supports giving the entire POST body as a dict that is directly
        serialised into JSON. Refer to the REST API documentation for correct format.

        Example:
        -------
        server1 = Server( core_number = 1,
              memory_amount = 1024,
              hostname = "my.example.1",
              zone = "uk-lon1",
              labels = [Label('role', 'example')],
              storage_devices = [
                Storage(os = "01000000-0000-4000-8000-000030240200", size=10, tier=maxiops, title='Example OS disk'),
                Storage(size=10, labels=[Label('usage', 'data_disk')]),
                Storage()
              title = "My Example Server"
            ])
        manager.create_server(server1)

        One storage should contain an OS. Otherwise storage fields are optional.
        - size defaults to 10,
        - title defaults to hostname + " OS disk" and hostname + " storage disk id"
          (id is a running starting from 1)
        - tier defaults to maxiops
        - valid operating systems are for example:
          * Debian GNU/Linux 12 (Bookworm): 01000000-0000-4000-8000-000020070100
          * Ubuntu Server 24.04 LTS (Noble Numbat): 01000000-0000-4000-8000-000030240200
          * Rocky Linux 9: 01000000-0000-4000-8000-000150020100
          * Windows Server 2022 Standard: 01000000-0000-4000-8000-000010080300
          (for a more up-to-date listing, use UpCloud's CLI: `upctl storage list --public --template`.)

        """
        if isinstance(server, Server):
            body = server.prepare_post_body()
        else:
            server = Server._create_server_obj(server, cloud_manager=self)
            body = server.prepare_post_body()

        res = self.api.post_request('/server', body)

        server_to_return = server
        server_to_return._reset(res['server'], cloud_manager=self, populated=True)
        return server_to_return

    def modify_server(self, uuid: str, **kwargs) -> Server:
        """
        modify_server allows updating the server's updateable_fields.

        Note: Server's IP-addresses and Storages are managed by their own add/remove methods.
        """
        body = dict()
        body['server'] = {}
        for arg in kwargs:
            if arg not in Server.updateable_fields:
                Exception(f'{arg} is not an updateable field')
            body['server'][arg] = kwargs[arg]

        res = self.api.put_request(f'/server/{uuid}', body)
        server = res['server']

        # Populate subobjects
        IPAddresses = IPAddress._create_ip_address_objs(
            server.pop('ip_addresses'), cloud_manager=self
        )

        storages = Storage._create_storage_objs(server.pop('storage_devices'), cloud_manager=self)

        return Server(
            server,
            ip_addresses=IPAddresses,
            storage_devices=storages,
            populated=True,
            cloud_manager=self,
        )

    def delete_server(
        self,
        uuid: str,
        delete_storages: bool = False,
        backups: BackupDeletionPolicy = BackupDeletionPolicy.KEEP,
    ):
        """
        DELETE '/server/UUID'. Permanently destroys the virtual machine.

        Does remove storage disks if delete_storages is defined as True.

        Does remove backups of the attached storages if

        Returns an empty object.
        """
        storages = '1' if delete_storages else '0'

        return self.api.delete_request(
            f'/server/{uuid}?storages={storages}&backups={backups.value}'
        )

    def get_server_data(self, uuid: str):
        """
        Return '/server/uuid' data in Python dict.

        Creates object representations of any IP-address and Storage.
        """
        data = self.api.get_request(f'/server/{uuid}')
        server = data['server']

        # Populate subobjects
        IPAddresses = IPAddress._create_ip_address_objs(
            server.pop('ip_addresses'), cloud_manager=self
        )

        storages = Storage._create_storage_objs(server.pop('storage_devices'), cloud_manager=self)

        return server, IPAddresses, storages

    def create_server_group(self, server_group: ServerGroup) -> ServerGroup:
        """
        Creates a new server group. Allows including servers and defining labels.
        """
        body = server_group.to_dict()

        res = self.api.post_request('/server-group', body)
        return ServerGroup(cloud_manager=self, **res['server_group'])

    def get_server_group(self, uuid: str) -> ServerGroup:
        """
        Fetches server group details and returns a ServerGroup object.
        """
        data = self.api.get_request(f'/server-group/{uuid}')
        return ServerGroup(cloud_manager=self, **data['server_group'])

    def delete_server_group(self, uuid: str):
        """
        DELETE '/server-group/UUID'. Destroys the server group, but not attached servers.

        Returns an empty object.
        """
        return self.api.delete_request(f'/server-group/{uuid}')
