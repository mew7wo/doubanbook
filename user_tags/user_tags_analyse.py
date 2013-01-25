#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:user_tags_analyse.py
#create time:Wed 19 Dec 2012 08:15:14 PM CST


import json

def cmp(x, y):
    if x[1]>y[1]: return -1
    elif x[1] == y[1]: return 0
    else: return 1


def countTags():
    tags_count = {}
    tags_count_all = {}
    with open('user_filtered_tags.txt', 'r') as f:
        for line in f:
            json_obj = json.loads(line.rstrip('\n'))
            for tag in json_obj['tags']:
                title = tag['title'] 
                count = int(tag['count'])
                tags_count.setdefault(title, 0)
                tags_count[title] += 1
                
                tags_count_all.setdefault(title, 0)
                tags_count_all[title] += count



    with open('tags_analyse.txt', 'w') as f:
        tags_list = [(tag.encode('utf-8'), tags_count[tag]) for tag in tags_count]
        tags_list.sort(cmp)
        for tag in tags_list:
            f.write('%s %d\n' % tag )

    with open('tags_analyse_all.txt', 'w') as f:
        tags_list = [(tag.encode('utf-8'), tags_count_all[tag]) for tag in tags_count_all]
        tags_list.sort(cmp)
        for tag in tags_list:
            f.write('%s %d\n' % tag)


def main():
    countTags() 


if __name__ == '__main__':
    print 'begin....'
    main()
    print 'end....'
