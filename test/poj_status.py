#encoding=utf8
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
		if stack_size == 1 and tag == 'tr':
			for name,value in attrs:
				if name == 'align' and value == 'center':
					self.st.push('tr')
					break
	def handle_data(self, data):
		stack_size = self.st.getLength()
		if stack_size == 2:
				print data
	def handle_endtag(self, tag):
		global flag
		global picin
		stack_size = self.st.getLength()
		stack_tag = self.st.getTop()
		if 'tr' == tag and 'tr' == stack_tag:
			self.st.pop()

if __name__ == '__main__':
	for num in range(1000,1001):
		user='testfile'
		page = getPageContent('http://poj.org/status?problem_id='+str(num)+'&user_id='+user+'&result=&language=')
		my=DealWithPages()
		my.feed(page)
