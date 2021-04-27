import ast
import os.path
import re

from setuptools import setup


def get_version(rel_path: str) -> str:
    """
    Parse a version string from a __version__ = ... line in the given file.
    """
    with open(os.path.join(os.path.dirname(__file__), rel_path)) as infp:
        match = re.search("__version__ = (.+?)$", infp.read(), re.M)
        if not match:
            raise ValueError("No version could be found")
        return ast.literal_eval(match.group(1))


with open('README.md') as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(version=get_version('upcloud_api/__init__.py'))
