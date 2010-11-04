#!/usr/bin/env python

from setuptools import setup

setup(name='django-blog',
      version='0.1',
      description='Simple Django Blog with Markdown',
      author='aaron madison',
      packages=['blog', 'wmd', 'ext'],
      package_dir={'': 'src'},
      install_requires=['django==1.2.3', 'mock', 'markdown', 'pyyaml', 'django-debug-toolbar', 'south',],
      entry_points=("""
        [console_scripts]
        manage=manage:main
        """)
      )
