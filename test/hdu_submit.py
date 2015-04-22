#!/usr/bin/python
# -*- coding: utf-8 -*-
import re;
import cookielib;
import urllib;
import urllib2;
import optparse;
def SendCode(code,problemid,language):
    h=open(code,"r")
    e=h.read()
    #e=urllib.quote(e)
    h.close()
    HduMainUrl = "http://acm.hdu.edu.cn/";    
    header={ 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16'}
    HduMainSubmitUrl = "http://acm.hdu.edu.cn/submit.php?action=submit";
    postDict = {
            'check'         : '0',
            'problemid'     : problemid,
	    'language'      : language,
	    'usercode'      : str(e),
        };
    postData = urllib.urlencode(postDict);
    req = urllib2.Request(HduMainSubmitUrl, postData, header);
    req.add_header('Content-Type', "application/x-www-form-urlencoded");
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    print "respHtml=",respHtml;
