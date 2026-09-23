from importlib.metadata import version

import upcloud_api


def test_package_version_matches_distribution():
    assert upcloud_api.__version__ == version("upcloud-api")
