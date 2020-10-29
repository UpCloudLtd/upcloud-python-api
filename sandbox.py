import upcloud_api
from upcloud_api import Server, Storage, ZONE, login_user_block

manager = upcloud_api.CloudManager('techconsult', 'LetMeTest123')
manager.authenticate()


storages = manager.get_storages(storage_type='template')
