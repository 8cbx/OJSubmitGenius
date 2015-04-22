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
    PojMainUrl = "http://poj.org";    
    header={ 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16'}
    PojMainSubmitUrl = "http://poj.org/submit";
    postDict = {
            'problem_id'     : problemid,
	    'language'      : language,
	    'source'      : str(e),
        };
    postData = urllib.urlencode(postDict);
    req = urllib2.Request(PojMainSubmitUrl, postData, header);
    req.add_header('Content-Type', "application/x-www-form-urlencoded");
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    print "respHtml=",respHtml;
