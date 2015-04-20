#encoding=utf8
import pycurl
import StringIO
c = pycurl.Curl()
b=StringIO.StringIO()
c.setopt(pycurl.URL,'http://acm.hdu.edu.cn/userloginex.php?action=login')
#c.setopt(pycurl.COOKIEJAR,'cookies.txt')
#c.setopt(pycurl.COOKIEFILE,'cookies.txt')
c.setopt(pycurl.POSTFIELDS, "username=testfile&userpass=testfile&login=Sign+In")
c.setopt(pycurl.URL,'http://acm.hdu.edu.cn/')
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
d= b.getvalue()
print d

