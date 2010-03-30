memcached_lock
-----

Implements a distributed transaction using memcached or
a memcached compatible storage.

Example:

    from __future__ import with_statement
    import memcache
    from memcached_lock import dist_lock

    client = memcache.Client(['127.0.0.1:11211'])
    with dist_lock('test', client):
        print 'Is there anybody out there!?'

© 2010 amix the lucky stiff

License BSD
