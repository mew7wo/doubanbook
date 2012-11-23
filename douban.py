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
from lxml import etree
from time import sleep


class DouBan():
    ''' douban spider '''
    
    def __init__(self):
        self._new_urls = set()
        self._old_urls = set()
        self._opener = urllib2.build_opener()
        self._headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'} 
        self.__readConfig()

    def __readConfig(self):
        with open(r'./config/config.xml', 'r') as f:
            content = f.read()
            root = etree.XML(content)
            self._login_url = root.xpath('/douban/login_url/text()')[0]
            self._new_urls.add(root.xpath('/douban/begin_url/text()')[0])
            self._user = root.xpath('/douban/user/text()')[0]
            self._password = root.xpath('/douban/password/text()')[0]
            self._depth = int(root.xpath('/douban/depth/text()')[0])
            self._threads = int(root.xpath('/douban/threads/text()')[0])
            self._speed = int(root.xpath('/douban/speed/text()')[0])


    def login(self, cookieFile=None):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        post_data = urllib.urlencode({'form_email':self._user, 'form_password':self._password})
        req = urllib2.Request(self._login_url, headers = self._headers)
        
        if cookieFile != None:
            cookieHandler = cookielib.LWPCookieJar(filename=cookieFile)
            try:
                cookieHandler.load(ignore_discard=True, ignore_expires=True)
            except (cookielib.LoadError, IOError):
                cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)
    
            self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieHandler), httpHandler)

            try:
                resp = self._opener.open(req, data=post_data)
            except (urllib2.URLError, socket.timeout):
                raise urllib2.URLError()
            cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)
                
        else:
            cj = cookielib.CookieJar()
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), httpHandler)
            try:
                resp = self._opener.open(req, data=post_data)
            except (urllib2.URLError, socket.timeout):
                raise urllib2.URLError()
        

    def __getPage(self, url):
        try:
            req = urllib2.Request(url, headers=self._headers)
            content = self._opener.open(req).read()
            return content
        except (urllib2.URLError, socket.timeout):
            raise urllib2.URLError()
            

    # //*[@id="content"]/div/div[1]/div[3]/dl/dt/a/@href
    def __getUrls(self, page):
        root = etree.HTML(page)
        urls = root.xpath('//*[@id="content"]/div/div[1]/div[3]/dl/dt/a/@href')
        new_urls = set()
        for url in urls:
            if url != None:
                new_urls.add(url)
        return new_urls


    def run(self):
        for i in range(self._depth):
            new_urls = set()
            for url in self._new_urls:
                print url
                if url not in self._old_urls:
                    sleep(60/self._speed)
                    page = self.__getPage(url)
                    urls = self.__getUrls(page)
                    new_urls = new_urls.union(urls)
                    self._old_urls.add(url)
            self._new_urls = self._new_urls.union(new_urls)

