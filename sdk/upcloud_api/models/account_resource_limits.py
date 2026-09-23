from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountResourceLimits")


@_attrs_define
class AccountResourceLimits:
    """Per-resource quota limits for an account.

    Attributes:
        managed_databases (int | Unset): The maximum number of managed databases allowed.
        network_peerings (int | Unset): The maximum number of network peerings allowed.
        file_storages (int | Unset): The maximum number of file storage instances allowed.
        managed_container_registries (int | Unset): The maximum number of managed container registries allowed.
        managed_kubernetes (int | Unset): The maximum number of managed Kubernetes clusters allowed.
        tags (int | Unset): The maximum number of tags allowed.
        cores (int | Unset): The maximum number of CPU cores allowed.
        cloud_server_dev_1xcpu_1gb_10gb_plans (int | None | Unset): The maximum number of cloud server dev 1xCPU 1GB
            10GB plans allowed.
        cloud_server_dev_1xcpu_1gb_plans (int | None | Unset): The maximum number of cloud server dev 1xCPU 1GB 10GB
            plans allowed.
        storage_hdd (int | Unset): The maximum amount of HDD storage (in GiB) allowed.
        networks (int | Unset): The maximum number of networks allowed.
        network_gateways_essentials (int | Unset): The maximum number of essential network gateways allowed.
        network_gateways (int | Unset): The maximum number of network gateways allowed.
        storage_ssd (int | Unset): The maximum amount of SSD storage (in GiB) allowed.
        load_balancers_essentials (int | Unset): The maximum number of essential load balancers allowed.
        load_balancers (int | Unset): The maximum number of load balancers allowed.
        gpus (int | Unset): The maximum number of GPUs allowed.
        detached_interfaces (int | Unset): The maximum number of detached network interfaces allowed.
        detached_floating_ips (int | Unset): The maximum number of detached floating IPs allowed.
        managed_object_storages (int | Unset): The maximum number of managed object storage instances allowed.
        memory (int | Unset): The maximum amount of memory (in MiB) allowed.
        ntp_excess_gib (int | Unset): The maximum amount of excess NTP data (in GiB) allowed.
        public_ipv4 (int | Unset): The maximum number of public IPv4 addresses allowed.
        public_ipv6 (int | Unset): The maximum number of public IPv6 addresses allowed.
        routers (int | Unset): The maximum number of routers allowed.
        storage_maxiops (int | Unset): The maximum amount of MaxiOPS storage (in GiB) allowed.
        storage_standard (int | Unset): The maximum amount of standard storage (in GiB) allowed.
        storage_total (int | Unset): The maximum total amount of storage (in GiB) allowed.
        type_ (Any | Unset):
        required (Any | Unset):
        additional_properties (Any | Unset):
    """

    managed_databases: int | Unset = UNSET
    network_peerings: int | Unset = UNSET
    file_storages: int | Unset = UNSET
    managed_container_registries: int | Unset = UNSET
    managed_kubernetes: int | Unset = UNSET
    tags: int | Unset = UNSET
    cores: int | Unset = UNSET
    cloud_server_dev_1xcpu_1gb_10gb_plans: int | None | Unset = UNSET
    cloud_server_dev_1xcpu_1gb_plans: int | None | Unset = UNSET
    storage_hdd: int | Unset = UNSET
    networks: int | Unset = UNSET
    network_gateways_essentials: int | Unset = UNSET
    network_gateways: int | Unset = UNSET
    storage_ssd: int | Unset = UNSET
    load_balancers_essentials: int | Unset = UNSET
    load_balancers: int | Unset = UNSET
    gpus: int | Unset = UNSET
    detached_interfaces: int | Unset = UNSET
    detached_floating_ips: int | Unset = UNSET
    managed_object_storages: int | Unset = UNSET
    memory: int | Unset = UNSET
    ntp_excess_gib: int | Unset = UNSET
    public_ipv4: int | Unset = UNSET
    public_ipv6: int | Unset = UNSET
    routers: int | Unset = UNSET
    storage_maxiops: int | Unset = UNSET
    storage_standard: int | Unset = UNSET
    storage_total: int | Unset = UNSET
    type_: Any | Unset = UNSET
    required: Any | Unset = UNSET
    additional_properties: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        managed_databases = self.managed_databases

        network_peerings = self.network_peerings

        file_storages = self.file_storages

        managed_container_registries = self.managed_container_registries

        managed_kubernetes = self.managed_kubernetes

        tags = self.tags

        cores = self.cores

        cloud_server_dev_1xcpu_1gb_10gb_plans: int | None | Unset
        if isinstance(self.cloud_server_dev_1xcpu_1gb_10gb_plans, Unset):
            cloud_server_dev_1xcpu_1gb_10gb_plans = UNSET
        else:
            cloud_server_dev_1xcpu_1gb_10gb_plans = self.cloud_server_dev_1xcpu_1gb_10gb_plans

        cloud_server_dev_1xcpu_1gb_plans: int | None | Unset
        if isinstance(self.cloud_server_dev_1xcpu_1gb_plans, Unset):
            cloud_server_dev_1xcpu_1gb_plans = UNSET
        else:
            cloud_server_dev_1xcpu_1gb_plans = self.cloud_server_dev_1xcpu_1gb_plans

        storage_hdd = self.storage_hdd

        networks = self.networks

        network_gateways_essentials = self.network_gateways_essentials

        network_gateways = self.network_gateways

        storage_ssd = self.storage_ssd

        load_balancers_essentials = self.load_balancers_essentials

        load_balancers = self.load_balancers

        gpus = self.gpus

        detached_interfaces = self.detached_interfaces

        detached_floating_ips = self.detached_floating_ips

        managed_object_storages = self.managed_object_storages

        memory = self.memory

        ntp_excess_gib = self.ntp_excess_gib

        public_ipv4 = self.public_ipv4

        public_ipv6 = self.public_ipv6

        routers = self.routers

        storage_maxiops = self.storage_maxiops

        storage_standard = self.storage_standard

        storage_total = self.storage_total

        type_ = self.type_

        required = self.required

        additional_properties = self.additional_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if managed_databases is not UNSET:
            field_dict["managed_databases"] = managed_databases
        if network_peerings is not UNSET:
            field_dict["network_peerings"] = network_peerings
        if file_storages is not UNSET:
            field_dict["file_storages"] = file_storages
        if managed_container_registries is not UNSET:
            field_dict["managed_container_registries"] = managed_container_registries
        if managed_kubernetes is not UNSET:
            field_dict["managed_kubernetes"] = managed_kubernetes
        if tags is not UNSET:
            field_dict["tags"] = tags
        if cores is not UNSET:
            field_dict["cores"] = cores
        if cloud_server_dev_1xcpu_1gb_10gb_plans is not UNSET:
            field_dict["cloud_server_dev_1xcpu_1gb_10gb_plans"] = cloud_server_dev_1xcpu_1gb_10gb_plans
        if cloud_server_dev_1xcpu_1gb_plans is not UNSET:
            field_dict["cloud_server_dev_1xcpu_1gb_plans"] = cloud_server_dev_1xcpu_1gb_plans
        if storage_hdd is not UNSET:
            field_dict["storage_hdd"] = storage_hdd
        if networks is not UNSET:
            field_dict["networks"] = networks
        if network_gateways_essentials is not UNSET:
            field_dict["network_gateways_essentials"] = network_gateways_essentials
        if network_gateways is not UNSET:
            field_dict["network_gateways"] = network_gateways
        if storage_ssd is not UNSET:
            field_dict["storage_ssd"] = storage_ssd
        if load_balancers_essentials is not UNSET:
            field_dict["load_balancers_essentials"] = load_balancers_essentials
        if load_balancers is not UNSET:
            field_dict["load_balancers"] = load_balancers
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if detached_interfaces is not UNSET:
            field_dict["detached_interfaces"] = detached_interfaces
        if detached_floating_ips is not UNSET:
            field_dict["detached_floating_ips"] = detached_floating_ips
        if managed_object_storages is not UNSET:
            field_dict["managed_object_storages"] = managed_object_storages
        if memory is not UNSET:
            field_dict["memory"] = memory
        if ntp_excess_gib is not UNSET:
            field_dict["ntp_excess_gib"] = ntp_excess_gib
        if public_ipv4 is not UNSET:
            field_dict["public_ipv4"] = public_ipv4
        if public_ipv6 is not UNSET:
            field_dict["public_ipv6"] = public_ipv6
        if routers is not UNSET:
            field_dict["routers"] = routers
        if storage_maxiops is not UNSET:
            field_dict["storage_maxiops"] = storage_maxiops
        if storage_standard is not UNSET:
            field_dict["storage_standard"] = storage_standard
        if storage_total is not UNSET:
            field_dict["storage_total"] = storage_total
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        managed_databases = d.pop("managed_databases", UNSET)

        network_peerings = d.pop("network_peerings", UNSET)

        file_storages = d.pop("file_storages", UNSET)

        managed_container_registries = d.pop("managed_container_registries", UNSET)

        managed_kubernetes = d.pop("managed_kubernetes", UNSET)

        tags = d.pop("tags", UNSET)

        cores = d.pop("cores", UNSET)

        def _parse_cloud_server_dev_1xcpu_1gb_10gb_plans(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_server_dev_1xcpu_1gb_10gb_plans = _parse_cloud_server_dev_1xcpu_1gb_10gb_plans(
            d.pop("cloud_server_dev_1xcpu_1gb_10gb_plans", UNSET)
        )

        def _parse_cloud_server_dev_1xcpu_1gb_plans(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_server_dev_1xcpu_1gb_plans = _parse_cloud_server_dev_1xcpu_1gb_plans(
            d.pop("cloud_server_dev_1xcpu_1gb_plans", UNSET)
        )

        storage_hdd = d.pop("storage_hdd", UNSET)

        networks = d.pop("networks", UNSET)

        network_gateways_essentials = d.pop("network_gateways_essentials", UNSET)

        network_gateways = d.pop("network_gateways", UNSET)

        storage_ssd = d.pop("storage_ssd", UNSET)

        load_balancers_essentials = d.pop("load_balancers_essentials", UNSET)

        load_balancers = d.pop("load_balancers", UNSET)

        gpus = d.pop("gpus", UNSET)

        detached_interfaces = d.pop("detached_interfaces", UNSET)

        detached_floating_ips = d.pop("detached_floating_ips", UNSET)

        managed_object_storages = d.pop("managed_object_storages", UNSET)

        memory = d.pop("memory", UNSET)

        ntp_excess_gib = d.pop("ntp_excess_gib", UNSET)

        public_ipv4 = d.pop("public_ipv4", UNSET)

        public_ipv6 = d.pop("public_ipv6", UNSET)

        routers = d.pop("routers", UNSET)

        storage_maxiops = d.pop("storage_maxiops", UNSET)

        storage_standard = d.pop("storage_standard", UNSET)

        storage_total = d.pop("storage_total", UNSET)

        type_ = d.pop("type", UNSET)

        required = d.pop("required", UNSET)

        additional_properties = d.pop("additionalProperties", UNSET)

        account_resource_limits = cls(
            managed_databases=managed_databases,
            network_peerings=network_peerings,
            file_storages=file_storages,
            managed_container_registries=managed_container_registries,
            managed_kubernetes=managed_kubernetes,
            tags=tags,
            cores=cores,
            cloud_server_dev_1xcpu_1gb_10gb_plans=cloud_server_dev_1xcpu_1gb_10gb_plans,
            cloud_server_dev_1xcpu_1gb_plans=cloud_server_dev_1xcpu_1gb_plans,
            storage_hdd=storage_hdd,
            networks=networks,
            network_gateways_essentials=network_gateways_essentials,
            network_gateways=network_gateways,
            storage_ssd=storage_ssd,
            load_balancers_essentials=load_balancers_essentials,
            load_balancers=load_balancers,
            gpus=gpus,
            detached_interfaces=detached_interfaces,
            detached_floating_ips=detached_floating_ips,
            managed_object_storages=managed_object_storages,
            memory=memory,
            ntp_excess_gib=ntp_excess_gib,
            public_ipv4=public_ipv4,
            public_ipv6=public_ipv6,
            routers=routers,
            storage_maxiops=storage_maxiops,
            storage_standard=storage_standard,
            storage_total=storage_total,
            type_=type_,
            required=required,
            additional_properties=additional_properties,
        )

        account_resource_limits.additional_properties = d
        return account_resource_limits

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
