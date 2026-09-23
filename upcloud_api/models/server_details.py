from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_boolean_onoff import ServerBooleanOnoff
from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_details_firewall_private_default_incoming_action import (
    ServerDetailsFirewallPrivateDefaultIncomingAction,
)
from ..models.server_details_firewall_private_default_outgoing_action import (
    ServerDetailsFirewallPrivateDefaultOutgoingAction,
)
from ..models.server_details_firewall_public_default_incoming_action import (
    ServerDetailsFirewallPublicDefaultIncomingAction,
)
from ..models.server_details_firewall_public_default_outgoing_action import (
    ServerDetailsFirewallPublicDefaultOutgoingAction,
)
from ..models.server_nic_model import ServerNicModel
from ..models.server_remote_access_enabled import ServerRemoteAccessEnabled
from ..models.server_remote_access_type import ServerRemoteAccessType
from ..models.server_state import ServerState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_details_devices import ServerDetailsDevices
    from ..models.server_ip_addresses import ServerIpAddresses
    from ..models.server_labels import ServerLabels
    from ..models.server_networking import ServerNetworking
    from ..models.server_storage_devices_response import ServerStorageDevicesResponse
    from ..models.server_tags_type_1 import ServerTagsType1


T = TypeVar("T", bound="ServerDetails")


