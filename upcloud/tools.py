from .storage import Storage
from .ip_address import IP_address

def _create_ip_address_objs(IP_addrs, cloud_manager):
		IP_addrs = IP_addrs["ip_address"]
		IP_objs = list()
		for IP_addr in IP_addrs:
			IP_objs.append( IP_address(cloud_manager = cloud_manager, **IP_addr) )
		return IP_objs

def _create_ip_address_obj(IP_addr, cloud_manager):
	return IP_address(cloud_manager = cloud_manager, **IP_addr)

def _create_storage_objs(storages, cloud_manager):
	if "storage" in storages:
		storages = storages["storage"]

	if "storage_device" in storages:
		storages = storages["storage_device"]

	storage_objs = list()
	for storage in storages:
		storage_objs.append( Storage(cloud_manager = cloud_manager, **storage) )
	return storage_objs

def _create_storage_obj(storage, cloud_manager):
	return Storage(cloud_manager = cloud_manager, **storage)