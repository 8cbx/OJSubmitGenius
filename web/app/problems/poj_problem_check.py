#encoding=utf8
import urllib
import sys
import httplib2
import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
flag = 0
index = 'http://poj.org/'
picin = 0
flagofsmall = 0
Data=''
havei=0
coun=0
fp = open("detals.txt","w")
havebeenprint=0
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
		global coun
		global havei
		stack_size = self.st.getLength()
		if stack_size == 1 and tag == 'tr':
			for name,value in attrs:
				if name == 'align' and value == 'center':
					self.st.push('tr')
					break
		if tag == 'i' or tag == 'sup':
			coun=coun-2
			havei=2
			#fp.write('------\n')
	def handle_data(self, data):
		global Data
		global coun
		global fp
		global havebeenprint
		global havei
		#print '----'+data+'------'
		data=data.replace(',','\.\..')
		stack_size = self.st.getLength()
		#print stack_size
		#print coun
		if stack_size == 2:
			if data=='&':
				Data = Data + data
				coun=coun-1
			elif coun!=7:
				if coun==0 or coun == 3:
					#fp.write(str(coun)+'\n')
					if coun == 3 :
						Data =  Data + ','
					Data = Data + data
					#if havei==0:
						#Data = Data + ','
					#else:
						#havei = havei - 1
				if coun==1:
					#fp.write(str(coun)+' '+str(havei)+'\n')
					if havei==0:
						Data =  Data + ','
					else:
						havei = havei - 1
					Data = Data +data 
				if coun==-1:
					#fp.write(str(coun)+' '+str(havei)+'\n')
					Data =  Data + '!!!!'
					havei = havei - 1
					coun=coun+1
					Data = Data +data 
				if coun == 5:
					#fp.write(str(coun)+'\n')
					Data = Data + ',' +data
				coun=coun+1;
			else:
				fp.write(Data+'\n')	
				havebeenprint=1
				havei=0
				Data=''
				coun=0;
	def handle_endtag(self, tag):
		global flag
		global picin
		global coun
		global havei
		stack_size = self.st.getLength()
		stack_tag = self.st.getTop()
		if 'tr' == tag and 'tr' == stack_tag:
			self.st.pop()
		#if tag == 'i':
			#coun=coun-2
			#havei=2
			#fp.write('------\n')
			
if __name__ == '__main__':
	for i in range(1,2):
		havebeenprint=0
		havei=0
		page = getPageContent('http://poj.org/problemlist?volume='+str(i))
		#print '\n'+str(num)
		html_parser = HTMLParser.HTMLParser()
		page = html_parser.unescape(page)
		#print page
		my=DealWithPages()
		my.feed(page)
		if havebeenprint==0:
			break;
