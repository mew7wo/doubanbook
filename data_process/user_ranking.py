#!/usr/bin/env python
#coding:utf-8


import json
def cmp(a, b):
    return b[1] - a[1]

def main():
    user_rank = {}
    with open('../data_sets/seed_user_rel.txt', 'r') as f:
        for line in f:
            user_rel = json.loads(line.rstrip('\n'))
            for user in user_rel['followed']:
                user_rank.setdefault(user, 1)
                user_rank[user] += 1
    user_list = user_rank.items()
    user_list.sort(cmp)
    print user_list[:10]


if __name__ == '__main__':
    main()
