from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_acl_response import DatabaseAclResponse
    from ..models.database_backup_response import DatabaseBackupResponse
    from ..models.database_connection_pool_response import DatabaseConnectionPoolResponse
    from ..models.database_label_information_response import DatabaseLabelInformationResponse
    from ..models.database_maintenance_window_response import DatabaseMaintenanceWindowResponse
    from ..models.database_network_information_details_response import DatabaseNetworkInformationDetailsResponse
    from ..models.database_node_state_response import DatabaseNodeStateResponse
    from ..models.database_plan_components_response import DatabasePlanComponentsResponse
    from ..models.database_service_component_response import DatabaseServiceComponentResponse
    from ..models.database_service_information_response_metadata import DatabaseServiceInformationResponseMetadata
    from ..models.database_service_information_response_properties import DatabaseServiceInformationResponseProperties
    from ..models.database_service_information_response_service_uri_params import (
        DatabaseServiceInformationResponseServiceUriParams,
    )
    from ..models.database_service_information_response_state_error import DatabaseServiceInformationResponseStateError
    from ..models.database_service_integration_response import DatabaseServiceIntegrationResponse
    from ..models.database_user_response import DatabaseUserResponse
    from ..models.logical_database_response import LogicalDatabaseResponse


T = TypeVar("T", bound="DatabaseServiceInformationResponse")


