#!/usr/bin/python
# -*- coding: utf-8 -*-
import cookielib;
import urllib;
import urllib2;
import optparse;
import hdu_login
import hdu_submit
hdu_login.TryLogin('testfile','testfile')
hdu_submit.SendCode("code.cpp",1000,0)

