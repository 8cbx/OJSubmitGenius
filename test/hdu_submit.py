#encoding=utf8
import pycurl
import StringIO
c = pycurl.Curl()
b=StringIO.StringIO()
h=open("code.cpp","r")
e=h.read()
h.close()
#print "check=0&problemid=1000&language=0&usercode="+e
c.setopt(pycurl.COOKIEJAR,"cookie.txt")
c.setopt(pycurl.COOKIEFILE,"cookie.txt")
c.setopt(pycurl.URL,'http://acm.hdu.edu.cn/userloginex.php?action=login')
c.setopt(pycurl.POSTFIELDS, "username=testfile&userpass=testfile&login=Sign+In")
c.setopt(pycurl.URL,'http://acm.hdu.edu.cn/submit.php?action=submit')
c.setopt(pycurl.POSTFIELDS, "check=0&problemid=1000&language=0&usercode="+e)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
d= b.getvalue()
print d

