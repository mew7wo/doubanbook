#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:tags_filter.py
#create time:Wed 19 Dec 2012 07:45:19 PM CST

import json

def main():
    json_out_file = open('user_filtered_tags.txt', 'a+')

    with open('/home/mew7wo/Downloads/user_tags.txt', 'r') as f:
        for line in f:
            json_obj = json.loads(line.rstrip('\n'))
            if json_obj['tags'] != None and len(json_obj['tags']) != 0:
                json_str = json.dumps(json_obj)
                json_out_file.write(json_str + '\n')
                
    json_out_file.close()

if __name__ == '__main__':
    print 'begin...'
    main()
    print 'end...'
