#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:douban_test.py
#create time:Thu 22 Nov 2012 08:15:44 PM CST

import sys
from douban import DouBan

def testLogin():
    db = DouBan()
    cookie_file = '/home/mew7wo/python/douban/cookie_test'
    try:
        db.login('./fuck')
    except Exception, e:
        print repr(e)    
        print 'login failure'
        sys.exit(1) 

def testPersistent():
    db = DouBan()
    try:
        db.login('cookie_test')
        db.run()
        db.persistent()
    except KeyboardInterrupt:
        db.persistent()
    except Exception, e:
        db.persistent()
        print repr(e)
        sys.exit(1)

def testRun():
    db = DouBan()
    try:
        db.login('cookie_test')
        db.run()
    except Exception, e:
        print repr(e)
        print 'run failure'
        sys.exit(1)

if __name__ == '__main__':
#testLogin()
#   testRun()
    testPersistent()
