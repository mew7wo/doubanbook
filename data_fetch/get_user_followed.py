#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:user_follower.py
#create time:Thu 31 Jan 2013 04:49:13 PM CST


import sys
sys.path.append('..')


import json
from data_process.followed import Followed
from utils.fetch import Fetch


def run():
    fetch = Fetch()
    followed = Followed()
    out_file = open('../data_sets/seed_user_rel.txt', 'w')
    with open('../data_sets/seed_user.txt', 'r') as f:
        for line in f:
            user_id = line.rstrip('\n').decode('utf-8')
            url = followed.getUrlByUser(user_id)
            page = fetch.get(url, sleeptime=2.3)
            ids = followed.getFollowedUser(page)
            json_obj = {}
            json_obj['id'] = user_id
            json_obj['followed'] = list(ids)
            out_file.write(json.dumps(json_obj) + '\n')

    out_file.close()


if __name__ == '__main__':
    run()
