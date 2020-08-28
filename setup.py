#!/usr/bin/env python

from setuptools import setup


version = '0.4.6'
with open('README.md') as f:
    long_description = f.read()

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
    python_requires='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'requests>=2.6.0',
        'six>=1.9.0'
    ]
)
