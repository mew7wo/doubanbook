#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:test.py
#create time:Tue 18 Dec 2012 08:29:11 PM CST

from meinv_user import login
from meinv_user import installOpener

def main():
    installOpener()
    login()


if __name__ == '__main__':
    main()
