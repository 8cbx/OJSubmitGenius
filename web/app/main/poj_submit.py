#!/usr/bin/python
# -*- coding: utf-8 -*-
import re;
import cookielib;
import urllib;
import urllib2;
import optparse;
import base64
def Submit(code,problemid,language):
	PojMainUrl = "http://poj.org";    
	header={ 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.16) Gecko/20130319 Firefox/3.6.16'}
	PojMainSubmitUrl = "http://poj.org/submit";
	code=base64.b64encode(code)
	postDict = {
            'problem_id'     : problemid,
	    'language'      : language,
	    'source'      : str(code),
	    'submit'    :'Submit',
	    'encoded'   : '1'
        };
	postData = urllib.urlencode(postDict);
	#print postData
	req = urllib2.Request(PojMainSubmitUrl, postData, header);
	#print req
	#print "------------------"
	req.add_header('Content-Type', "application/x-www-form-urlencoded");
	resp = urllib2.urlopen(req);
	#respHtml = resp.read();
	#print "respHtml=",respHtml;
