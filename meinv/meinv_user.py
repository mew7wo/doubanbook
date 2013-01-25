#!/usr/bin/env python2.7
#coding=utf-8
#author:mew7wo
#mail:mew7wo@gmail.com
#filename:meinv_user.py
#create time:Tue 18 Dec 2012 02:12:48 PM CST

import urllib2
import urllib
import sys
import cookielib
from lxml import etree


url = 'http://www.douban.com/photos/album/64180843/?start=%d'
url_xpath = '//*[@id="content"]/div[3]/div[1]/div[2]/div[@class="photo_wrap"]/a'
login_url = 'http://www.douban.com/accounts/login'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) Chrome/23.0.1271.64 Safari/537.11'}
post_data = urllib.urlencode({'form_email':'1398882926@qq.com', 'form_passowrd':'liumengchao'})
step = 18

def installOpener():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

def login():
    login_req = urllib2.Request(login_url, headers=headers) 
    try:
        login_result = urllib2.urlopen(login_req, data = post_data)
    except Exception, e:
        print str(e)
        sys.exit(1)
    print 'login success'
    
def getUrls(content):
    mv_urls = set()
    root = etree.HTML(content)
    urls = root.xpath(url_xpath)

    for u in urls:
        mv_urls.add(u.get('href'))

    return mv_urls


def main():
    installOpener() 
    login()

    index = 0
    meinv_urls = set()

    for i in range(30):
        req_url = url % index
        index += step
        try:
            req = urllib2.Request(req_url)
            content = urllib2.urlopen(req).read()
        except Exception, e:
            print req_url
            print str(e)
            continue

        urls = getUrls(content)
        meinv_urls = meinv_urls.union(urls)

    with open('meinv_url.txt', 'w') as f:
        for mv_url in meinv_urls:
            f.write(mv_url + '\n')


if __name__ == '__main__':
    print 'begin...'
    main()
    print 'end...'

