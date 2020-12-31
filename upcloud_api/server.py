from __future__ import unicode_literals
from __future__ import absolute_import

from time import sleep

from upcloud_api import Storage, IPAddress
from upcloud_api.utils import try_it_n_times


def login_user_block(username, ssh_keys, create_password=True):
    """
    Helper function for creating Server.login_user blocks.

    (see: https://www.upcloud.com/api/8-servers/#create-server)
    """
    block = {
        'create_password': 'yes' if create_password is True else 'no',
        'ssh_keys': {
            'ssh_key': ssh_keys
        }
    }

    if username:
        block['username'] = username

    return block


class Server(object):
    """
    Class representation of UpCloud Server instance.

    Partially immutable class; only fields that are persisted with the `.save()` method may be set
    with the server.field=value syntax. See __setattr__ override.
    """

    #
    # Functionality for partial immutability and repopulating the object from API.
    #

    updateable_fields = [
        'boot_order', 'core_number', 'firewall', 'hostname', 'memory_amount', 'nic_model',
        'title', 'timezone', 'video_model', 'vnc', 'vnc_password', 'plan'
    ]

    optional_fields = [
        'plan', 'core_number', 'memory_amount', 'boot_order', 'firewall', 'nic_model',
        'timezone', 'video_model', 'vnc_password', 'password_delivery', 'avoid_host',
        'login_user', 'user_data'
    ]

    def __init__(self, server=None, **kwargs):
        """
        Initialize Server.

        Use _reset to set attributes.
        Set title = hostname if title not given.
        """
        object.__setattr__(self, 'populated', False)
        self._reset(server, **kwargs)

        if not hasattr(self, 'title') and hasattr(self, 'hostname'):
            self.title = self.hostname

    def __setattr__(self, name, value):
        """
        Override to prevent updating readonly fields.
        """
        if name not in self.updateable_fields:
            raise Exception("'{0}' is a readonly field".format(name))
        else:
            object.__setattr__(self, name, value)

    def _reset(self, server, **kwargs):
        """
        Reset the server object with new values given as params.

        - server: a dict representing the server. e.g the API response.
        - kwargs: any meta fields such as cloud_manager and populated.

        Note: storage_devices and ip_addresses may be given in server as dicts or
        in kwargs as lists containing Storage and IPAddress objects.
        """
        if server:
            # handle storage, ip_address dicts and tags if they exist
            Server._handle_server_subobjs(server, kwargs.get('cloud_manager'))

            for key in server:
                object.__setattr__(self, key, server[key])

        for key in kwargs:
            object.__setattr__(self, key, kwargs[key])

    def populate(self):
        """
        Sync changes from the API to the local object.

        Note: syncs ip_addresses and storage_devices too (/server/uuid endpoint)
        """
        server, IPAddresses, storages = self.cloud_manager.get_server_data(self.uuid)
        self._reset(
            server,
            ip_addresses=IPAddresses,
            storage_devices=storages,
            populated=True
        )
        return self

    def __str__(self):
        return self.uuid

    #
    # Main functionality, 1:1 with UpCloud's API
    #

    def save(self):
        """
        Sync local changes in server's attributes to the API.

        Note: DOES NOT sync IPAddresses and storage_devices,
        use add_ip, add_storage, remove_ip, remove_storage instead.
        """
        # dict comprehension that also works with 2.6
        # http://stackoverflow.com/questions/21069668/alternative-to-dict-comprehension-prior-to-python-2-7
        kwargs = dict(
            (field, getattr(self, field))
            for field in self.updateable_fields
            if hasattr(self, field)
        )

        self.cloud_manager.modify_server(self.uuid, **kwargs)
        self._reset(kwargs)

    def destroy(self):  # noqa
        self.cloud_manager.delete_server(self.uuid)

    def shutdown(self, hard=False, timeout=30):
        """
        Shutdown/stop the server. By default, issue a soft shutdown with a timeout of 30s.

        After the a timeout a hard shutdown is performed if the server has not stopped.

        Note: API responds immediately (unlike in start), with state: started.
        This client will, however, set state as 'maintenance' to signal that the server is neither
        started nor stopped.
        """
        body = dict()
        body['stop_server'] = {
            'stop_type': 'hard' if hard else 'soft',
            'timeout': '{0}'.format(timeout)
        }

        path = '/server/{0}/stop'.format(self.uuid)
        self.cloud_manager.post_request(path, body)
        object.__setattr__(self, 'state', 'maintenance')

    def stop(self):  # noqa
        """
        Alias for shutdown.
        """
        self.shutdown()

    def start(self, timeout=120):
        """
        Start the server. Note: slow and blocking request.

        The API waits for confirmation from UpCloud's IaaS backend before responding.
        """
        path = '/server/{0}/start'.format(self.uuid)
        self.cloud_manager.post_request(path, timeout=timeout)
        object.__setattr__(self, 'state', 'started')

    def restart(self, hard=False, timeout=30, force=True):
        """
        Restart the server. By default, issue a soft restart with a timeout of 30s
        and a hard restart after the timeout.

        After the a timeout a hard restart is performed if the server has not stopped.

        Note: API responds immediately (unlike in start), with state: started.
        This client will, however, set state as 'maintenance' to signal that the server is neither
        started nor stopped.
        """
        body = dict()
        body['restart_server'] = {
            'stop_type': 'hard' if hard else 'soft',
            'timeout': '{0}'.format(timeout),
            'timeout_action': 'destroy' if force else 'ignore'
        }

        path = '/server/{0}/restart'.format(self.uuid)
        self.cloud_manager.post_request(path, body)
        object.__setattr__(self, 'state', 'maintenance')

    def add_ip(self, family='IPv4'):
        """
        Allocate a new (random) IP-address to the Server.
        """
        IP = self.cloud_manager.attach_ip(self.uuid, family)
        self.ip_addresses.append(IP)
        return IP

    def remove_ip(self, IPAddress):
        """
        Release the specified IP-address from the server.
        """
        self.cloud_manager.release_ip(IPAddress.address)
        self.ip_addresses.remove(IPAddress)

    def add_storage(self, storage=None, type='disk', address=None):
        """
        Attach the given storage to the Server.

        Default address is next available.
        """
        self.cloud_manager.attach_storage(server=self.uuid,
                                          storage=storage.uuid,
                                          storage_type=type,
                                          address=address)
        storage.address = address
        storage.type = type
        self.storage_devices.append(storage)

    def remove_storage(self, storage):
        """
        Remove Storage from a Server.

        The Storage must be a reference to an object in
        Server.storage_devices or the method will throw and Exception.

        A Storage from get_storage(uuid) will not work as it is missing the 'address' property.
        """
        if not hasattr(storage, 'address'):
            raise Exception(
                ('Storage does not have an address. '
                 'Access the Storage via Server.storage_devices '
                 'so they include an address. '
                 '(This is due how the API handles Storages)')
            )

        self.cloud_manager.detach_storage(server=self.uuid, address=storage.address)
        self.storage_devices.remove(storage)

    def add_firewall_rule(self, FirewallRule):
        """
        Add the specified FirewallRule to this server.

        Returns a FirewallRule instance that is associated with this server instance.

        Instantly calls the API, no need to call .save(). This is because firewall can not
        be configured with the same request as the rest of the Server.
        """
        return self.cloud_manager.create_firewall_rule(self, FirewallRule.to_dict())

    def remove_firewall_rule(self, FirewallRule):  # noqa
        return FirewallRule.destroy()

    def get_firewall_rules(self):
        """
        Return all FirewallRule instances that are associated with this server instance.
        """
        return self.cloud_manager.get_firewall_rules(self)

    def add_tags(self, tags):
        """
        Add tags to a server. Accepts tags as strings or Tag objects.
        """
        if self.cloud_manager.assign_tags(self.uuid, tags):
            tags = self.tags + [str(tag) for tag in tags]
            object.__setattr__(self, 'tags', tags)

    def remove_tags(self, tags):
        """
        Add tags to a server. Accepts tags as strings or Tag objects.
        """
        if self.cloud_manager.remove_tags(self, tags):
            new_tags = [tag for tag in self.tags if tag not in tags]
            object.__setattr__(self, 'tags', new_tags)

    #
    # Helper and convenience functions.
    # May perform several API requests and contain more complex logic.
    #

    def configure_firewall(self, FirewallRules):
        """
        Helper function for automatically adding several FirewallRules in series.
        """
        firewall_rule_bodies = [
            FirewallRule.to_dict()
            for FirewallRule in FirewallRules
        ]
        return self.cloud_manager.configure_firewall(self, firewall_rule_bodies)

    def prepare_post_body(self):
        """
        Prepare a JSON serializable dict from a Server instance with nested.

        Storage instances.
        """
        body = dict()
        # mandatory
        body['server'] = {
            'hostname': self.hostname,
            'zone': self.zone,
            'title': self.title,
            'storage_devices': {}
        }

        # optional fields

        for optional_field in self.optional_fields:
            if hasattr(self, optional_field):
                body['server'][optional_field] = getattr(self, optional_field)

        # set password_delivery default as 'none' to prevent API from sending
        # emails (with credentials) about each created server
        if not hasattr(self, 'password_delivery'):
            body['server']['password_delivery'] = 'none'

        # collect storage devices and create a unique title (see: Storage.title in API doc)
        # for each of them

        body['server']['storage_devices'] = {
            'storage_device': []
        }

        storage_title_id = 0  # running number for unique storage titles
        for storage in self.storage_devices:
            if not hasattr(storage, 'os') or storage.os is None:
                storage_title_id += 1
            storage_body = storage.to_dict()

            # setup default titles for storages unless the user has specified
            # them at storage.title
            if not hasattr(storage, 'title') or not storage.title:
                if hasattr(storage, 'os') and storage.os:
                    storage_body['title'] = self.hostname + ' OS disk'
                else:
                    storage_body['title'] = self.hostname + ' storage disk ' + str(storage_title_id)


            # figure out the storage `action` parameter
            # public template
            if hasattr(storage, 'os') and storage.os:
                storage_body['action'] = 'clone'
                storage_body['storage'] = storage.os

            # private template
            elif hasattr(storage, 'uuid'):
                storage_body['action'] = 'clone'
                storage_body['storage'] = storage.uuid

            # create a new storage
            else:
                storage_body['action'] = 'create'

            body['server']['storage_devices']['storage_device'].append(storage_body)

        if hasattr(self, 'ip_addresses') and self.ip_addresses:
            body['server']['ip_addresses'] = {
                'ip_address': [
                    ip.to_dict() for ip in self.ip_addresses
                ]
            }


        return body

    def to_dict(self):
        """
        Prepare a JSON serializable dict for read-only purposes.

        Includes storages and IP-addresses.
        Use prepare_post_body for POST and .save() for PUT.
        """
        fields = dict(vars(self).items())

        if self.populated:
            fields['ip_addresses'] = []
            fields['storage_devices'] = []
            for ip in self.ip_addresses:
                fields['ip_addresses'].append({
                    'address': ip.address,
                    'access': ip.access,
                    'family': ip.family
                })

            for storage in self.storage_devices:
                fields['storage_devices'].append({
                    'address': storage.address,
                    'storage': storage.uuid,
                    'storage_size': storage.size,
                    'storage_title': storage.title,
                    'type': storage.type,
                })

        del fields['populated']
        del fields['cloud_manager']
        return fields

    def get_ip(self, access='public', addr_family=None, strict=None):
        """
        Return the server's IP address.

        Params:
        - addr_family: IPv4, IPv6 or None. None prefers IPv4 but will
                       return IPv6 if IPv4 addr was not available.
        - access: 'public' or 'private'
        """
        if addr_family not in ['IPv4', 'IPv6', None]:
            raise Exception("`addr_family` must be 'IPv4', 'IPv6' or None")

        if access not in ['private', 'public']:
            raise Exception("`access` must be 'public' or 'private'")

        if not hasattr(self, 'ip_addresses'):
            self.populate()

        # server can have several public or private IPs
        ip_addrs = [
            ip_addr for ip_addr in self.ip_addresses
            if ip_addr.access == access
        ]

        # prefer addr_family (or IPv4 if none given)
        preferred_family = addr_family if addr_family else 'IPv4'
        for ip_addr in ip_addrs:
            if ip_addr.family == preferred_family:
                return ip_addr.address

        # any IP (of the right access) will do if available and addr_family is None
        return ip_addrs[0].address if ip_addrs and not addr_family else None

    def get_public_ip(self, addr_family=None, *args, **kwargs):
        """Alias for get_ip('public')"""
        return self.get_ip('public', addr_family, *args, **kwargs)

    def get_private_ip(self, addr_family=None, *args, **kwargs):
        """Alias for get_ip('private')"""
        return self.get_ip('private', addr_family, *args, **kwargs)

    def _wait_for_state_change(self, target_states, update_interval=10):
        """
        Blocking wait until target_state reached. update_interval is in seconds.

        Warning: state change must begin before calling this method.
        """
        while self.state not in target_states:
            if self.state == 'error':
                raise Exception('server is in error state')

            # update server state every 10s
            sleep(update_interval)
            self.populate()

    def ensure_started(self):
        """
        Start a server and waits (blocking wait) until it is fully started.
        """
        # server is either starting or stopping (or error)
        if self.state in ['maintenance', 'error']:
            self._wait_for_state_change(['stopped', 'started'])

        if self.state == 'stopped':
            self.start()
            self._wait_for_state_change(['started'])

        if self.state == 'started':
            return True
        else:
            # something went wrong, fail explicitly
            raise Exception('unknown server state: ' + self.state)

    def stop_and_destroy(self, sync=True):
        """
        Destroy a server and its storages. Stops the server before destroying.

        Syncs the server state from the API, use sync=False to disable.
        """
        def _self_destruct():
            """destroy the server and all storages attached to it."""

            # try_it_n_times util is used as a convenience because
            # Servers and Storages can fluctuate between "maintenance" and their
            # original state due to several different reasons especially when
            # destroying infrastructure.

            # first destroy server
            try_it_n_times(operation=self.destroy,
                           expected_error_codes=['SERVER_STATE_ILLEGAL'],
                           custom_error='destroying server failed')

            # storages may be deleted instantly after server DELETE
            for storage in self.storage_devices:
                try_it_n_times(operation=storage.destroy,
                               expected_error_codes=['STORAGE_STATE_ILLEGAL'],
                               custom_error='destroying storage failed')

        if sync:
            self.populate()

        # server is either starting or stopping (or error)
        if self.state in ['maintenance', 'error']:
            self._wait_for_state_change(['stopped', 'started'])

        if self.state == 'started':
            try_it_n_times(operation=self.stop,
                           expected_error_codes=['SERVER_STATE_ILLEGAL'],
                           custom_error='stopping server failed')

            self._wait_for_state_change(['stopped'])

        if self.state == 'stopped':
            _self_destruct()
        else:
            raise Exception('unknown server state: ' + self.state)

    @classmethod
    def _handle_server_subobjs(cls, server, cloud_manager):
        ip_data = server.pop('ip_addresses', None)
        storage_data = server.pop('storage_devices', None)
        tags = server.pop('tags', None)

        if ip_data:
            ip_addresses = IPAddress._create_ip_address_objs(ip_data, cloud_manager=cloud_manager)
            server['ip_addresses'] = ip_addresses

        if storage_data:
            storages = Storage._create_storage_objs(storage_data, cloud_manager=cloud_manager)
            server['storage_devices'] = storages

        if tags and 'tag' in tags:
            server['tags'] = tags['tag']

    @classmethod
    def _create_server_obj(cls, server, cloud_manager):
        cls._handle_server_subobjs(server, cloud_manager)

        server_dict = dict()
        server_dict.update(server)
        server_dict['cloud_manager'] = cloud_manager

        return Server(**server_dict)
