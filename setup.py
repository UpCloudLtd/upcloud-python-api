#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup

setup(name='UpCloud',
      version='0.1',
      description='UpCloud API Client',
      author='Elias Nygren',
      author_email='elias.nygren@upcloud.com',
      url='https://www.upcloud.com',
      packages=['upcloud', 'upcloud.cloud_manager'],
      install_requires=[
  		'mock==1.0.1',
		'py==1.4.26',
		'pytest==2.6.4',
		'requests==2.6.0',
		'responses==0.3.0',
		'six==1.9.0'
      ]
)
