# -*- coding: utf-8 -*-
from fabric.api import *

env.user = 'www-data'
env.hosts = ['server1.com','server2.com']

def pack():
    #create a new source distribution as tarball
    local('python setup.py sdist --format=gztar', capture = False)

def deploy():
    dist = local('python setup.py --fullname', capture = True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/demo.tar.gz')
    run('mkdir /tmp/demo')
    with cd('/tmp/demo'):
        run('tar xzf /tmp/demo.tar.gz')
        run('./bootstrap/ve python setup.py install')
    run('rm -fr /tmp/demo /tmp/demo.tar.gz')
    run()
