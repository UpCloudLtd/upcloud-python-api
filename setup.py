#!/usr/bin/env python

from setuptools import setup

setup(
    name='upcloud-api',
    version='0.3.5',
    description='UpCloud API Client',
    author='Elias Nygren',
    author_email='elias.nygren@upcloud.com',
    maintainer='Elias Nygren',
    maintainer_email='elias.nygren@upcloud.com',
    url='https://github.com/UpCloudLtd/upcloud-python-api',
    packages=['upcloud_api', 'upcloud_api.cloud_manager'],
    download='https://github.com/UpCloudLtd/upcloud-python-api/tarball/v0.3.5',
    license='MIT',
    install_requires=[
    	'future==0.14.3',
        'mock==1.0.1',
        'requests==2.6.0',
        'responses==0.3.0',
        'six==1.9.0',
        'wheel==0.24.0'
    ]
)
