


def assignIfExists(opts, default=None, **kwargs):
	"""
	Helper for assigning object attributes from API responses.
	"""
	for opt in opts:
		if(opt in kwargs):
			return kwargs[opt]
	return default

class ZONE:
	"""
	Enums for UpCloud's Zones.
	"""
	Helsinki = "fi-hel1"
	London = "uk-lon1"
	Chicago = "us-chi1"

class OperatingSystems:
	templates = {
		"CentOS 6.5":	"01000000-0000-4000-8000-000050010200",
		"CentOS 7.0":	"01000000-0000-4000-8000-000050010300",
		"Debian 7.8":	"01000000-0000-4000-8000-000020020100",
		"Ubuntu 12.04":	"01000000-0000-4000-8000-000030030200",
		"Ubuntu 14.04":	"01000000-0000-4000-8000-000030040200",
		"Windows 2003":	"01000000-0000-4000-8000-000010040400",
		"Windows 2008":	"01000000-0000-4000-8000-000010030200",
		"Windows 2012":	"01000000-0000-4000-8000-000010050200"
	}

	@classmethod
	def get_OS_UUID(cls, os):
		"""
		Validate Storage OS, return the public template UUID for server creation (Server.prepate_post_body)
		"""

		if os in cls.templates:
			return cls.templates[os]
		else:
			raise Exception('Invalid OS -- valid options are: "CentOS 6.5", "CentOS 7.0", "Debian 7.8", "Ubuntu 12.04", "Ubuntu 14.04", "Windows 2003", "Windows 2008", "Windows 2012"')



			