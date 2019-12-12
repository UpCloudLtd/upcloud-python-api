#!/usr/bin/env python

from setuptools import setup


version = '0.4.5'

setup(
    name='upcloud-api',
    version=version,
    description='UpCloud API Client',
    author='Elias Nygren',
    maintainer='Mika Lackman',
    maintainer_email='mika.lackman@upcloud.com',
    url='https://github.com/UpCloudLtd/upcloud-python-api',
    packages=['upcloud_api', 'upcloud_api.cloud_manager'],
    download_url='https://github.com/UpCloudLtd/upcloud-python-api/archive/%s.tar.gz' % version,
    license='MIT',
    install_requires=[
        'requests>=2.6.0',
        'six>=1.9.0'
    ]
)
