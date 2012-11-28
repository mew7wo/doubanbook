#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:rq.py
#create time:Wed 28 Nov 2012 03:36:39 PM CST


from redis import Redis

class RedisQueue(object):
    ''' redis queue '''
    def __init__(self, name, namespace='queue', **args):
        self._rq = Redis(**args)
        self._key = '%s:%s' % (namespace, name)
