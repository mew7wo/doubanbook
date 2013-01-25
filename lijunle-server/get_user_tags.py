#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:get_user_tags.py
#create time:Fri 30 Nov 2012 10:27:53 AM CST

import urllib2
import json
import re
from time import sleep

api = 'https://api.douban.com/v2/book/user/%s/tags'

def main():
    new_ids = set()
    old_ids = set()
    with open('new_ids.txt', 'r') as f:
        for line in f:
            new_ids.add(line.rstrip('\n'))

    with open('old_ids.txt', 'r') as f:
        for line in f:
            old_ids.add(line.rstrip('\n'))

    with open('user_tags.txt', 'a+') as f:
        try:
            for user_id in new_ids:
                sleep(2)
                content = urllib2.urlopen(api % user_id).read()
                tags_obj = json.loads(content)
                tags_obj['id'] = user_id
                tags_json = json.dumps(tags_obj)
                print tags_json
                f.write(tags_json + '\n')
                old_ids.add(user_id)
        except:
            for user_id in old_ids:
                if user_id in new_ids:
                    new_ids.remove(user_id)
            with open('new_ids.txt', 'w') as new_f:
                for user_id in new_ids:
                    new_f.write(user_id + '\n')

            with open('old_ids.txt', 'w') as old_f:
                for user_id in old_ids:
                    old_f.write(user_id + '\n')
                


if __name__ == '__main__':
    main()
