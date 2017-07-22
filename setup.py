#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='m18nify',
      version='0.1',
      description='cli utility to simplify the process of internationalization in the YunoHost project',
      author='Laurent Peuch',
      #long_description='',
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/m18nify',
      install_requires=['RedBaron'],
      packages=[],
      py_modules=[],
      license= 'wtfpl',
      scripts=['m18nify'],
      keywords='yunohost internationalization',
     )
