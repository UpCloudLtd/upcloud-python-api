from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import six

from upcloud_api import Tag


class TagManager(object):
    """
    Functions for managing Tags.

    Intended to be used as a mixin for CloudManager.
    """

    def get_tags(self):
        """List all tags as Tag objects."""
        res = self.get_request('/tag')
        return [Tag(cloud_manager=self, **tag) for tag in res['tags']['tag']]

    def get_tag(self, name):
        """Return the tag as Tag object."""
        res = self.get_request('/tag/' + name)
        return Tag(cloud_manager=self, **res['tag'])

    def create_tag(self, name, description=None, servers=[]):
        """
        Create a new Tag. Only name is mandatory.

        Returns the created Tag object.
        """
        servers = [str(server) for server in servers]
        body = {'tag': Tag(name, description, servers).to_dict()}
        res = self.post_request('/tag', body)

        return Tag(cloud_manager=self, **res['tag'])

    def _modify_tag(self, name, description, servers, new_name):
        """
        PUT /tag/name. Returns a dict that can be used to create a Tag object.

        Private method used by the Tag class and TagManager.modify_tag.
        """
        body = {'tag': Tag(new_name, description, servers).to_dict()}
        res = self.put_request('/tag/' + name, body)
        return res['tag']

    def modify_tag(self, name, description=None, servers=None, new_name=None):
        """
        PUT /tag/name. Returns a new Tag object based on the API response.
        """
        res = self._modify_tag(name, description, servers, new_name)
        return Tag(cloud_manager=self, **res['tag'])

    def assign_tags(self, server, tags):
        """
        Assign tags to a server.

        - server: Server object or UUID string
        - tags: list of Tag objects or strings
        """
        uuid = str(server)
        tags = [str(tag) for tag in tags]

        url = '/server/{0}/tag/{1}'.format(uuid, ','.join(tags))
        return self.post_request(url)

    def remove_tags(self, server, tags):
        """
        Remove tags from a server.

        - server: Server object or UUID string
        - tags: list of Tag objects or strings
        """
        uuid = str(server)
        tags = [str(tag) for tag in tags]

        url = '/server/{0}/untag/{1}'.format(uuid, ','.join(tags))
        return self.post_request(url)

    def delete_tag(self, tag):
        """Delete the Tag. Returns and empty object."""
        return self.delete_request('/tag/' + str(tag))
