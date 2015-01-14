#!/usr/bin/env python

from distutils.core import setup

setup(name='MusicPi',
      version='0.5',
      description='MusicServer with python.',
      author='Kosuke Nagano',
      author_email='gm.charlie@gmail.com',
      license='MIT',
      install_requires=[
        'bottle', 'qrcode'
        ],
      )

