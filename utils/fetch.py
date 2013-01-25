#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:fetch.py
#create time:Wed 28 Nov 2012 02:20:12 PM CST

import urllib2
import cookielib


class Fetch(object):
    ''' url fetch class '''

    def __init__(self, queue, cookie=False):
        self._queue = queue
        if cookie:
            cj = cookielib.CookieJar() 
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        else:
            self.opener = urllib2.build_opener()

    def get(self, headers=None):
        url = self._queue.get()
        
