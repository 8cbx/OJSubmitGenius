#encoding=utf8
import pycurl
import StringIO
import urllib
import poj_login
poj_login.login()
b=StringIO.StringIO()
h=open("code.cpp","r")
e=h.read()
e=urllib.quote(e)
h.close()
c=pycurl.Curl()
c.setopt(pycurl.URL,'http://poj.org/submit')
c.setopt(pycurl.POSTFIELDS, "problem_id=1000&language=0&source="+e)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
d= b.getvalue()
print d

