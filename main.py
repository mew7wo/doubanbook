#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:main.py
#create time:Tue 27 Nov 2012 04:01:23 PM CST


from data_fetch.douban_user import DouBanUser

def main():
    db = DouBanUser()
    db.login('douban_cookie')
    try:
        db.run()
    except KeyboardInterrupt:
        print 'ctrl - c'
    except Exception, e:
        print repr(e)


if __name__ == '__main__':
    print 'begin ....'
    main()
    print 'end ....'
