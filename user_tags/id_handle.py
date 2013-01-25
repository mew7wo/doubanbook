#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:id_handle.py
#create time:Fri 30 Nov 2012 12:29:32 PM CST

import json


def main():
    get_tags_ids = set()
    new_ids = set()
    old_ids = set()


    with open('user_tags.txt', 'r') as f:
        for line in f:
            tags_json = line.rstrip('\n')
            tags_obj = json.loads(tags_json)
            get_tags_ids.add(tags_obj['id'])

    with open('new_ids.txt', 'r') as f:
        for line in f:
            new_ids.add(line.rstrip('\n'))

        for user_id in get_tags_ids:
            if user_id in new_ids:
                new_ids.remove(user_id)

    with open('new_ids.txt', 'w') as f:
        for user_id in new_ids:
            f.write(user_id + '\n')

    with open('old_ids.txt', 'w') as f:
        for user_id in get_tags_ids:
            f.write(user_id + '\n') 

        
if __name__ == '__main__':
    main()
