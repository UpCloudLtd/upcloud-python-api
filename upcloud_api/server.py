from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from builtins import str
from future import standard_library
standard_library.install_aliases()

from upcloud_api.base import BaseAPI
from upcloud_api import Storage, IP_address

from time import sleep


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


class Server(BaseAPI):
  """
  Object representation of UpCloud Server instance.

  Partially immutable class; only fields that are persisted with the `.save()` method may be set
  with the server.field = value syntax. See __setattr__ override.
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
    'login_user'
  ]


  def __init__(self, server=None, **kwargs):
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
    Resets the server object with new values given as params.
    - server: a dict representing the server. e.g the API response.
    - kwargs: any meta fields such as cloud_manager and populated.

    Note: storage_devices and ip_addresses may be given in server as dicts or
    in kwargs as lists containing Storage and IP_address objects.
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
    server, IP_addresses, storages = self.cloud_manager.get_server_data(self.uuid)
    self._reset(
      server,
      ip_addresses = IP_addresses,
      storage_devices = storages,
      populated = True
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

    Note: DOES NOT sync IP_addresses and storage_devices,
    use add_IP, add_storage, remove_IP, remove_storage instead.
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

  def destroy(self):
    self.cloud_manager.delete_server(self.uuid)

  def shutdown(self):
    """
    Shutdown/stop the server. Issue a soft shutdown with a timeout of 30s.
    After the a timeout a hard shutdown is performed if the server has not stopped.

    Note: API responds immediately (unlike in start), with state: started.
    This client will, however, set state as 'maintenance' to signal that the server is neither
    started nor stopped.
    """
    body = dict()
    body['stop_server'] = {
      'stop_type' : 'soft',
      'timeout' : '30'
    }

    path = '/server/{0}/stop'.format(self.uuid)
    self.cloud_manager.post_request(path, body)
    object.__setattr__(self, 'state', 'maintenance')


  def stop(self):
    """
    Alias for shutdow.
    """
    self.shutdown()

  def start(self):
    """
    Starts the server. Note: slow and blocking request.
    The API waits for confirmation from UpCloud's IaaS backend before responding.
    """
    path = '/server/{0}/start'.format(self.uuid)
    res = self.cloud_manager.post_request(path)
    object.__setattr__(self, 'state', 'started')

  def restart(self):
    """
    Restart the server. Issue a soft restart with a timeout of 30s.
    After the a timeout a hard restart is performed if the server has not stopped.

    Note: API responds immediately (unlike in start), with state: started.
    This client will, however, set state as 'maintenance' to signal that the server is neither
    started nor stopped.
    """
    body = dict()
    body['restart_server'] = {
      'stop_type' : 'soft',
      'timeout' : '30',
      'timeout_action' : 'destroy'
    }

    path = '/server/{0}/restart'.format(self.uuid)
    self.cloud_manager.post_request(path, body)
    object.__setattr__(self, 'state', 'maintenance')

  def add_IP(self, family='IPv4'):
    """
    Allocate a new (random) IP-address to the Server.
    """
    IP = self.cloud_manager.attach_IP(self.uuid, family)
    self.ip_addresses.append(IP)
    return IP

  def remove_IP(self, IP_address):
    """
    Release the specified IP-address from the server.
    """
    self.cloud_manager.release_IP(IP_address.address)
    self.ip_addresses.remove(IP_address)


  def add_storage(self, Storage=None, type='disk', address=None):
    """
    To add a Storage instance to a server: add_storage(Storage).
    Default address is next available. To add a CDROM slot: add_storage('cdrom').
    """
    self.cloud_manager.attach_storage(
      server_uuid=self.uuid,
      storage_uuid=Storage.uuid,
      storage_type=type,
      address=address
    )
    self.storage_devices.append(Storage)

  def remove_storage(self, Storage):
    """
    Remove Storage from a Server. The Storage must be a reference to an object in
    Server.storage_devices or the method will throw and Exception.

    A Storage from get_storage(uuid) will not work as it is missing the 'address' property.
    """
    if not hasattr(Storage, 'address'):
      raise Exception(
        ('Storage does not have an address. Access the Storage via Server.storage_devices so '
         'they include address. (This is due how the API handles Storages)')
      )

    self.cloud_manager.detach_storage(server_uuid=self.uuid, address=Storage.address)
    self.storage_devices.remove(Storage)

  def add_firewall_rule(self, FirewallRule):
    """
    Adds the specified FirewallRule to this server. Returns a FirewallRule instance
    that is associated with this server instance.

    Instantly calls the API, no need to call .save(). This is because firewall can not
    be configured with the same request as the rest of the Server.
    """
    firewall_rule_body = FirewallRule.prepare_post_body()
    firewall_rule = self.cloud_manager.create_firewall_rule(self.uuid, firewall_rule_body)
    firewall_rule._associate_with_server(self)
    return firewall_rule

  def remove_firewall_rule(self, FirewallRule):
    return FirewallRule.destroy()


  def get_firewall_rules(self):
    """
    Returns all FirewallRule instances that are associated with this server instance.
    """
    firewall_rules = self.cloud_manager.get_firewall_rules(self.uuid)
    for firewall_rule in firewall_rules:
      firewall_rule._associate_with_server(self)
    return firewall_rules


  def add_tags(self, tags):
    """
    Add tags to a server. Accepts tags as strings or Tag objects.
    """
    if self.cloud_manager.assign_tags(self.uuid, tags):
      tags = self.tags + [ str(tag) for tag in tags ]
      object.__setattr__(self, 'tags', tags)


  def remove_tags(self, tags):
    """
    Add tags to a server. Accepts tags as strings or Tag objects.
    """
    if self.cloud_manager.remove_tags(self.uuid, tags):
      new_tags = [ tag for tag in self.tags if tag not in tags ]
      object.__setattr__(self, 'tags', new_tags)


  #
  # Helper and convenience functions.
  # May perform several API requests and contain more complex logic.
  #

  def configure_firewall(self, FirewallRules):
    """
    Helper function for automatically adding several FirewallRules in series.
    """
    firewall_rule_bodies = []
    for FirewallRule in FirewallRules:
      firewall_rule_bodies.append(FirewallRule.prepare_post_body())

    firewall_rules = self.cloud_manager.configure_firewall(self.uuid, firewall_rule_bodies)
    for firewall_rule in firewall_rules:
      firewall_rule._associate_with_server(self)
    return firewall_rules


  def prepare_post_body(self):
    """
    Prepares a JSON serializable dict from a Server instance with nested
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

    storage_title_id = 0 # running number for unique storage titles
    for storage in self.storage_devices:
      if storage.os == None:
        storage_title_id +=  1
      storage_body = storage.prepare_post_body(self.hostname, storage_title_id)
      body['server']['storage_devices']['storage_device'].append(storage_body)

    return body


  def to_dict(self):
    """
    Prepares a JSON serializable dict for read-only purposes. Includes storages and IP-addresses.
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


  def get_public_ip(self, addr_family='IPv4', strict=False):
    """
    Returns a server's public IP.

    Params:
    - addr_family: prefer IPv4 (default) or IPv6.
    - strict mode (false/off by default): only return IP if it belongs to addr_family (IPv4 or IPv6).

    Tries to fetch Server data from API if ip_addresses not set.

    New in 3.4:
    - possibility to specify which protocol is preferred via addr_family,
      instead of always preferring IPv4.
    - strict mode
    """

    if addr_family not in ['IPv4', 'IPv6']:
        raise Exception("`addr_family` must be 'IPv4' or 'IPv6'")

    if not hasattr(self, 'ip_addresses'):
        self.populate()

    # server can have several public IPs
    public_ip_addrs = []
    for ip_addr in self.ip_addresses:
        if ip_addr.access == 'public':
            public_ip_addrs.append(ip_addr)

    if not public_ip_addrs:
        return None

    # prefer addr_family
    for ip_addr in public_ip_addrs:
        if ip_addr.family == addr_family:
            return ip_addr.address

    # strict mode: either find addr_family or don't
    if strict:
        return None

    # not stict mode: any public IP will do if addr_family didn't match
    return public_ip_addrs[0].address


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
    """Starts a server and waits (blocking wait) until a it is fully started."""

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


  def stop_and_destroy(self):
    """Destroy a server and its storages. Stops the server (blocking wait) before destroying."""

    def destroy_storages():
      # list view does not return all server info, populate if necessary
      if not hasattr(self, 'storage_devices'):
        self.populate()

      # destroy the server and all storages attached to it
      self.destroy()
      for storage in self.storage_devices:
        storage.destroy()

    # server is either starting or stopping (or error)
    if self.state in ['maintenance', 'error']:
      self._wait_for_state_change(['stopped', 'started'])

    # server is started
    if self.state != 'stopped':
      self.stop()
      self._wait_for_state_change(['stopped'])

    if self.state == 'stopped':
      destroy_storages()
    else:
      # something went wrong, fail explicitly
      raise Exception('unknown server state: ' + self.state)


  @classmethod
  def _handle_server_subobjs(cls, server, cloud_manager):
    ip_data = server.pop('ip_addresses', None)
    storage_data = server.pop('storage_devices', None)
    tags = server.pop('tags', None)

    if ip_data:
      ip_addresses = IP_address._create_ip_address_objs(ip_data, cloud_manager = cloud_manager)
      server['ip_addresses'] = ip_addresses

    if storage_data:
      storages = Storage._create_storage_objs(storage_data, cloud_manager = cloud_manager)
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