@_attrs_define
class ServerDetails:
    """Detailed public information about a Cloud Server

    Example:
        {'boot_order': 'disk', 'core_number': '12', 'created': 1705320000, 'firewall': 'on', 'host': 7653311107,
            'hostname': 'server1.example.com', 'labels': {'label': [{'key': 'env', 'value': 'development'}]}, 'license':
            '0', 'memory_amount': '130048', 'nic_model': 'virtio', 'plan': 'GPU-12xCPU-128GB-2xL40S', 'plan_ipv4_bytes':
            '3565675343', 'plan_ipv6_bytes': '4534432', 'remote_access_enabled': 'yes', 'remote_access_host': 'fi-
            hel1.vnc.upcloud.com', 'remote_access_password': 'aabbccdd', 'remote_access_port': '3000', 'remote_access_type':
            'vnc', 'server_group': '0b3d85b4-b3be-46ca-a1e2-3b5d40d60fb1', 'simple_backup': '0100,dailies', 'state':
            'started', 'storage_devices': {'storage_device': [{'address': 'virtio:0', 'boot_disk': '1', 'labels': [],
            'storage': '012580a1-32a1-466e-a323-689ca16f2d43', 'storage_encrypted': 'yes', 'storage_size': 20,
            'storage_title': 'Operating system disk', 'type': 'disk'}]}, 'tags': {'tag': ['DEV', 'Ubuntu']}, 'timezone':
            'UTC', 'title': 'Development GPU server', 'uuid': '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'video_model':
            'cirrus', 'zone': 'fi-hel1'}

    Attributes:
        core_number (str): Number of CPU cores.
        created (int): Creation timestamp (Unix epoch time) Example: 1705320000.
        hostname (str): Cloud Server hostname.
        license_ (str): Hourly license price
        memory_amount (str): Memory in MiB.
        state (ServerState): Current state of the Cloud Server Example: started.
        title (str): Display title.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        zone (str): Zone identifier
        boot_order (str | Unset): Boot device order (comma-separated list) Example: cdrom,disk.
        devices (ServerDetailsDevices | Unset):
        firewall (ServerBooleanOnoff | Unset): Boolean value represented as on/off Example: on.
        firewall_private (ServerBooleanOnoff | Unset): Boolean value represented as on/off Example: on.
        firewall_private_default_incoming_action (ServerDetailsFirewallPrivateDefaultIncomingAction | Unset):
        firewall_private_default_outgoing_action (ServerDetailsFirewallPrivateDefaultOutgoingAction | Unset):
        firewall_public_default_incoming_action (ServerDetailsFirewallPublicDefaultIncomingAction | Unset):
        firewall_public_default_outgoing_action (ServerDetailsFirewallPublicDefaultOutgoingAction | Unset):
        host (int | Unset): Encoded Private Cloud host ID
        ip_addresses (ServerIpAddresses | Unset): IP addresses assigned to the Cloud Server Example: {'ip_address':
            [{'access': 'utility', 'address': '10.0.0.10', 'family': 'IPv4'}]}.
        labels (ServerLabels | Unset): Cloud Server labels Example: {'label': [{'key': 'env', 'value': 'production'}]}.
        metadata (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        networking (ServerNetworking | Unset): Network interfaces configured for the Cloud Server Example:
            {'interfaces': {'interface': [{'bootable': 'no', 'index': 4, 'ip_addresses': {'ip_address': [{'address':
            '10.0.0.20', 'dhcp_provided': 'yes', 'family': 'IPv4', 'floating': 'no', 'release_policy': 'release'}]}, 'mac':
            'de:ff:ff:ff:cc:20', 'network': '0374ce47-4303-4490-987d-32dc96cfd79b', 'source_ip_filtering': 'yes', 'type':
            'private'}]}}.
        nic_model (ServerNicModel | Unset): Network interface card model Example: virtio.
        plan (str | Unset): Server plan identifier
        plan_ipv4_bytes (str | Unset): Public IPv4 outbound traffic this billing month, in bytes.
        plan_ipv6_bytes (str | Unset): Public IPv6 outbound traffic this billing month, in bytes.
        password (str | Unset): One-time login password returned when the Cloud Server is created.
        progress (str | Unset): Progress percentage for an operation in progress.
        remote_access_enabled (ServerRemoteAccessEnabled | Unset): Whether remote access is enabled Example: yes.
        remote_access_host (str | Unset): Remote access hostname.
        remote_access_password (str | Unset): Eight-character alphanumeric password used to authenticate remote access
            Example: A1b2C3d4.
        remote_access_port (str | Unset): Remote access port.
        remote_access_type (ServerRemoteAccessType | Unset): Protocol used for remote access Example: vnc.
        server_group (None | str | Unset): UUID of the server group containing the Cloud Server, or null when the Cloud
            Server is not in a group. Example: 0b3d85b4-b3be-46ca-a1e2-3b5d40d60fb1.
        simple_backup (None | str | Unset): Simple backup start time in UTC and frequency, separated by a comma, or no
            to disable
        storage_devices (ServerStorageDevicesResponse | Unset): Storage devices attached to a Cloud Server Example:
            {'storage_device': [{'address': 'virtio:0', 'boot_disk': '1', 'labels': [], 'storage':
            '012580a1-32a1-466e-a323-689ca16f2d43', 'storage_encrypted': 'yes', 'storage_size': 20, 'storage_title':
            'Operating system disk', 'type': 'disk'}]}.
        tags (list[str] | ServerTagsType1 | Unset): tags can be an empty array or an object with a tag array Example:
            {'tag': []}.
        timezone (str | Unset): Configured timezone.
        username (str | Unset): Username for an account.
        video_model (str | Unset): Video adapter model Example: vga.
    """

    core_number: str
    created: int
    hostname: str
    license_: str
    memory_amount: str
    state: ServerState
    title: str
    uuid: UUID
    zone: str
    boot_order: str | Unset = UNSET
    devices: ServerDetailsDevices | Unset = UNSET
    firewall: ServerBooleanOnoff | Unset = UNSET
    firewall_private: ServerBooleanOnoff | Unset = UNSET
    firewall_private_default_incoming_action: ServerDetailsFirewallPrivateDefaultIncomingAction | Unset = UNSET
    firewall_private_default_outgoing_action: ServerDetailsFirewallPrivateDefaultOutgoingAction | Unset = UNSET
    firewall_public_default_incoming_action: ServerDetailsFirewallPublicDefaultIncomingAction | Unset = UNSET
    firewall_public_default_outgoing_action: ServerDetailsFirewallPublicDefaultOutgoingAction | Unset = UNSET
    host: int | Unset = UNSET
    ip_addresses: ServerIpAddresses | Unset = UNSET
    labels: ServerLabels | Unset = UNSET
    metadata: ServerBooleanYesno | Unset = UNSET
    networking: ServerNetworking | Unset = UNSET
    nic_model: ServerNicModel | Unset = UNSET
    plan: str | Unset = UNSET
    plan_ipv4_bytes: str | Unset = UNSET
    plan_ipv6_bytes: str | Unset = UNSET
    password: str | Unset = UNSET
    progress: str | Unset = UNSET
    remote_access_enabled: ServerRemoteAccessEnabled | Unset = UNSET
    remote_access_host: str | Unset = UNSET
    remote_access_password: str | Unset = UNSET
    remote_access_port: str | Unset = UNSET
    remote_access_type: ServerRemoteAccessType | Unset = UNSET
    server_group: None | str | Unset = UNSET
    simple_backup: None | str | Unset = UNSET
    storage_devices: ServerStorageDevicesResponse | Unset = UNSET
    tags: list[str] | ServerTagsType1 | Unset = UNSET
    timezone: str | Unset = UNSET
    username: str | Unset = UNSET
    video_model: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        core_number = self.core_number

        created = self.created

        hostname = self.hostname

        license_ = self.license_

        memory_amount = self.memory_amount

        state = self.state.value

        title = self.title

        uuid = str(self.uuid)

        zone = self.zone

        boot_order = self.boot_order

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        firewall: str | Unset = UNSET
        if not isinstance(self.firewall, Unset):
            firewall = self.firewall.value

        firewall_private: str | Unset = UNSET
        if not isinstance(self.firewall_private, Unset):
            firewall_private = self.firewall_private.value

        firewall_private_default_incoming_action: str | Unset = UNSET
        if not isinstance(self.firewall_private_default_incoming_action, Unset):
            firewall_private_default_incoming_action = self.firewall_private_default_incoming_action.value

        firewall_private_default_outgoing_action: str | Unset = UNSET
        if not isinstance(self.firewall_private_default_outgoing_action, Unset):
            firewall_private_default_outgoing_action = self.firewall_private_default_outgoing_action.value

        firewall_public_default_incoming_action: str | Unset = UNSET
        if not isinstance(self.firewall_public_default_incoming_action, Unset):
            firewall_public_default_incoming_action = self.firewall_public_default_incoming_action.value

        firewall_public_default_outgoing_action: str | Unset = UNSET
        if not isinstance(self.firewall_public_default_outgoing_action, Unset):
            firewall_public_default_outgoing_action = self.firewall_public_default_outgoing_action.value

        host = self.host

        ip_addresses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        metadata: str | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.value

        networking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.networking, Unset):
            networking = self.networking.to_dict()

        nic_model: str | Unset = UNSET
        if not isinstance(self.nic_model, Unset):
            nic_model = self.nic_model.value

        plan = self.plan

        plan_ipv4_bytes = self.plan_ipv4_bytes

        plan_ipv6_bytes = self.plan_ipv6_bytes

        password = self.password

        progress = self.progress

        remote_access_enabled: str | Unset = UNSET
        if not isinstance(self.remote_access_enabled, Unset):
            remote_access_enabled = self.remote_access_enabled.value

        remote_access_host = self.remote_access_host

        remote_access_password = self.remote_access_password

        remote_access_port = self.remote_access_port

        remote_access_type: str | Unset = UNSET
        if not isinstance(self.remote_access_type, Unset):
            remote_access_type = self.remote_access_type.value

        server_group: None | str | Unset
        if isinstance(self.server_group, Unset):
            server_group = UNSET
        else:
            server_group = self.server_group

        simple_backup: None | str | Unset
        if isinstance(self.simple_backup, Unset):
            simple_backup = UNSET
        else:
            simple_backup = self.simple_backup

        storage_devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_devices, Unset):
            storage_devices = self.storage_devices.to_dict()

        tags: dict[str, Any] | list[str] | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags.to_dict()

        timezone = self.timezone

        username = self.username

        video_model = self.video_model

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "core_number": core_number,
                "created": created,
                "hostname": hostname,
                "license": license_,
                "memory_amount": memory_amount,
                "state": state,
                "title": title,
                "uuid": uuid,
                "zone": zone,
            }
        )
        if boot_order is not UNSET:
            field_dict["boot_order"] = boot_order
        if devices is not UNSET:
            field_dict["devices"] = devices
        if firewall is not UNSET:
            field_dict["firewall"] = firewall
        if firewall_private is not UNSET:
            field_dict["firewall_private"] = firewall_private
        if firewall_private_default_incoming_action is not UNSET:
            field_dict["firewall_private_default_incoming_action"] = firewall_private_default_incoming_action
        if firewall_private_default_outgoing_action is not UNSET:
            field_dict["firewall_private_default_outgoing_action"] = firewall_private_default_outgoing_action
        if firewall_public_default_incoming_action is not UNSET:
            field_dict["firewall_public_default_incoming_action"] = firewall_public_default_incoming_action
        if firewall_public_default_outgoing_action is not UNSET:
            field_dict["firewall_public_default_outgoing_action"] = firewall_public_default_outgoing_action
        if host is not UNSET:
            field_dict["host"] = host
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if networking is not UNSET:
            field_dict["networking"] = networking
        if nic_model is not UNSET:
            field_dict["nic_model"] = nic_model
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_ipv4_bytes is not UNSET:
            field_dict["plan_ipv4_bytes"] = plan_ipv4_bytes
        if plan_ipv6_bytes is not UNSET:
            field_dict["plan_ipv6_bytes"] = plan_ipv6_bytes
        if password is not UNSET:
            field_dict["password"] = password
        if progress is not UNSET:
            field_dict["progress"] = progress
        if remote_access_enabled is not UNSET:
            field_dict["remote_access_enabled"] = remote_access_enabled
        if remote_access_host is not UNSET:
            field_dict["remote_access_host"] = remote_access_host
        if remote_access_password is not UNSET:
            field_dict["remote_access_password"] = remote_access_password
        if remote_access_port is not UNSET:
            field_dict["remote_access_port"] = remote_access_port
        if remote_access_type is not UNSET:
            field_dict["remote_access_type"] = remote_access_type
        if server_group is not UNSET:
            field_dict["server_group"] = server_group
        if simple_backup is not UNSET:
            field_dict["simple_backup"] = simple_backup
        if storage_devices is not UNSET:
            field_dict["storage_devices"] = storage_devices
        if tags is not UNSET:
            field_dict["tags"] = tags
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if username is not UNSET:
            field_dict["username"] = username
        if video_model is not UNSET:
            field_dict["video_model"] = video_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_details_devices import ServerDetailsDevices  # noqa: PLC0415
        from ..models.server_ip_addresses import ServerIpAddresses  # noqa: PLC0415
        from ..models.server_labels import ServerLabels  # noqa: PLC0415
        from ..models.server_networking import ServerNetworking  # noqa: PLC0415
        from ..models.server_storage_devices_response import ServerStorageDevicesResponse  # noqa: PLC0415
        from ..models.server_tags_type_1 import ServerTagsType1  # noqa: PLC0415

        d = dict(src_dict)
        core_number = d.pop("core_number")

        created = d.pop("created")

        hostname = d.pop("hostname")

        license_ = d.pop("license")

        memory_amount = d.pop("memory_amount")

        state = ServerState(d.pop("state"))

        title = d.pop("title")

        uuid = UUID(d.pop("uuid"))

        zone = d.pop("zone")

        boot_order = d.pop("boot_order", UNSET)

        _devices = d.pop("devices", UNSET)
        devices: ServerDetailsDevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = ServerDetailsDevices.from_dict(_devices)

        _firewall = d.pop("firewall", UNSET)
        firewall: ServerBooleanOnoff | Unset
        if isinstance(_firewall, Unset):
            firewall = UNSET
        else:
            firewall = ServerBooleanOnoff(_firewall)

        _firewall_private = d.pop("firewall_private", UNSET)
        firewall_private: ServerBooleanOnoff | Unset
        if isinstance(_firewall_private, Unset):
            firewall_private = UNSET
        else:
            firewall_private = ServerBooleanOnoff(_firewall_private)

        _firewall_private_default_incoming_action = d.pop("firewall_private_default_incoming_action", UNSET)
        firewall_private_default_incoming_action: ServerDetailsFirewallPrivateDefaultIncomingAction | Unset
        if isinstance(_firewall_private_default_incoming_action, Unset):
            firewall_private_default_incoming_action = UNSET
        else:
            firewall_private_default_incoming_action = ServerDetailsFirewallPrivateDefaultIncomingAction(
                _firewall_private_default_incoming_action
            )

        _firewall_private_default_outgoing_action = d.pop("firewall_private_default_outgoing_action", UNSET)
        firewall_private_default_outgoing_action: ServerDetailsFirewallPrivateDefaultOutgoingAction | Unset
        if isinstance(_firewall_private_default_outgoing_action, Unset):
            firewall_private_default_outgoing_action = UNSET
        else:
            firewall_private_default_outgoing_action = ServerDetailsFirewallPrivateDefaultOutgoingAction(
                _firewall_private_default_outgoing_action
            )

        _firewall_public_default_incoming_action = d.pop("firewall_public_default_incoming_action", UNSET)
        firewall_public_default_incoming_action: ServerDetailsFirewallPublicDefaultIncomingAction | Unset
        if isinstance(_firewall_public_default_incoming_action, Unset):
            firewall_public_default_incoming_action = UNSET
        else:
            firewall_public_default_incoming_action = ServerDetailsFirewallPublicDefaultIncomingAction(
                _firewall_public_default_incoming_action
            )

        _firewall_public_default_outgoing_action = d.pop("firewall_public_default_outgoing_action", UNSET)
        firewall_public_default_outgoing_action: ServerDetailsFirewallPublicDefaultOutgoingAction | Unset
        if isinstance(_firewall_public_default_outgoing_action, Unset):
            firewall_public_default_outgoing_action = UNSET
        else:
            firewall_public_default_outgoing_action = ServerDetailsFirewallPublicDefaultOutgoingAction(
                _firewall_public_default_outgoing_action
            )

        host = d.pop("host", UNSET)

        _ip_addresses = d.pop("ip_addresses", UNSET)
        ip_addresses: ServerIpAddresses | Unset
        if isinstance(_ip_addresses, Unset):
            ip_addresses = UNSET
        else:
            ip_addresses = ServerIpAddresses.from_dict(_ip_addresses)

        _labels = d.pop("labels", UNSET)
        labels: ServerLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServerLabels.from_dict(_labels)

        _metadata = d.pop("metadata", UNSET)
        metadata: ServerBooleanYesno | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServerBooleanYesno(_metadata)

        _networking = d.pop("networking", UNSET)
        networking: ServerNetworking | Unset
        if isinstance(_networking, Unset):
            networking = UNSET
        else:
            networking = ServerNetworking.from_dict(_networking)

        _nic_model = d.pop("nic_model", UNSET)
        nic_model: ServerNicModel | Unset
        if isinstance(_nic_model, Unset):
            nic_model = UNSET
        else:
            nic_model = ServerNicModel(_nic_model)

        plan = d.pop("plan", UNSET)

        plan_ipv4_bytes = d.pop("plan_ipv4_bytes", UNSET)

        plan_ipv6_bytes = d.pop("plan_ipv6_bytes", UNSET)

        password = d.pop("password", UNSET)

        progress = d.pop("progress", UNSET)

        _remote_access_enabled = d.pop("remote_access_enabled", UNSET)
        remote_access_enabled: ServerRemoteAccessEnabled | Unset
        if isinstance(_remote_access_enabled, Unset):
            remote_access_enabled = UNSET
        else:
            remote_access_enabled = ServerRemoteAccessEnabled(_remote_access_enabled)

        remote_access_host = d.pop("remote_access_host", UNSET)

        remote_access_password = d.pop("remote_access_password", UNSET)

        remote_access_port = d.pop("remote_access_port", UNSET)

        _remote_access_type = d.pop("remote_access_type", UNSET)
        remote_access_type: ServerRemoteAccessType | Unset
        if isinstance(_remote_access_type, Unset):
            remote_access_type = UNSET
        else:
            remote_access_type = ServerRemoteAccessType(_remote_access_type)

        def _parse_server_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_group = _parse_server_group(d.pop("server_group", UNSET))

        def _parse_simple_backup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        simple_backup = _parse_simple_backup(d.pop("simple_backup", UNSET))

        _storage_devices = d.pop("storage_devices", UNSET)
        storage_devices: ServerStorageDevicesResponse | Unset
        if isinstance(_storage_devices, Unset):
            storage_devices = UNSET
        else:
            storage_devices = ServerStorageDevicesResponse.from_dict(_storage_devices)

        def _parse_tags(data: object) -> list[str] | ServerTagsType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemasserver_tags_type_0 = cast(list[str], data)

                return componentsschemasserver_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasserver_tags_type_1 = ServerTagsType1.from_dict(data)

            return componentsschemasserver_tags_type_1

        tags = _parse_tags(d.pop("tags", UNSET))

        timezone = d.pop("timezone", UNSET)

        username = d.pop("username", UNSET)

        video_model = d.pop("video_model", UNSET)

        server_details = cls(
            core_number=core_number,
            created=created,
            hostname=hostname,
            license_=license_,
            memory_amount=memory_amount,
            state=state,
            title=title,
            uuid=uuid,
            zone=zone,
            boot_order=boot_order,
            devices=devices,
            firewall=firewall,
            firewall_private=firewall_private,
            firewall_private_default_incoming_action=firewall_private_default_incoming_action,
            firewall_private_default_outgoing_action=firewall_private_default_outgoing_action,
            firewall_public_default_incoming_action=firewall_public_default_incoming_action,
            firewall_public_default_outgoing_action=firewall_public_default_outgoing_action,
            host=host,
            ip_addresses=ip_addresses,
            labels=labels,
            metadata=metadata,
            networking=networking,
            nic_model=nic_model,
            plan=plan,
            plan_ipv4_bytes=plan_ipv4_bytes,
            plan_ipv6_bytes=plan_ipv6_bytes,
            password=password,
            progress=progress,
            remote_access_enabled=remote_access_enabled,
            remote_access_host=remote_access_host,
            remote_access_password=remote_access_password,
            remote_access_port=remote_access_port,
            remote_access_type=remote_access_type,
            server_group=server_group,
            simple_backup=simple_backup,
            storage_devices=storage_devices,
            tags=tags,
            timezone=timezone,
            username=username,
            video_model=video_model,
        )

        return server_details
