#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:fetch_test.py
#create time:Wed 30 Jan 2013 05:11:33 PM CST

import sys
sys.path.append('..')

from utils.fetch import Fetcher

def testGet():
    f = Fetcher()
    content = f.get('http://www.douban.com/people/51417203/')
#    content = f.get('http://www.douban.com/people/dadfsajfio')
#    content = f.get('httafdajfpd')
    content = f.get(None, 2)
    print content
     

def main():
    testGet()

if __name__ == '__main__':
    print 'begin..'
    main()
    print 'end ...'

