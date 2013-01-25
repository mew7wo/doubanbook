#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:user_tags.py
#create time:Thu 29 Nov 2012 08:49:28 PM CST

import urllib2
import re

api = 'https://api.douban.com/v2/book/user/%s/tags'

def main():
    new_ids = set() 
    old_ids = set()
    with open('id.txt', 'r') as f:
        for i in xrange(100000):
            f.readline()

        for i in xrange(20000):
            new_ids.add(f.readline()) 

    with open('./user_tags/new_ids.txt', 'w') as f:
        for user_id in new_ids:
            f.write(user_id)
    

if __name__ == '__main__':
    main()
