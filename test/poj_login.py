#encoding=utf8
import pycurl
import StringIO
def login():
	c = pycurl.Curl()
	b=StringIO.StringIO()
	c.setopt(pycurl.COOKIEJAR,"cookie.txt")
	c.setopt(pycurl.COOKIEFILE,"cookie.txt")
	c.setopt(pycurl.URL,'http://poj.org/login')
	c.setopt(pycurl.POSTFIELDS, "user_id1=testfile&password1=testfile&B1=login&url=%2F")
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.perform()
	c.close()
	d=b.getvalue()
	#print d

