#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:douban.py
#create time:Tue 20 Nov 2012 08:16:05 PM CST

import urllib2
import urllib
import cookielib
import socket


class DouBan():
    ''' douban spider '''

    
    def __init__(self):
        self.originUrl = ''
        self.loginUrl = 'http://www.douban.com/accounts/login'
        self.opener = urllib2.build_opener()
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'} 

    def __readConfig(self):
        pass

    def login(self, user, pw, cookieFile=None):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        post_data = urllib.urlencode({'form_email':user, 'form_password':pw})
        req = urllib2.Request(self.loginUrl, headers = self.headers)
        
        if cookieFile != None:
            cookieHandler = cookielib.LWPCookieJar(filename=cookieFile)
            try:
                cookieHandler.load(ignore_discard=True, ignore_expires=True)
            except (cookielib.LoadError, IOError):
                cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)
    
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieHandler), httpHandler)

            try:
                resp = self.opener.open(req, data=post_data)
            except (urllib2.URLError, socket.timeout):
                raise urllib2.URLError()
            cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)
                
        else:
            cj = cookielib.CookieJar()
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), httpHandler)
            try:
                resp = self.opener.open(req, data=post_data)
            except (urllib2.URLError, socket.timeout):
                raise urllib2.URLError()
        

    def __getPage(self, url):
        try:
            req = urllib2.Request(url, headers=self.headers)
            content = self.opener.open(req).read()
            return content
        except (urllib2.URLError, socket.timeout):
            raise urllib2.URLError()
            

    def __getUrls(self, page):
        pass

    def run(self):
        pass
