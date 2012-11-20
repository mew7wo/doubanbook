#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:douban.py
#create time:Tue 20 Nov 2012 08:16:05 PM CST

import urllib2
import socket


class DouBan():
    ''' douban spider '''

    
    def __init__(self):
        self.originUrl = ''
        self.loginUrl = ''
        self.opener = urllib2.build_opener()

    def login(self, user, pw, cookieFile=None):
        if cookieFile != None:
            cookieHandler = urllib2.LWPCookieJar(filename=cookieFile)
            try:
                cookieHandler.load(ignore_discard=True, ignore_expires=True)
            except urllib2.LoadError:
                cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)

            self.opener = 
        
        

    def __getPage(self, url):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
            req = urllib2.Request(url, headers=headers)
            content = urllib2.urlopen(req).read()
            return content
        except (urllib2.URLError, socket.timeout):
            raise urllib2.URLError()
            

    def __getUrls(self, page):
        pass
