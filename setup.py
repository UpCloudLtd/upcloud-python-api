#!/usr/bin/env python

from setuptools import setup

setup(
    name='upcloud-api',
    version='0.4.2',
    description='UpCloud API Client',
    author='Elias Nygren',
    maintainer='Mika Lackman',
    maintainer_email='mika.lackman@upcloud.com',
    url='https://github.com/UpCloudLtd/upcloud-python-api',
    packages=['upcloud_api', 'upcloud_api.cloud_manager'],
    download='https://github.com/UpCloudLtd/upcloud-python-api/tarball/v0.4.1',
    license='MIT',
    install_requires=[
        'requests>=2.6.0',
        'six>=1.9.0'
    ]
)
