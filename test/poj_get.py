#encoding=utf8
import pycurl
import StringIO
import urllib
import sys
import httplib2
import HTMLParser
flag = 0
index = 'http://poj.org/'
picin = 0
flagofsmall = 0
def getPageContent(url):
    headers = {'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)', 'cache-control':'no-cache'}    
    local=urllib.urlopen(url).read()
    return local 
   
class stack:
    def __init__(self,size = 100, list = None):
        self.contain = []
        self.msize = size
        self.top = 0;
    def getTop(self):
    	if self.top > 0 :
    		return self.contain[self.top-1]
    	else:
    		return None
    def getLength(self):
    	return len(self.contain)
    def push(self,data):
    	if self.top == self.msize:
    		return -1
    	self.contain.append(data)
    	self.top = self.top+1
    def pop(self):
    	try:
    		res = self.contain.pop()
    		if self.top > 0:
    			self.top = self.top-1
    		return res;
    	except IndexError:
    		return None

class DealWithPages(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.st=stack(size=1000)
		self.st.push('over')
	def handle_starttag(self,tag,attrs):
		stack_size = self.st.getLength()
		#print tag
		global flag
		global index
		global picin
		if tag == 'tt':
			flag = 2
		if tag == 'i':
			flag = 2
		if tag == 'sup':
			flag = 2
		if stack_size == 1 and tag == 'div':
			for name,value in attrs:
				if name == 'class' and value == 'ptt':
					picin = 1
					self.st.push('div')
					break
		if stack_size == 1 and tag == 'div':
			for name,value in attrs:
				if name == 'class' and value == 'plm':
					picin = 1
					self.st.push('div')
					break
		if stack_size == 1 and tag == 'p':
			for name,value in attrs:
				if name == 'class' and value == 'pst':
					picin = 1
					self.st.push('div')
					break
		if stack_size == 1 and tag == 'div':
			for name,value in attrs:
				if name == 'class' and value == 'ptx':
					picin = 1
					self.st.push('div')
					break
		if stack_size == 1 and tag == 'div':
			for name,value in attrs:
				if name == 'class' and value == 'sio':
					picin = 1
					self.st.push('div')
					break
		if tag == 'img' and picin == 1:
			print '<img ',
			for name,value in attrs:
				print name,
				if name == 'src':
					print '="'+index+value+'"',
				else:
					print '='+value,
					print '/>',
	def handle_data(self, data):
		global flag
		global flagofsmall
		#print flagofsmall,
		stack_size = self.st.getLength()
		if data == '<':
			print '\b'+data,
			flagofsmall = 1
		else:
			if stack_size == 2 and flag == 1:
				flag = flag-1
				print data,
			else:
				if stack_size == 2 and flag == 2:
					print data,
				else:
					if stack_size == 2 and flag == 0:
						if flagofsmall == 0:
							print '\n'
						print data,
			if flagofsmall == 1:
				flagofsmall = 0
		
	def handle_endtag(self, tag):
		global flag
		global picin
		stack_size = self.st.getLength()
		stack_tag = self.st.getTop()
		if tag == 'tt':
			flag = flag-1
		if tag == 'i':
			flag = flag-1
		if tag == 'sup':
			flag = flag-1
		if 'div' == tag and 'div' == stack_tag:
			self.st.pop()
			picin = 0

if __name__ == '__main__':
	for num in range(1001,1002):
		page = getPageContent('http://poj.org/problem?id='+str(num))
		#print page
		print '\n'+str(num)
		my=DealWithPages()
		my.feed(page)
