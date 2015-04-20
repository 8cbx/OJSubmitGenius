#encoding=utf8
import pycurl
import StringIO
import urllib
c = pycurl.Curl()
b=StringIO.StringIO()
h=open("code.cpp","r")
e=h.read()
e=urllib.quote(e)
h.close()
#print "check=0&problemid=1000&language=0&usercode="+e
#c.setopt(pycurl.COOKIEJAR,"cookie.txt")
#c.setopt(pycurl.COOKIEFILE,"cookie.txt")
c.setopt(pycurl.URL,'http://poj.org/login')
c.setopt(pycurl.POSTFIELDS, "user_id1=testfile&password1=testfile&B1=login&url=%2F")
c.setopt(pycurl.URL,'http://poj.org/submit')
c.setopt(pycurl.POSTFIELDS, "problem_id=1000&language=0&source="+e)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
d= b.getvalue()
print d

