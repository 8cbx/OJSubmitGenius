#!/usr/bin/python
# -*- coding: utf-8 -*-
import re;
import cookielib;
import urllib;
import urllib2;
import optparse;
def TryLogin(username,userpass):
    PojMainUrl = "http://poj.org";    
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    header={ 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16'}
    urllib2.install_opener(opener);
    req = urllib2.Request(PojMainUrl,None, header)
    resp = urllib2.urlopen(req);
    #for index, cookie in enumerate(cj):
       # print '[',index, ']',cookie;
    PojMainLoginUrl = "http://poj.org/login";
    postDict = {
            'user_id1'      : username,
            'password1'      : userpass,
	     'B1'           :'login',
	    'url'           : '%2F',
        };
    postData = urllib.urlencode(postDict);
    req = urllib2.Request(PojMainLoginUrl, postData, header);
    req.add_header('Content-Type', "application/x-www-form-urlencoded");
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    if respHtml.find('userstatus?user_id='+str(username))!=-1:
    	return 1
    else:
    	return 0
