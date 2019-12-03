#!/usr/bin/env python

from setuptools import setup

setup(
    name='upcloud-api',
    version='0.4.5',
    description='UpCloud API Client',
    author='Elias Nygren',
    maintainer='Mika Lackman',
    maintainer_email='mika.lackman@upcloud.com',
    url='https://github.com/UpCloudLtd/upcloud-python-api',
    packages=['upcloud_api', 'upcloud_api.cloud_manager'],
    download_url='https://github.com/UpCloudLtd/upcloud-python-api/archive/0.4.5.tar.gz',
    license='MIT',
    install_requires=[
        'requests>=2.6.0',
        'six>=1.9.0'
    ]
)
