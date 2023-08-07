from upcloud_api.api import API
from upcloud_api.load_balancer import LoadBalancer, LoadBalancerBackend


class LoadBalancerManager:
    """
    Functions for managing UpCloud loadbalancer instances and their properties with basic dictionary objects
    """

    api: API

    def get_loadbalancers(self):
        """
        Returns a list of loadbalancer dictionary objects
        """

        url = '/load-balancer'
        return self.api.get_request(url)

    def get_loadbalancer(self, lb_uuid: str):
        """
        Returns details for a single loadbalancer as a dictionary

        :param lb_uuid:
        :return: LB details
        """
        url = f'/load-balancer/{lb_uuid}'
        return self.api.get_request(url)

    def create_loadbalancer(self, body: LoadBalancer):
        """
        Creates a loadbalancer service specified in body and returns its details

        :param body:
        :return: LB details
        """

        url = '/load-balancer'
        return self.api.post_request(url, body.to_dict())

    def delete_loadbalancer(self, lb_uuid: str):
        """
        Deletes a loadbalancer service

        :param lb_uuid:
        """

        url = f'/load-balancer/{lb_uuid}'
        return self.api.delete_request(url)

    def get_loadbalancer_backends(self, lb_uuid: str):
        """
        Returns a list of backends for a loadbalancer service

        :param lb_uuid:
        :return: List of LB backends
        """

        url = f'/load-balancer/{lb_uuid}/backends'
        return self.api.get_request(url)

    def get_loadbalancer_backend(self, lb_uuid: str, backend: LoadBalancerBackend):
        """
        Returns details for a single loadbalancer backend

        :param lb_uuid:
        :param backend:
        :return: LB backend details
        """

        url = f'/load-balancer/{lb_uuid}/backends/{backend.name}'
        return self.api.get_request(url)

    def create_loadbalancer_backend(self, lb_uuid: str, body: LoadBalancerBackend):
        """
        Creates a new backend for a loadbalancer and returns its details

        :param lb_uuid:
        :param body:
        :return: LB backend details
        """

        url = f'/load-balancer/{lb_uuid}/backends'
        return self.api.post_request(url, body.to_dict())

    def modify_loadbalancer_backend(self, lb_uuid: str, backend: str, body: LoadBalancerBackend):
        """
        Modifies an existing loadbalancer backend and returns its details

        :param lb_uuid:
        :param backend:
        :param body:
        :return: LB backend details
        """

        url = f'/load-balancer/{lb_uuid}/backends/{backend}'
        return self.api.patch_request(url, body.to_dict())

    def delete_loadbalancer_backend(self, lb_uuid: str, backend: str):
        """
        Deletes a loadbalancer backend

        :param lb_uuid:
        :param backend:
        :return:
        """

        url = f'/load-balancer/{lb_uuid}/backends/{backend}'
        return self.api.delete_request(url)
