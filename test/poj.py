#!/usr/bin/python
# -*- coding: utf-8 -*-
import cookielib;
import urllib;
import urllib2;
import optparse;
import poj_login
import poj_submit
poj_login.TryLogin('testfile','testfile')
poj_submit.SendCode("code.cpp",1000,0)

