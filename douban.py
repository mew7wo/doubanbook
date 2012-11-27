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
        self._headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) Chrome/23.0.1271.64 Safari/537.11'} 
        self.__readConfig()

        with open('old_urls', 'r') as f:
            for url in f:
                self._old_urls.add(url.rstrip('\n'))

        with open('new_urls', 'r') as f:
            for url in f:
                self._new_urls.add(url.rstrip('\n'))


    def __readConfig(self):
        with open('./config/config.xml', 'r') as f:
            content = f.read()
            root = etree.XML(content)
            self._login_url = root.xpath('/douban/login_url/text()')[0]
            self._user = root.xpath('/douban/user/text()')[0]
            self._password = root.xpath('/douban/password/text()')[0]
            self._depth = int(root.xpath('/douban/depth/text()')[0])

     
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
            self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), httpHandler)
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
            
    def __urlValid(self, url):
        if url == None: return False
        return True

    # //*[@id="content"]/div/div[1]/div[3]/dl/dt/a/@href
    def __getUrls(self, page):
        root = etree.HTML(page)
        urls = root.xpath('//*[@id="content"]/div/div[1]/div[3]/dl/dt/a/@href')
        new_urls = set()
        for url in urls:
            if self.__urlValid(url):
                new_urls.add(url)
        return new_urls


    def persistent(self):
        with open(r'new_urls', 'w') as f:
            for url in self._new_urls:
                f.write(url + '\n')

        with open(r'old_urls', 'w') as f:
            for url in self._old_urls:
                f.write(url + '\n')


    def run(self):
        for i in range(self._depth):
            new_urls = set()
            for url in self._new_urls:
                print '================================== %d ==================================' % i
                if url not in self._old_urls:
                    sleep(2)
                    page = self.__getPage(url + 'contacts')
                    urls = self.__getUrls(page)
                    new_urls = new_urls.union(urls)
                    self._old_urls.add(url)
            self._new_urls = new_urls

