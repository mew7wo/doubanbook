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


class Fetcher(object):
    ''' url fetch class '''
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) Chrome/23.0.1271.64 Safari/537.11'}
    opener = None
    def __init__(self):
        if self.__class__.opener == None:
            cj = cookielib.CookieJar()
            http_handler = urllib2.HTTPHandler(debuglevel=1)
            self.__class__.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), http_handler)

        self.__login()

    def __login(self):
        post_data = urllib.urlencode({'form_email':'1398882026@qq.com', 'form_password':'liumengchao'})
        login_url = 'http://www.douban.com/accounts/login'
        login_req = urllib2.Request(login_url, data=post_data, headers=self.__class__.headers)
        login_resp = self.__get(login_req)

        if login_resp.getcode() != 200:
            raise LoginError(login_resp.getcode())
            
    def __get(self, req):
        resp = None
        try:
            resp = self.__class__.opener.open(req) 
        except (urllib2.URLError, socket.timeout), e:
            print repr(e)
        finally:
            return resp 

    def get(self, url):
        req = urllib2.Request(url, headers=self.__class__.headers)
        content = self.__get(req).read()
        return content
        

class LoginError(Exception):
    def __init__(self, msg=None):
        self.msg = msg

