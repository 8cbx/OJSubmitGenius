#!/usr/bin/python
# -*- coding: utf-8 -*-
import re;
import cookielib;
import urllib;
import urllib2;
import optparse;
def TryLogin(username,userpass):
    HduMainUrl = "http://acm.hdu.edu.cn/";    
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    header={ 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16'}
    urllib2.install_opener(opener);
    req = urllib2.Request(HduMainUrl,None, header)
    resp = urllib2.urlopen(req);
    for index, cookie in enumerate(cj):
        print '[',index, ']',cookie;
    HduMainLoginUrl = "http://acm.hdu.edu.cn/userloginex.php?action=login";
    postDict = {
            'username'      : username,
            'userpass'      : userpass,
	    'login'         : 'Sign+In',
        };
    postData = urllib.urlencode(postDict);
    req = urllib2.Request(HduMainLoginUrl, postData, header);
    req.add_header('Content-Type', "application/x-www-form-urlencoded");
    resp = urllib2.urlopen(req);
    #respHtml = resp.read();
    #print "respHtml=",respHtml;
