from enum import Enum

from upcloud_api.upcloud_resource import UpCloudResource


class ServerGroupAffinityPolicy(str, Enum):
    """
    Enum representation of affinity policy for a server group
    """

    STRICT_ANTI_AFFINITY = 'strict'
    ANTI_AFFINITY_PREFERRED = 'yes'
    NO_ANTI_AFFINITY = 'no'


class ServerGroup(UpCloudResource):
    """
    Class representation of UpCloud server group resource
    """

    ATTRIBUTES = {
        'anti_affinity': ServerGroupAffinityPolicy.NO_ANTI_AFFINITY,
        'labels': None,
        'servers': None,
        'title': None,
        'uuid': None,
    }

    def __str__(self) -> str:
        return self.title

    def to_dict(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.
        """
        body = {
            'title': self.title,
        }

        if hasattr(self, 'anti_affinity'):
            body['anti_affinity'] = f"{self.anti_affinity}"

        if hasattr(self, 'servers'):
            servers = []
            for server in self.servers:
                if isinstance(server, server.Server) and hasattr(server, 'uuid'):
                    servers.append(server.uuid)
                else:
                    servers.append(server)

        if hasattr(self, 'labels'):
            dict_labels = {'label': []}
            for label in self.labels:
                dict_labels['label'].append(label.to_dict())
            body['labels'] = dict_labels

        return {'server_group': body}
