#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:fetch.py
#create time:Wed 28 Nov 2012 02:20:12 PM CST

import urllib2
import urllib
import cookielib
import socket


class Fetch(object):
    ''' url fetch class '''
    def __init__(self):
        self._headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) Chrome/23.0.1271.64 Safari/537.11'}
        self.__login()

    def __login(self):
        http_handler = urllib2.HTTPHandler(debuglevel=1)
        cj = cookielib.CookieJar()
        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), http_handler)

        post_data = urllib.urlencode({'form_email':'1398882026@qq.com', 'form_password':'liumengchao'})
        login_url = 'http://www.douban.com/accounts/login'
        login_req = urllib2.Request(login_url, data=post_data, headers=self._headers)
        login_resp = self.__get(login_req)
        if login_resp.getcode() != '200':
            raise LoginError()
            
    def __get(self, req):
        content = None
        try:
            content = self._opener.open(req) 
        except (urllib2.URLError, socket.timeout), e:
            print repr(e)
        return content

    def get(self, url):
        req = urllib2.Request(url, headers=self._headers)
        content = self.__get(req).read()
        return content
        

class LoginError(object):
    def __init__(self, msg=None):
        self.msg = msg

