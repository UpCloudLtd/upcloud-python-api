from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_state import ServerState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_in_get_server_list_labels import ServerInGetServerListLabels
    from ..models.server_tags_type_1 import ServerTagsType1


T = TypeVar("T", bound="ServerInGetServerList")


@_attrs_define
class ServerInGetServerList:
    """Schema for a Cloud Server item returned in Cloud Server list responses.

    Example:
        {'core_number': '2', 'created': 1705320000, 'hostname': 'web-1.example.com', 'license': '0', 'memory_amount':
            '2048', 'labels': {'label': [{'key': 'env', 'value': 'production'}]}, 'plan': '2xCPU-2GB', 'plan_ipv4_bytes':
            '34253332', 'plan_ipv6_bytes': '0', 'simple_backup': '0100,dailies', 'state': 'started', 'tags': {'tag':
            ['production', 'web']}, 'title': 'Production web server', 'uuid': '007bf7bd-e3cf-4a10-bf01-4251dc7f3b65',
            'zone': 'fi-hel1'}

    Attributes:
        created (int): Creation timestamp (Unix epoch time) Example: 1705320000.
        core_number (str): Number of CPU cores allocated to the Cloud Server.
        hostname (str): Hostname configured for the Cloud Server.
        license_ (str): Hourly operating system license charge in credits.
        memory_amount (str): Amount of memory allocated to the Cloud Server, in MiB.
        state (ServerState): Current state of the Cloud Server Example: started.
        title (str): Display title of the Cloud Server.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        zone (str): Zone identifier
        host (int | Unset): Encoded Private Cloud host ID
        labels (ServerInGetServerListLabels | Unset): Labels assigned to the Cloud Server.
        plan (str | Unset): Server plan identifier
        plan_ipv4_bytes (str | Unset): Public IPv4 outbound traffic used during the current billing month, in bytes.
        plan_ipv6_bytes (str | Unset): Public IPv6 outbound traffic used during the current billing month, in bytes.
        progress (str | Unset): Progress percentage for an operation that places the Cloud Server in maintenance state.
        simple_backup (None | str | Unset): Simple backup start time in UTC and frequency, separated by a comma, or no
            to disable
        tags (list[str] | ServerTagsType1 | Unset): tags can be an empty array or an object with a tag array Example:
            {'tag': []}.
        server_group (None | str | Unset): UUID of the server group containing the Cloud Server, or null when the Cloud
            Server is not in a group. Example: 0b3d85b4-b3be-46ca-a1e2-3b5d40d60fb1.
    """

    created: int
    core_number: str
    hostname: str
    license_: str
    memory_amount: str
    state: ServerState
    title: str
    uuid: UUID
    zone: str
    host: int | Unset = UNSET
    labels: ServerInGetServerListLabels | Unset = UNSET
    plan: str | Unset = UNSET
    plan_ipv4_bytes: str | Unset = UNSET
    plan_ipv6_bytes: str | Unset = UNSET
    progress: str | Unset = UNSET
    simple_backup: None | str | Unset = UNSET
    tags: list[str] | ServerTagsType1 | Unset = UNSET
    server_group: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        core_number = self.core_number

        hostname = self.hostname

        license_ = self.license_

        memory_amount = self.memory_amount

        state = self.state.value

        title = self.title

        uuid = str(self.uuid)

        zone = self.zone

        host = self.host

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        plan = self.plan

        plan_ipv4_bytes = self.plan_ipv4_bytes

        plan_ipv6_bytes = self.plan_ipv6_bytes

        progress = self.progress

        simple_backup: None | str | Unset
        if isinstance(self.simple_backup, Unset):
            simple_backup = UNSET
        else:
            simple_backup = self.simple_backup

        tags: dict[str, Any] | list[str] | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags.to_dict()

        server_group: None | str | Unset
        if isinstance(self.server_group, Unset):
            server_group = UNSET
        else:
            server_group = self.server_group

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created": created,
                "core_number": core_number,
                "hostname": hostname,
                "license": license_,
                "memory_amount": memory_amount,
                "state": state,
                "title": title,
                "uuid": uuid,
                "zone": zone,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if labels is not UNSET:
            field_dict["labels"] = labels
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_ipv4_bytes is not UNSET:
            field_dict["plan_ipv4_bytes"] = plan_ipv4_bytes
        if plan_ipv6_bytes is not UNSET:
            field_dict["plan_ipv6_bytes"] = plan_ipv6_bytes
        if progress is not UNSET:
            field_dict["progress"] = progress
        if simple_backup is not UNSET:
            field_dict["simple_backup"] = simple_backup
        if tags is not UNSET:
            field_dict["tags"] = tags
        if server_group is not UNSET:
            field_dict["server_group"] = server_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_in_get_server_list_labels import ServerInGetServerListLabels  # noqa: PLC0415
        from ..models.server_tags_type_1 import ServerTagsType1  # noqa: PLC0415

        d = dict(src_dict)
        created = d.pop("created")

        core_number = d.pop("core_number")

        hostname = d.pop("hostname")

        license_ = d.pop("license")

        memory_amount = d.pop("memory_amount")

        state = ServerState(d.pop("state"))

        title = d.pop("title")

        uuid = UUID(d.pop("uuid"))

        zone = d.pop("zone")

        host = d.pop("host", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: ServerInGetServerListLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServerInGetServerListLabels.from_dict(_labels)

        plan = d.pop("plan", UNSET)

        plan_ipv4_bytes = d.pop("plan_ipv4_bytes", UNSET)

        plan_ipv6_bytes = d.pop("plan_ipv6_bytes", UNSET)

        progress = d.pop("progress", UNSET)

        def _parse_simple_backup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        simple_backup = _parse_simple_backup(d.pop("simple_backup", UNSET))

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

        def _parse_server_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_group = _parse_server_group(d.pop("server_group", UNSET))

        server_in_get_server_list = cls(
            created=created,
            core_number=core_number,
            hostname=hostname,
            license_=license_,
            memory_amount=memory_amount,
            state=state,
            title=title,
            uuid=uuid,
            zone=zone,
            host=host,
            labels=labels,
            plan=plan,
            plan_ipv4_bytes=plan_ipv4_bytes,
            plan_ipv6_bytes=plan_ipv6_bytes,
            progress=progress,
            simple_backup=simple_backup,
            tags=tags,
            server_group=server_group,
        )

        return server_in_get_server_list
