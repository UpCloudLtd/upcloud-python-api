from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.server_boolean_onoff import ServerBooleanOnoff
from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_nic_model import ServerNicModel
from ..models.server_remote_access_enabled import ServerRemoteAccessEnabled
from ..models.server_remote_access_type import ServerRemoteAccessType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_create_devices import ServerCreateDevices
    from ..models.server_create_networking import ServerCreateNetworking
    from ..models.server_ip_addresses import ServerIpAddresses
    from ..models.server_labels import ServerLabels
    from ..models.server_login_user import ServerLoginUser
    from ..models.server_storage_devices import ServerStorageDevices


T = TypeVar("T", bound="CreateServerServer")


@_attrs_define
class CreateServerServer:
    """
    Attributes:
        hostname (str): Cloud Server hostname Example: example.upcloud.com.
        storage_devices (ServerStorageDevices): Storage devices to create or attach to the Cloud Server Example:
            {'storage_device': [{'action': 'create', 'size': '20', 'title': 'Operating system disk'}]}.
        title (str): Cloud Server title Example: My Server.
        zone (str): Zone identifier
        avoid_host (int | Unset): Encoded Private Cloud host ID
        boot_order (str | Unset): Boot device order (comma-separated list) Example: cdrom,disk.
        core_number (int | Unset): Number of CPU cores Example: 2.
        firewall (ServerBooleanOnoff | Unset): Boolean value represented as on/off Example: on.
        host (int | Unset): Encoded Private Cloud host ID
        ip_addresses (ServerIpAddresses | Unset): IP addresses assigned to the Cloud Server Example: {'ip_address':
            [{'access': 'utility', 'address': '10.0.0.10', 'family': 'IPv4'}]}.
        labels (ServerLabels | Unset): Cloud Server labels Example: {'label': [{'key': 'env', 'value': 'production'}]}.
        login_user (ServerLoginUser | Unset): Login user configuration for Cloud Server creation Example: {'username':
            'upclouduser'}.
        memory_amount (int | Unset): Amount of memory in MB Example: 2048.
        networking (ServerCreateNetworking | Unset): Network interfaces for a new Cloud Server Example: {'interfaces':
            {'interface': [{'ip_addresses': {'ip_address': [{'family': 'IPv4'}]}, 'type': 'public'}]}}.
        nic_model (ServerNicModel | Unset): Network interface card model Example: virtio.
        password_delivery (str | Unset): Password delivery method Example: email.
        plan (str | Unset): Cloud Server plan name Example: 2xCPU-2GB.
        server_group (None | str | Unset): UUID of the server group containing the Cloud Server, or null when the Cloud
            Server is not in a group. Example: 0b3d85b4-b3be-46ca-a1e2-3b5d40d60fb1.
        simple_backup (None | str | Unset): Simple backup start time in UTC and frequency, separated by a comma, or no
            to disable
        metadata (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        devices (ServerCreateDevices | Unset): Passthrough devices requested for a new Cloud Server Example: {'device':
            [{'serial': '1723925007011', 'type': 'gpu'}]}.
        remote_access_enabled (ServerRemoteAccessEnabled | Unset): Whether remote access is enabled Example: yes.
        remote_access_password (str | Unset): Eight-character alphanumeric password used to authenticate remote access
            Example: A1b2C3d4.
        remote_access_type (ServerRemoteAccessType | Unset): Protocol used for remote access Example: vnc.
        timezone (str | Unset): Cloud Server timezone Example: UTC.
        user_data (str | Unset): Setup script body or URL processed during Cloud Server initialization Example:
            #!/bin/sh
            apt-get update.
        video_model (str | Unset): Video adapter model Example: vga.
        vnc_keymap (str | Unset): VNC keyboard layout Example: en-us.
    """

    hostname: str
    storage_devices: ServerStorageDevices
    title: str
    zone: str
    avoid_host: int | Unset = UNSET
    boot_order: str | Unset = UNSET
    core_number: int | Unset = UNSET
    firewall: ServerBooleanOnoff | Unset = UNSET
    host: int | Unset = UNSET
    ip_addresses: ServerIpAddresses | Unset = UNSET
    labels: ServerLabels | Unset = UNSET
    login_user: ServerLoginUser | Unset = UNSET
    memory_amount: int | Unset = UNSET
    networking: ServerCreateNetworking | Unset = UNSET
    nic_model: ServerNicModel | Unset = UNSET
    password_delivery: str | Unset = UNSET
    plan: str | Unset = UNSET
    server_group: None | str | Unset = UNSET
    simple_backup: None | str | Unset = UNSET
    metadata: ServerBooleanYesno | Unset = UNSET
    devices: ServerCreateDevices | Unset = UNSET
    remote_access_enabled: ServerRemoteAccessEnabled | Unset = UNSET
    remote_access_password: str | Unset = UNSET
    remote_access_type: ServerRemoteAccessType | Unset = UNSET
    timezone: str | Unset = UNSET
    user_data: str | Unset = UNSET
    video_model: str | Unset = UNSET
    vnc_keymap: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        storage_devices = self.storage_devices.to_dict()

        title = self.title

        zone = self.zone

        avoid_host = self.avoid_host

        boot_order = self.boot_order

        core_number = self.core_number

        firewall: str | Unset = UNSET
        if not isinstance(self.firewall, Unset):
            firewall = self.firewall.value

        host = self.host

        ip_addresses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        login_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login_user, Unset):
            login_user = self.login_user.to_dict()

        memory_amount = self.memory_amount

        networking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.networking, Unset):
            networking = self.networking.to_dict()

        nic_model: str | Unset = UNSET
        if not isinstance(self.nic_model, Unset):
            nic_model = self.nic_model.value

        password_delivery = self.password_delivery

        plan = self.plan

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

        metadata: str | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.value

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        remote_access_enabled: str | Unset = UNSET
        if not isinstance(self.remote_access_enabled, Unset):
            remote_access_enabled = self.remote_access_enabled.value

        remote_access_password = self.remote_access_password

        remote_access_type: str | Unset = UNSET
        if not isinstance(self.remote_access_type, Unset):
            remote_access_type = self.remote_access_type.value

        timezone = self.timezone

        user_data = self.user_data

        video_model = self.video_model

        vnc_keymap = self.vnc_keymap

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hostname": hostname,
                "storage_devices": storage_devices,
                "title": title,
                "zone": zone,
            }
        )
        if avoid_host is not UNSET:
            field_dict["avoid_host"] = avoid_host
        if boot_order is not UNSET:
            field_dict["boot_order"] = boot_order
        if core_number is not UNSET:
            field_dict["core_number"] = core_number
        if firewall is not UNSET:
            field_dict["firewall"] = firewall
        if host is not UNSET:
            field_dict["host"] = host
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if labels is not UNSET:
            field_dict["labels"] = labels
        if login_user is not UNSET:
            field_dict["login_user"] = login_user
        if memory_amount is not UNSET:
            field_dict["memory_amount"] = memory_amount
        if networking is not UNSET:
            field_dict["networking"] = networking
        if nic_model is not UNSET:
            field_dict["nic_model"] = nic_model
        if password_delivery is not UNSET:
            field_dict["password_delivery"] = password_delivery
        if plan is not UNSET:
            field_dict["plan"] = plan
        if server_group is not UNSET:
            field_dict["server_group"] = server_group
        if simple_backup is not UNSET:
            field_dict["simple_backup"] = simple_backup
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if devices is not UNSET:
            field_dict["devices"] = devices
        if remote_access_enabled is not UNSET:
            field_dict["remote_access_enabled"] = remote_access_enabled
        if remote_access_password is not UNSET:
            field_dict["remote_access_password"] = remote_access_password
        if remote_access_type is not UNSET:
            field_dict["remote_access_type"] = remote_access_type
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if video_model is not UNSET:
            field_dict["video_model"] = video_model
        if vnc_keymap is not UNSET:
            field_dict["vnc_keymap"] = vnc_keymap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_create_devices import ServerCreateDevices  # noqa: PLC0415
        from ..models.server_create_networking import ServerCreateNetworking  # noqa: PLC0415
        from ..models.server_ip_addresses import ServerIpAddresses  # noqa: PLC0415
        from ..models.server_labels import ServerLabels  # noqa: PLC0415
        from ..models.server_login_user import ServerLoginUser  # noqa: PLC0415
        from ..models.server_storage_devices import ServerStorageDevices  # noqa: PLC0415

        d = dict(src_dict)
        hostname = d.pop("hostname")

        storage_devices = ServerStorageDevices.from_dict(d.pop("storage_devices"))

        title = d.pop("title")

        zone = d.pop("zone")

        avoid_host = d.pop("avoid_host", UNSET)

        boot_order = d.pop("boot_order", UNSET)

        core_number = d.pop("core_number", UNSET)

        _firewall = d.pop("firewall", UNSET)
        firewall: ServerBooleanOnoff | Unset
        if isinstance(_firewall, Unset):
            firewall = UNSET
        else:
            firewall = ServerBooleanOnoff(_firewall)

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

        _login_user = d.pop("login_user", UNSET)
        login_user: ServerLoginUser | Unset
        if isinstance(_login_user, Unset):
            login_user = UNSET
        else:
            login_user = ServerLoginUser.from_dict(_login_user)

        memory_amount = d.pop("memory_amount", UNSET)

        _networking = d.pop("networking", UNSET)
        networking: ServerCreateNetworking | Unset
        if isinstance(_networking, Unset):
            networking = UNSET
        else:
            networking = ServerCreateNetworking.from_dict(_networking)

        _nic_model = d.pop("nic_model", UNSET)
        nic_model: ServerNicModel | Unset
        if isinstance(_nic_model, Unset):
            nic_model = UNSET
        else:
            nic_model = ServerNicModel(_nic_model)

        password_delivery = d.pop("password_delivery", UNSET)

        plan = d.pop("plan", UNSET)

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

        _metadata = d.pop("metadata", UNSET)
        metadata: ServerBooleanYesno | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServerBooleanYesno(_metadata)

        _devices = d.pop("devices", UNSET)
        devices: ServerCreateDevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = ServerCreateDevices.from_dict(_devices)

        _remote_access_enabled = d.pop("remote_access_enabled", UNSET)
        remote_access_enabled: ServerRemoteAccessEnabled | Unset
        if isinstance(_remote_access_enabled, Unset):
            remote_access_enabled = UNSET
        else:
            remote_access_enabled = ServerRemoteAccessEnabled(_remote_access_enabled)

        remote_access_password = d.pop("remote_access_password", UNSET)

        _remote_access_type = d.pop("remote_access_type", UNSET)
        remote_access_type: ServerRemoteAccessType | Unset
        if isinstance(_remote_access_type, Unset):
            remote_access_type = UNSET
        else:
            remote_access_type = ServerRemoteAccessType(_remote_access_type)

        timezone = d.pop("timezone", UNSET)

        user_data = d.pop("user_data", UNSET)

        video_model = d.pop("video_model", UNSET)

        vnc_keymap = d.pop("vnc_keymap", UNSET)

        create_server_server = cls(
            hostname=hostname,
            storage_devices=storage_devices,
            title=title,
            zone=zone,
            avoid_host=avoid_host,
            boot_order=boot_order,
            core_number=core_number,
            firewall=firewall,
            host=host,
            ip_addresses=ip_addresses,
            labels=labels,
            login_user=login_user,
            memory_amount=memory_amount,
            networking=networking,
            nic_model=nic_model,
            password_delivery=password_delivery,
            plan=plan,
            server_group=server_group,
            simple_backup=simple_backup,
            metadata=metadata,
            devices=devices,
            remote_access_enabled=remote_access_enabled,
            remote_access_password=remote_access_password,
            remote_access_type=remote_access_type,
            timezone=timezone,
            user_data=user_data,
            video_model=video_model,
            vnc_keymap=vnc_keymap,
        )

        return create_server_server
