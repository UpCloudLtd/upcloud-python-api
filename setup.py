#!/usr/bin/env python

from setuptools import setup
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open('README.md') as f:
    long_description = f.read()

version = get_version('upcloud_api/__init__.py')
setup(
    name='upcloud-api',
    version=version,
    description='UpCloud API Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Elias Nygren',
    maintainer='UpCloud',
    maintainer_email='hello@upcloud.com',
    url='https://github.com/UpCloudLtd/upcloud-python-api',
    packages=['upcloud_api', 'upcloud_api.cloud_manager'],
    download_url='https://github.com/UpCloudLtd/upcloud-python-api/archive/%s.tar.gz' % version,
    license='MIT',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'requests>=2.6.0',
        'six>=1.9.0'
    ]
)
