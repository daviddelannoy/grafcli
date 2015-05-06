#!/usr/bin/python3
from setuptools import setup, find_packages

setup(name='grafcli',
      version='0.1.0',
      description='Grafana CLI management tool',
      author='Milosz Smolka',
      author_email='m110@m110.pl',
      url='https://github.com/m110/grafcli',
      packages=find_packages(exclude=['tests']),
      scripts=['scripts/grafcli'],
      data_files=[('/etc/grafcli', ['grafcli.example.conf'])],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.4',
          'Topic :: System :: Systems Administration',
      ])
