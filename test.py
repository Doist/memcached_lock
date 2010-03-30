from __future__ import with_statement
import memcache
from memcached_lock import dist_lock

import time
from datetime import datetime

client = memcache.Client(['127.0.0.1:11211'])
with dist_lock('test', client):
    print 'Start... %s' % datetime.now()
    time.sleep(4)
    print 'I am the only one here!!!'
    print 'End... %s' % datetime.now()
