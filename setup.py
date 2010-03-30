#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

def list_files(path):
    for fn in os.listdir(path):
        if fn.startswith('.'):
            continue
        fn = os.path.join(path, fn)
        if os.path.isfile(fn):
            yield fn

setup(name='memcached_lock',
      version = '1.1',
      author="amix the lucky stiff",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['memcached_lock'],
      platforms=["Any"],
      license="BSD",
      keywords='memcached lock distributed',
      description="Implements a distributed lock on top of memcached.",
      long_description="""\
memcached_lock
---------------

Implements a distributed transaction using memcached or
a memcached compatible storage.


Example
-------

Basic example of usage::

    from __future__ import with_statement
    import memcache
    from memcached_lock import dist_lock

    client = memcache.Client(['127.0.0.1:11211'])
    with dist_lock('test', client):
        print 'Is there anybody out there!?'
""")
