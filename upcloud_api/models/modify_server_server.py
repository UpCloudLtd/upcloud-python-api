from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.modify_server_server_firewall_private_default_incoming_action import (
    ModifyServerServerFirewallPrivateDefaultIncomingAction,
)
from ..models.modify_server_server_firewall_private_default_outgoing_action import (
    ModifyServerServerFirewallPrivateDefaultOutgoingAction,
)
from ..models.modify_server_server_firewall_public_default_incoming_action import (
    ModifyServerServerFirewallPublicDefaultIncomingAction,
)
from ..models.modify_server_server_firewall_public_default_outgoing_action import (
    ModifyServerServerFirewallPublicDefaultOutgoingAction,
)
from ..models.server_boolean_onoff import ServerBooleanOnoff
from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_nic_model import ServerNicModel
from ..models.server_remote_access_enabled import ServerRemoteAccessEnabled
from ..models.server_remote_access_type import ServerRemoteAccessType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_labels import ServerLabels


T = TypeVar("T", bound="ModifyServerServer")


@_attrs_define
class ModifyServerServer:
    """
    Attributes:
        boot_order (str | Unset): Boot device order (comma-separated list) Example: cdrom,disk.
        core_number (int | Unset): Number of CPU cores Example: 2.
        firewall (ServerBooleanOnoff | Unset): Boolean value represented as on/off Example: on.
        firewall_private (ServerBooleanOnoff | Unset): Boolean value represented as on/off Example: on.
        firewall_private_default_incoming_action (ModifyServerServerFirewallPrivateDefaultIncomingAction | Unset):
        firewall_private_default_outgoing_action (ModifyServerServerFirewallPrivateDefaultOutgoingAction | Unset):
        firewall_public_default_incoming_action (ModifyServerServerFirewallPublicDefaultIncomingAction | Unset):
        firewall_public_default_outgoing_action (ModifyServerServerFirewallPublicDefaultOutgoingAction | Unset):
        hostname (str | Unset): Cloud Server hostname Example: example.upcloud.com.
        labels (ServerLabels | Unset): Cloud Server labels Example: {'label': [{'key': 'env', 'value': 'production'}]}.
        memory_amount (int | Unset): Amount of memory in MB Example: 2048.
        metadata (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        nic_model (ServerNicModel | Unset): Network interface card model Example: virtio.
        plan (str | Unset): Cloud Server plan name Example: 2xCPU-2GB.
        remote_access_enabled (ServerRemoteAccessEnabled | Unset): Whether remote access is enabled Example: yes.
        remote_access_password (str | Unset): Eight-character alphanumeric password used to authenticate remote access
            Example: A1b2C3d4.
        remote_access_type (ServerRemoteAccessType | Unset): Protocol used for remote access Example: vnc.
        simple_backup (None | str | Unset): Simple backup start time in UTC and frequency, separated by a comma, or no
            to disable
        timezone (str | Unset): Cloud Server timezone Example: UTC.
        title (str | Unset): Cloud Server title Example: My Server.
        video_model (str | Unset): Video adapter model Example: vga.
        vnc_keymap (str | Unset): VNC keyboard layout Example: en-us.
    """

    boot_order: str | Unset = UNSET
    core_number: int | Unset = UNSET
    firewall: ServerBooleanOnoff | Unset = UNSET
    firewall_private: ServerBooleanOnoff | Unset = UNSET
    firewall_private_default_incoming_action: ModifyServerServerFirewallPrivateDefaultIncomingAction | Unset = UNSET
    firewall_private_default_outgoing_action: ModifyServerServerFirewallPrivateDefaultOutgoingAction | Unset = UNSET
    firewall_public_default_incoming_action: ModifyServerServerFirewallPublicDefaultIncomingAction | Unset = UNSET
    firewall_public_default_outgoing_action: ModifyServerServerFirewallPublicDefaultOutgoingAction | Unset = UNSET
    hostname: str | Unset = UNSET
    labels: ServerLabels | Unset = UNSET
    memory_amount: int | Unset = UNSET
    metadata: ServerBooleanYesno | Unset = UNSET
    nic_model: ServerNicModel | Unset = UNSET
    plan: str | Unset = UNSET
    remote_access_enabled: ServerRemoteAccessEnabled | Unset = UNSET
    remote_access_password: str | Unset = UNSET
    remote_access_type: ServerRemoteAccessType | Unset = UNSET
    simple_backup: None | str | Unset = UNSET
    timezone: str | Unset = UNSET
    title: str | Unset = UNSET
    video_model: str | Unset = UNSET
    vnc_keymap: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        boot_order = self.boot_order

        core_number = self.core_number

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

        hostname = self.hostname

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        memory_amount = self.memory_amount

        metadata: str | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.value

        nic_model: str | Unset = UNSET
        if not isinstance(self.nic_model, Unset):
            nic_model = self.nic_model.value

        plan = self.plan

        remote_access_enabled: str | Unset = UNSET
        if not isinstance(self.remote_access_enabled, Unset):
            remote_access_enabled = self.remote_access_enabled.value

        remote_access_password = self.remote_access_password

        remote_access_type: str | Unset = UNSET
        if not isinstance(self.remote_access_type, Unset):
            remote_access_type = self.remote_access_type.value

        simple_backup: None | str | Unset
        if isinstance(self.simple_backup, Unset):
            simple_backup = UNSET
        else:
            simple_backup = self.simple_backup

        timezone = self.timezone

        title = self.title

        video_model = self.video_model

        vnc_keymap = self.vnc_keymap

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if boot_order is not UNSET:
            field_dict["boot_order"] = boot_order
        if core_number is not UNSET:
            field_dict["core_number"] = core_number
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
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if labels is not UNSET:
            field_dict["labels"] = labels
        if memory_amount is not UNSET:
            field_dict["memory_amount"] = memory_amount
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if nic_model is not UNSET:
            field_dict["nic_model"] = nic_model
        if plan is not UNSET:
            field_dict["plan"] = plan
        if remote_access_enabled is not UNSET:
            field_dict["remote_access_enabled"] = remote_access_enabled
        if remote_access_password is not UNSET:
            field_dict["remote_access_password"] = remote_access_password
        if remote_access_type is not UNSET:
            field_dict["remote_access_type"] = remote_access_type
        if simple_backup is not UNSET:
            field_dict["simple_backup"] = simple_backup
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if title is not UNSET:
            field_dict["title"] = title
        if video_model is not UNSET:
            field_dict["video_model"] = video_model
        if vnc_keymap is not UNSET:
            field_dict["vnc_keymap"] = vnc_keymap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_labels import ServerLabels  # noqa: PLC0415

        d = dict(src_dict)
        boot_order = d.pop("boot_order", UNSET)

        core_number = d.pop("core_number", UNSET)

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
        firewall_private_default_incoming_action: ModifyServerServerFirewallPrivateDefaultIncomingAction | Unset
        if isinstance(_firewall_private_default_incoming_action, Unset):
            firewall_private_default_incoming_action = UNSET
        else:
            firewall_private_default_incoming_action = ModifyServerServerFirewallPrivateDefaultIncomingAction(
                _firewall_private_default_incoming_action
            )

        _firewall_private_default_outgoing_action = d.pop("firewall_private_default_outgoing_action", UNSET)
        firewall_private_default_outgoing_action: ModifyServerServerFirewallPrivateDefaultOutgoingAction | Unset
        if isinstance(_firewall_private_default_outgoing_action, Unset):
            firewall_private_default_outgoing_action = UNSET
        else:
            firewall_private_default_outgoing_action = ModifyServerServerFirewallPrivateDefaultOutgoingAction(
                _firewall_private_default_outgoing_action
            )

        _firewall_public_default_incoming_action = d.pop("firewall_public_default_incoming_action", UNSET)
        firewall_public_default_incoming_action: ModifyServerServerFirewallPublicDefaultIncomingAction | Unset
        if isinstance(_firewall_public_default_incoming_action, Unset):
            firewall_public_default_incoming_action = UNSET
        else:
            firewall_public_default_incoming_action = ModifyServerServerFirewallPublicDefaultIncomingAction(
                _firewall_public_default_incoming_action
            )

        _firewall_public_default_outgoing_action = d.pop("firewall_public_default_outgoing_action", UNSET)
        firewall_public_default_outgoing_action: ModifyServerServerFirewallPublicDefaultOutgoingAction | Unset
        if isinstance(_firewall_public_default_outgoing_action, Unset):
            firewall_public_default_outgoing_action = UNSET
        else:
            firewall_public_default_outgoing_action = ModifyServerServerFirewallPublicDefaultOutgoingAction(
                _firewall_public_default_outgoing_action
            )

        hostname = d.pop("hostname", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: ServerLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServerLabels.from_dict(_labels)

        memory_amount = d.pop("memory_amount", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ServerBooleanYesno | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServerBooleanYesno(_metadata)

        _nic_model = d.pop("nic_model", UNSET)
        nic_model: ServerNicModel | Unset
        if isinstance(_nic_model, Unset):
            nic_model = UNSET
        else:
            nic_model = ServerNicModel(_nic_model)

        plan = d.pop("plan", UNSET)

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

        def _parse_simple_backup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        simple_backup = _parse_simple_backup(d.pop("simple_backup", UNSET))

        timezone = d.pop("timezone", UNSET)

        title = d.pop("title", UNSET)

        video_model = d.pop("video_model", UNSET)

        vnc_keymap = d.pop("vnc_keymap", UNSET)

        modify_server_server = cls(
            boot_order=boot_order,
            core_number=core_number,
            firewall=firewall,
            firewall_private=firewall_private,
            firewall_private_default_incoming_action=firewall_private_default_incoming_action,
            firewall_private_default_outgoing_action=firewall_private_default_outgoing_action,
            firewall_public_default_incoming_action=firewall_public_default_incoming_action,
            firewall_public_default_outgoing_action=firewall_public_default_outgoing_action,
            hostname=hostname,
            labels=labels,
            memory_amount=memory_amount,
            metadata=metadata,
            nic_model=nic_model,
            plan=plan,
            remote_access_enabled=remote_access_enabled,
            remote_access_password=remote_access_password,
            remote_access_type=remote_access_type,
            simple_backup=simple_backup,
            timezone=timezone,
            title=title,
            video_model=video_model,
            vnc_keymap=vnc_keymap,
        )

        return modify_server_server
