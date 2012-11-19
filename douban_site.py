#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:douban_site.py
#create time:Mon 19 Nov 2012 06:59:23 PM CST

import urllib2
import urllib
import cookielib
import sys
import socket
from bs4 import BeautifulSoup


newUser = set()
oldUser = set()
cookieFile = r'/home/mew7wo/douban/douban_cookie'
newUser.add('http://www.douban.com/people/ecqzone/')


def login():
    loginMsg = urllib.urlencode({'form_email':'1398882026@qq.com', 'form_password':'liumengchao'})
    loginUrl = 'http://www.douban.com/accounts/login'
    
    cookieHandler =cookielib.LWPCookieJar(filename=cookieFile)
    try:
        cookieHandler.load(ignore_discard=True, ignore_expires=True)
    except Exception, e:
        print repr(e)
        cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)
    
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieHandler), httpHandler)
    urllib2.install_opener(opener)
    
    try:
        loginReq = urllib2.Request(url=loginUrl, data=loginMsg)
        resp = opener.open(loginReq)
    except:
        print 'login error'
        print resp.headers
        sys.exit()
        
    cookieHandler.save(cookieFile, ignore_discard=True, ignore_expires=True)
    print 'login success...'
    
def loadCookie():
    cookieHandler = cookielib.LWPCookieJar(filename=cookieFile)
    try:
        cookieHandler.load(ignore_discard=True, ignore_expires=True)
    except (cookielib.LoadError, IOError):
        raise cookielib.LoadError()

    return cookieHandler
    
def getPage(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        req = urllib2.Request(url, headers=headers)
        content = urllib2.urlopen(req).read()
    except (urllib2.URLError, socket.timeout):
        raise urllib2.URLError()

    return content

def getUrls(page):
    urls = set()
    soup = BeautifulSoup(page.decode('utf-8'), 'lxml')
    nbgs = soup.find_all('a', {'class':'nbg'})
    print len(nbgs)
    for i in nbgs:
        href = i.get('href')
        if href != None:
            urls.add(href)
        
    return urls  

def main():
    #login()
    cookieHandler = loadCookie()
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieHandler), httpHandler)
    urllib2.install_opener(opener)
    
    host = 'http://www.douban.com/people/ecqzone/contacts'
    page = getPage(host)
    urls = getUrls(page)
    for i in urls:
        print '%s\n' % i

if __name__ == '__main__':
    print 'begin...'
    main()
    print 'end....'

