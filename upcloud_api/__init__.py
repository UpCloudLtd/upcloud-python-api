"""
Python Interface to UpCloud's API
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

__version__ = "0.3.5"
__author__ = "Elias Nygren"
__author_email__ = "elias.nygren@upcloud.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2015 Elias Nygren"

from upcloud_api.storage import Storage
from upcloud_api.ip_address import IP_address
from upcloud_api.server import Server, login_user_block
from upcloud_api.firewall import FirewallRule
from upcloud_api.tools import OperatingSystems, ZONE
from upcloud_api.tag import Tag
from upcloud_api.cloud_manager.cloud_manager import CloudManager
