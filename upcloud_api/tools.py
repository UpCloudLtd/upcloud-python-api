from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import object

import re

def assignIfExists(opts, default=None, **kwargs):
	"""
	Helper for assigning object attributes from API responses.
	"""
	for opt in opts:
		if(opt in kwargs):
			return kwargs[opt]
	return default

class ZONE(object):
	"""
	Enums for UpCloud's Zones.
	"""
	Helsinki = 'fi-hel1'
	London = 'uk-lon1'
	Chicago = 'us-chi1'
	Frankfurt = 'de-fra1'

class OperatingSystems(object):
	templates = {
		'CentOS 6.5':	'01000000-0000-4000-8000-000050010200',
		'CentOS 7.0':	'01000000-0000-4000-8000-000050010300',
		'Debian 7.8':	'01000000-0000-4000-8000-000020020100',
		'Debian 8.0':	'01000000-0000-4000-8000-000020030100',
		'Ubuntu 12.04':	'01000000-0000-4000-8000-000030030200',
		'Ubuntu 14.04':	'01000000-0000-4000-8000-000030040200',
		'Ubuntu 16.04': '01000000-0000-4000-8000-000030060200',
		'Windows 2008':	'01000000-0000-4000-8000-000010030200',
		'Windows 2012':	'01000000-0000-4000-8000-000010050200'
	}

	@classmethod
	def get_OS_UUID(cls, os):
		"""
		Validate Storage OS, return the public template UUID for server creation (Server.prepate_post_body).
		If the OS is a custom OS UUID, don't validate against templates.
		"""

		if os in cls.templates:
			return cls.templates[os]

		uuid_regexp = '^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$'
		if re.search(uuid_regexp, os):
			return os

		raise Exception((
			"Invalid OS -- valid options are: 'CentOS 6.5', 'CentOS 7.0', "
			"'Debian 7.8', 'Debian 8.0' ,'Ubuntu 12.04', 'Ubuntu 14.04', 'Ubuntu 16.04', "
			"'Windows 2008', 'Windows 2012'"
		))
