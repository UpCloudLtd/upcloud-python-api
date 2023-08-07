from upcloud_api.label import Label
from upcloud_api.upcloud_resource import UpCloudResource


class LoadBalancerFrontEndRule(UpCloudResource):
    """
    Class representation of loadbalancer frontend rule
    """

    ATTRIBUTES = {
        'name': '',
        'priority': 0,
        'matchers': [],
        'actions': [],
    }

    def to_dict(self):
        """
        Returns a dictionary object that adheres to UpCloud API json spec
        """
        return {
            'name': self.name,
            'priority': getattr(self, 'priority', 0),
            'actions': getattr(self, 'actions', []),
            'matchers': getattr(self, 'matchers', []),
        }


class LoadBalancerFrontend(UpCloudResource):
    """
    Class representation of loadbalancer frontend
    """

    ATTRIBUTES = {
        'name': '',
        'mode': '',
        'port': 0,
        'default_backend': '',
        'networks': [],
        'rules': None,
        'tls_configs': None,
        'properties': None,
    }

    def to_dict(self):
        """
        Returns a dictionary object that adheres to UpCloud API json spec
        """
        body = {
            'name': self.name,
            'mode': self.mode,
            'port': self.port,
            'networks': self.networks,
            'default_backend': self.default_backend,
        }

        if hasattr(self, 'rules'):
            fe_rules = []
            for rule in self.rules:
                if isinstance(rule, LoadBalancerFrontEndRule):
                    rule = rule.to_dict()
                fe_rules.append(rule)

            body['rules'] = fe_rules

        if hasattr(self, 'tls_configs'):
            body['tls_configs'] = self.tls_configs
        if hasattr(self, 'properties'):
            body['properties'] = self.properties

        return body


class LoadBalancerBackendMember(UpCloudResource):
    """
    Class representation of loadbalancer backend member
    """

    ATTRIBUTES = {
        'name': '',
        'type': 'static',
        'ip': None,
        'port': None,
        'weight': 1,
        'max_sessions': 100,
        'enabled': True,
    }

    def to_dict(self):
        """
        Returns a dictionary object that adheres to UpCloud API json spec
        """
        body = {
            'name': self.name,
            'type': getattr(self, 'type', 'static'),
            'weight': getattr(self, 'weight', 1),
            'max_sessions': getattr(self, 'max_sessions', 100),
            'enabled': getattr(self, 'enabled', True),
        }

        if hasattr(self, 'ip'):
            body['ip'] = self.ip
        if hasattr(self, 'port'):
            body['port'] = self.port

        return body


class LoadBalancerBackend(UpCloudResource):
    """
    Class representation of loadbalancer backend
    """

    ATTRIBUTES = {
        'name': '',
        'members': [],
        'resolver': None,
        'properties': None,
    }

    def to_dict(self):
        """
        Returns a dictionary object that adheres to UpCloud API json spec
        """
        be_members = []
        for member in self.members:
            if isinstance(member, LoadBalancerBackendMember):
                member = member.to_dict()
            be_members.append(member)

        body = {
            'name': self.name,
            'members': be_members,
        }

        if hasattr(self, 'resolver'):
            body['resolver'] = self.resolver
        if hasattr(self, 'properties'):
            body['properties'] = self.properties

        return body


class LoadBalancerNetwork(UpCloudResource):
    """
    Class representation of networks loadbalancer is attached to
    """

    ATTRIBUTES = {
        'name': '',
        'type': '',
        'family': 'IPv4',
        'uuid': None,
    }

    def to_dict(self):
        """
        Returns a dictionary object that adheres to UpCloud API json spec
        """
        body = {
            'name': self.name,
            'type': self.type,
            'family': getattr(self, 'family', 'IPv4'),
        }

        if hasattr(self, 'uuid'):
            body['uuid'] = self.uuid

        return body


class LoadBalancer(UpCloudResource):
    """
    Class representation of UpCloud loadbalancer
    """

    ATTRIBUTES = {
        'name': '',
        'zone': '',
        'plan': 'development',
        'configured_status': 'started',
        'networks': [],
        'frontends': None,
        'backends': None,
        'resolvers': None,
        'labels': None,
        'maintenance_dow': None,
        'maintenance_time': None,
    }

    def to_dict(self):
        """
        Returns a dictionary object that adheres to UpCloud API json spec
        """
        nets = []
        for net in self.networks:
            if isinstance(net, LoadBalancerNetwork):
                net = net.to_dict()
            nets.append(net)

        body = {
            'name': self.name,
            'zone': self.zone,
            'plan': getattr(self, 'plan', 'development'),
            'configured_status': getattr(self, 'configured_status', 'started'),
            'networks': nets,
        }

        if hasattr(self, 'frontends'):
            lb_fe = []
            for fe in self.frontends:
                if isinstance(fe, LoadBalancerFrontend):
                    fe = fe.to_dict()
                lb_fe.append(fe)
            body['frontends'] = lb_fe

        if hasattr(self, 'backends'):
            lb_be = []
            for be in self.backends:
                if isinstance(be, LoadBalancerBackend):
                    be = be.to_dict()
                lb_be.append(be)
            body['backends'] = lb_be

        if hasattr(self, 'labels'):
            lb_labels = []
            for label in self.labels:
                if isinstance(label, Label):
                    label = label.to_dict()
                lb_labels.append(label)
            body['labels'] = lb_labels

        if hasattr(self, 'maintenance_dow'):
            body['maintenance_dow'] = self.maintenance_dow
        if hasattr(self, 'maintenance_time'):
            body['maintenance_time'] = self.maintenance_time

        return body
