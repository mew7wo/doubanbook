#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:followed_test.py
#create time:Thu 31 Jan 2013 05:17:34 PM CST

import sys
sys.path.append('..')

from data_process.followed import Followed
from utils.fetch import Fetch


def main():
    fetch = Fetch()
    fol = Followed()
    url = fol.getUrlByUser('fenng')
    page = fetch.get(url, sleeptime=2)
    print page
    followed_user = fol.getFollowedUser(page)
    for user in followed_user:
        print '%s\n' % user


if __name__ == '__main__':
    print 'begin ..'
    main()
    print 'end ..'
