#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:user_filter.py
#create time:Fri 25 Jan 2013 03:51:32 PM CST

import json

#return set()
def readTags(fileName):
    tags = set()
    with open(fileName, 'r') as f:
        for line in f:
            tags.add(line.rstrip('\n').decode('utf-8'))

    return tags

def main():
    users = set()
    with open('./data_sets/user_filtered_tags.txt', 'r') as f:
        tags = readTags('./data_sets/douban_computer_tags.txt')
        for line in f:
            user = json.loads(line.rstrip('\n'))
            user_tags = [tag['title'] for tag in user['tags']]
            for tag in user_tags:
                if tag not in tags:
                    continue
                users.add(user['id'])
                break
    with open('./data_sets/seed_user.txt', 'a+') as f:
        for user in users:
            f.write('%s\n' %  user.encode('utf-8'))



if __name__ == '__main__':
    print 'begin...'
    main()
    print 'end... '
