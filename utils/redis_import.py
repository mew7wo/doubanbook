#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:redis_import.py
#create time:Wed 28 Nov 2012 04:22:19 PM CST

from redis import Redis


def main():
    rq = Redis()

    with open('new_urls', 'r') as f:
        for url in f:
            rq.sadd('set:url:new', url.rstrip('\n'))

    with open('old_urls', 'r') as f:
        for url in f:
            rq.sadd('set:url:old', url.rstrip('\n'))


if __name__ == '__main__':
    print 'begin...'
    main()
    print 'end....'