@_attrs_define
class DatabaseServiceInformationResponse:
    """Schema for service information response.

    Attributes:
        uuid (UUID | Unset): The unique identifier for the service.
        zone (str | Unset): The zone where the service is hosted.
        name (str | Unset): The name of the service.
        title (str | Unset): The title of the service.
        type_ (str | Unset): The type of the service.
        plan (str | Unset): The plan of the service. For componentised (rdb.*) plans this is the effective plan name:
            the storage segment shows the total storage per node the service is configured with, and the same name is
            accepted back on create, modify and clone.
        plan_components (DatabasePlanComponentsResponse | Unset): Structured breakdown of a service plan into compute,
            storage and backups components. Sizes are expressed in GB to match plan naming; the classic MB/MiB fields on the
            plan object are unchanged.
        additional_disk_space_gib (int | Unset): The additional disk space allocated to the service in GiB. Always 0 for
            componentised (rdb.*) plans, where storage is expressed only as the total in the plan name and in
            plan_components.
        state (str | Unset): The current state of the service.
        state_error (DatabaseServiceInformationResponseStateError | Unset): A map of errors related to the service
            state.
        powered (bool | Unset): Indicates whether the service is powered on.
        termination_protection (bool | Unset): Indicates whether termination protection is enabled for the service.
        node_count (int | Unset): The number of nodes in the service.
        create_time (datetime.datetime | Unset): The time when the service was created.
        update_time (datetime.datetime | Unset): The time when the service was last updated.
        service_uri (str | Unset): The URI for accessing the service.
        service_uri_params (DatabaseServiceInformationResponseServiceUriParams | Unset): A map of connection parameters
            for the service.
        maintenance (DatabaseMaintenanceWindowResponse | Unset): Schema for a maintenance window response.
        metadata (DatabaseServiceInformationResponseMetadata | Unset): A map of metadata key-value pairs for the
            service.
        properties (DatabaseServiceInformationResponseProperties | Unset): A map of additional properties for the
            service.
        networks (list[DatabaseNetworkInformationDetailsResponse] | Unset): List of network information details
            associated with the service.
        node_states (list[DatabaseNodeStateResponse] | Unset): The states of individual nodes in the service.
        labels (list[DatabaseLabelInformationResponse] | Unset): List of label information associated with the service.
        backups (list[DatabaseBackupResponse] | Unset): List of backups associated with the service.
        components (list[DatabaseServiceComponentResponse] | Unset): List of service components associated with the
            service.
        connection_pools (list[DatabaseConnectionPoolResponse] | Unset): List of connection pools associated with the
            service.
        users (list[DatabaseUserResponse] | Unset): List of users associated with the service.
        databases (list[LogicalDatabaseResponse] | Unset): A list of logical databases.
        acls (list[DatabaseAclResponse] | Unset): List of ACLs associated with the service.
        service_integrations (list[DatabaseServiceIntegrationResponse] | Unset): List of service integrations associated
            with the service.
    """

    uuid: UUID | Unset = UNSET
    zone: str | Unset = UNSET
    name: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    plan: str | Unset = UNSET
    plan_components: DatabasePlanComponentsResponse | Unset = UNSET
    additional_disk_space_gib: int | Unset = UNSET
    state: str | Unset = UNSET
    state_error: DatabaseServiceInformationResponseStateError | Unset = UNSET
    powered: bool | Unset = UNSET
    termination_protection: bool | Unset = UNSET
    node_count: int | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    service_uri: str | Unset = UNSET
    service_uri_params: DatabaseServiceInformationResponseServiceUriParams | Unset = UNSET
    maintenance: DatabaseMaintenanceWindowResponse | Unset = UNSET
    metadata: DatabaseServiceInformationResponseMetadata | Unset = UNSET
    properties: DatabaseServiceInformationResponseProperties | Unset = UNSET
    networks: list[DatabaseNetworkInformationDetailsResponse] | Unset = UNSET
    node_states: list[DatabaseNodeStateResponse] | Unset = UNSET
    labels: list[DatabaseLabelInformationResponse] | Unset = UNSET
    backups: list[DatabaseBackupResponse] | Unset = UNSET
    components: list[DatabaseServiceComponentResponse] | Unset = UNSET
    connection_pools: list[DatabaseConnectionPoolResponse] | Unset = UNSET
    users: list[DatabaseUserResponse] | Unset = UNSET
    databases: list[LogicalDatabaseResponse] | Unset = UNSET
    acls: list[DatabaseAclResponse] | Unset = UNSET
    service_integrations: list[DatabaseServiceIntegrationResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        zone = self.zone

        name = self.name

        title = self.title

        type_ = self.type_

        plan = self.plan

        plan_components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan_components, Unset):
            plan_components = self.plan_components.to_dict()

        additional_disk_space_gib = self.additional_disk_space_gib

        state = self.state

        state_error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state_error, Unset):
            state_error = self.state_error.to_dict()

        powered = self.powered

        termination_protection = self.termination_protection

        node_count = self.node_count

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        service_uri = self.service_uri

        service_uri_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_uri_params, Unset):
            service_uri_params = self.service_uri_params.to_dict()

        maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        node_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node_states, Unset):
            node_states = []
            for node_states_item_data in self.node_states:
                node_states_item = node_states_item_data.to_dict()
                node_states.append(node_states_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        backups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backups, Unset):
            backups = []
            for backups_item_data in self.backups:
                backups_item = backups_item_data.to_dict()
                backups.append(backups_item)

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        connection_pools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connection_pools, Unset):
            connection_pools = []
            for connection_pools_item_data in self.connection_pools:
                connection_pools_item = connection_pools_item_data.to_dict()
                connection_pools.append(connection_pools_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        databases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for componentsschemas_logical_databases_response_item_data in self.databases:
                componentsschemas_logical_databases_response_item = (
                    componentsschemas_logical_databases_response_item_data.to_dict()
                )
                databases.append(componentsschemas_logical_databases_response_item)

        acls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acls, Unset):
            acls = []
            for acls_item_data in self.acls:
                acls_item = acls_item_data.to_dict()
                acls.append(acls_item)

        service_integrations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_integrations, Unset):
            service_integrations = []
            for service_integrations_item_data in self.service_integrations:
                service_integrations_item = service_integrations_item_data.to_dict()
                service_integrations.append(service_integrations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if zone is not UNSET:
            field_dict["zone"] = zone
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_components is not UNSET:
            field_dict["plan_components"] = plan_components
        if additional_disk_space_gib is not UNSET:
            field_dict["additional_disk_space_gib"] = additional_disk_space_gib
        if state is not UNSET:
            field_dict["state"] = state
        if state_error is not UNSET:
            field_dict["state_error"] = state_error
        if powered is not UNSET:
            field_dict["powered"] = powered
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if service_uri is not UNSET:
            field_dict["service_uri"] = service_uri
        if service_uri_params is not UNSET:
            field_dict["service_uri_params"] = service_uri_params
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if properties is not UNSET:
            field_dict["properties"] = properties
        if networks is not UNSET:
            field_dict["networks"] = networks
        if node_states is not UNSET:
            field_dict["node_states"] = node_states
        if labels is not UNSET:
            field_dict["labels"] = labels
        if backups is not UNSET:
            field_dict["backups"] = backups
        if components is not UNSET:
            field_dict["components"] = components
        if connection_pools is not UNSET:
            field_dict["connection_pools"] = connection_pools
        if users is not UNSET:
            field_dict["users"] = users
        if databases is not UNSET:
            field_dict["databases"] = databases
        if acls is not UNSET:
            field_dict["acls"] = acls
        if service_integrations is not UNSET:
            field_dict["service_integrations"] = service_integrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_acl_response import DatabaseAclResponse  # noqa: PLC0415
        from ..models.database_backup_response import DatabaseBackupResponse  # noqa: PLC0415
        from ..models.database_connection_pool_response import DatabaseConnectionPoolResponse  # noqa: PLC0415
        from ..models.database_label_information_response import DatabaseLabelInformationResponse  # noqa: PLC0415
        from ..models.database_maintenance_window_response import DatabaseMaintenanceWindowResponse  # noqa: PLC0415
        from ..models.database_network_information_details_response import (
            DatabaseNetworkInformationDetailsResponse,  # noqa: PLC0415
        )
        from ..models.database_node_state_response import DatabaseNodeStateResponse  # noqa: PLC0415
        from ..models.database_plan_components_response import DatabasePlanComponentsResponse  # noqa: PLC0415
        from ..models.database_service_component_response import DatabaseServiceComponentResponse  # noqa: PLC0415
        from ..models.database_service_information_response_metadata import (
            DatabaseServiceInformationResponseMetadata,  # noqa: PLC0415
        )
        from ..models.database_service_information_response_properties import (
            DatabaseServiceInformationResponseProperties,  # noqa: PLC0415
        )
        from ..models.database_service_information_response_service_uri_params import (
            DatabaseServiceInformationResponseServiceUriParams,  # noqa: PLC0415
        )
        from ..models.database_service_information_response_state_error import (
            DatabaseServiceInformationResponseStateError,  # noqa: PLC0415
        )
        from ..models.database_service_integration_response import DatabaseServiceIntegrationResponse  # noqa: PLC0415
        from ..models.database_user_response import DatabaseUserResponse  # noqa: PLC0415
        from ..models.logical_database_response import LogicalDatabaseResponse  # noqa: PLC0415

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        zone = d.pop("zone", UNSET)

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        plan = d.pop("plan", UNSET)

        _plan_components = d.pop("plan_components", UNSET)
        plan_components: DatabasePlanComponentsResponse | Unset
        if isinstance(_plan_components, Unset):
            plan_components = UNSET
        else:
            plan_components = DatabasePlanComponentsResponse.from_dict(_plan_components)

        additional_disk_space_gib = d.pop("additional_disk_space_gib", UNSET)

        state = d.pop("state", UNSET)

        _state_error = d.pop("state_error", UNSET)
        state_error: DatabaseServiceInformationResponseStateError | Unset
        if isinstance(_state_error, Unset):
            state_error = UNSET
        else:
            state_error = DatabaseServiceInformationResponseStateError.from_dict(_state_error)

        powered = d.pop("powered", UNSET)

        termination_protection = d.pop("termination_protection", UNSET)

        node_count = d.pop("node_count", UNSET)

        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("update_time", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        service_uri = d.pop("service_uri", UNSET)

        _service_uri_params = d.pop("service_uri_params", UNSET)
        service_uri_params: DatabaseServiceInformationResponseServiceUriParams | Unset
        if isinstance(_service_uri_params, Unset):
            service_uri_params = UNSET
        else:
            service_uri_params = DatabaseServiceInformationResponseServiceUriParams.from_dict(_service_uri_params)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: DatabaseMaintenanceWindowResponse | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = DatabaseMaintenanceWindowResponse.from_dict(_maintenance)

        _metadata = d.pop("metadata", UNSET)
        metadata: DatabaseServiceInformationResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DatabaseServiceInformationResponseMetadata.from_dict(_metadata)

        _properties = d.pop("properties", UNSET)
        properties: DatabaseServiceInformationResponseProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = DatabaseServiceInformationResponseProperties.from_dict(_properties)

        _networks = d.pop("networks", UNSET)
        networks: list[DatabaseNetworkInformationDetailsResponse] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = DatabaseNetworkInformationDetailsResponse.from_dict(networks_item_data)

                networks.append(networks_item)

        _node_states = d.pop("node_states", UNSET)
        node_states: list[DatabaseNodeStateResponse] | Unset = UNSET
        if _node_states is not UNSET:
            node_states = []
            for node_states_item_data in _node_states:
                node_states_item = DatabaseNodeStateResponse.from_dict(node_states_item_data)

                node_states.append(node_states_item)

        _labels = d.pop("labels", UNSET)
        labels: list[DatabaseLabelInformationResponse] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = DatabaseLabelInformationResponse.from_dict(labels_item_data)

                labels.append(labels_item)

        _backups = d.pop("backups", UNSET)
        backups: list[DatabaseBackupResponse] | Unset = UNSET
        if _backups is not UNSET:
            backups = []
            for backups_item_data in _backups:
                backups_item = DatabaseBackupResponse.from_dict(backups_item_data)

                backups.append(backups_item)

        _components = d.pop("components", UNSET)
        components: list[DatabaseServiceComponentResponse] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = DatabaseServiceComponentResponse.from_dict(components_item_data)

                components.append(components_item)

        _connection_pools = d.pop("connection_pools", UNSET)
        connection_pools: list[DatabaseConnectionPoolResponse] | Unset = UNSET
        if _connection_pools is not UNSET:
            connection_pools = []
            for connection_pools_item_data in _connection_pools:
                connection_pools_item = DatabaseConnectionPoolResponse.from_dict(connection_pools_item_data)

                connection_pools.append(connection_pools_item)

        _users = d.pop("users", UNSET)
        users: list[DatabaseUserResponse] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = DatabaseUserResponse.from_dict(users_item_data)

                users.append(users_item)

        _databases = d.pop("databases", UNSET)
        databases: list[LogicalDatabaseResponse] | Unset = UNSET
        if _databases is not UNSET:
            databases = []
            for componentsschemas_logical_databases_response_item_data in _databases:
                componentsschemas_logical_databases_response_item = LogicalDatabaseResponse.from_dict(
                    componentsschemas_logical_databases_response_item_data
                )

                databases.append(componentsschemas_logical_databases_response_item)

        _acls = d.pop("acls", UNSET)
        acls: list[DatabaseAclResponse] | Unset = UNSET
        if _acls is not UNSET:
            acls = []
            for acls_item_data in _acls:
                acls_item = DatabaseAclResponse.from_dict(acls_item_data)

                acls.append(acls_item)

        _service_integrations = d.pop("service_integrations", UNSET)
        service_integrations: list[DatabaseServiceIntegrationResponse] | Unset = UNSET
        if _service_integrations is not UNSET:
            service_integrations = []
            for service_integrations_item_data in _service_integrations:
                service_integrations_item = DatabaseServiceIntegrationResponse.from_dict(service_integrations_item_data)

                service_integrations.append(service_integrations_item)

        database_service_information_response = cls(
            uuid=uuid,
            zone=zone,
            name=name,
            title=title,
            type_=type_,
            plan=plan,
            plan_components=plan_components,
            additional_disk_space_gib=additional_disk_space_gib,
            state=state,
            state_error=state_error,
            powered=powered,
            termination_protection=termination_protection,
            node_count=node_count,
            create_time=create_time,
            update_time=update_time,
            service_uri=service_uri,
            service_uri_params=service_uri_params,
            maintenance=maintenance,
            metadata=metadata,
            properties=properties,
            networks=networks,
            node_states=node_states,
            labels=labels,
            backups=backups,
            components=components,
            connection_pools=connection_pools,
            users=users,
            databases=databases,
            acls=acls,
            service_integrations=service_integrations,
        )

        database_service_information_response.additional_properties = d
        return database_service_information_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
