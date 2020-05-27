from __future__ import unicode_literals
from __future__ import absolute_import

import re


class ZONE(object):
    """
    Enums for UpCloud's Zones.
    """

    Helsinki = 'fi-hel1'
    Helsinki2 = 'fi-hel2'
    London = 'uk-lon1'
    Chicago = 'us-chi1'
    Frankfurt = 'de-fra1'
    Amsterdam = 'nl-ams1'
    Singapore = 'sg-sin1'
    SanJose = 'us-sjo1'


class OperatingSystems(object):
    """
    Helper class for dealing with operating system names.
    """

    templates = {
        'CentOS 6.10': '01000000-0000-4000-8000-000050010200',
        'CentOS 7.6': '01000000-0000-4000-8000-000050010300',
        'CentOS 8.0': '01000000-0000-4000-8000-000050010400',
        'Debian 8.11': '01000000-0000-4000-8000-000020030100',
        'Debian 9.9': '01000000-0000-4000-8000-000020040100',
        'Debian 10.0': '01000000-0000-4000-8000-000020050100',
        'Ubuntu 16.04': '01000000-0000-4000-8000-000030060200',
        'Ubuntu 18.04': '01000000-0000-4000-8000-000030080200',
        'Ubuntu 20.04': '01000000-0000-4000-8000-000030200200',
        'CoreOS Stable 1068.8.0': '01000000-0000-4000-8000-000080010200',
        'Windows 2016': '01000000-0000-4000-8000-000010060200',
        'Windows 2019': '01000000-0000-4000-8000-000010070200',
    }

    @classmethod
    def get_OS_UUID(cls, os):
        """
        Validate Storage OS and its UUID.

        If the OS is a custom OS UUID, don't validate against templates.
        """
        if os in cls.templates:
            return cls.templates[os]

        uuid_regexp = '^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$'
        if re.search(uuid_regexp, os):
            return os

        raise Exception((
            "Invalid OS -- valid options are: "
            "'CentOS 6.10', 'CentOS 7', 'Centos 8', "
            "'Debian 8.11', 'Debian 9.9', 'Debian 10.10', "
            "'Ubuntu 12.04', 'Ubuntu 16.04', 'Ubuntu 18.04', 'Ubuntu 20.04', "
            "'Windows 2016', 'Windows 2019'"
        ))
