#encoding=utf8
import urllib
import sys
import httplib2
import HTMLParser
from ..models import Code_detail
flag = 0
index = 'http://poj.org/'
picin = 0
flagofsmall = 0
Data1=[]
Data=[]
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
		global Data1
		global Data
		#print data
		stack_size = self.st.getLength()
		if stack_size == 2:
			#print data
			if data=='Presentation Error' or data=='Time Limit Exceeded' or data=='Memory Limit Exceeded' or data=='Wrong Answer' or data=='Runtime Error' or data=='Output Limit Exceeded' or data=='Compile Error' or data=='Compiling' or data=='Running & Judging':
				Data1.append(data)
				Data1.append(' ')
				Data1.append(' ')
			elif len(Data1)==9:
				Data.append(Data1)
				#print Data
				Data1=[]
				Data1.append(data)
			else:
				Data1.append(data)
	def handle_endtag(self, tag):
		global flag
		global picin
		stack_size = self.st.getLength()
		stack_tag = self.st.getTop()
		if 'tr' == tag and 'tr' == stack_tag:
			self.st.pop()

def SaveCEfile(filename,RID):
	fp1=open(str(filename),'w')
	page = getPageContent('http://poj.org/showcompileinfo?solution_id='+str(RID))
	while page.find("Error Occurred")!=-1 and page.find("The page is temporarily unavailable")!=-1:
		page = getPageContent('http://poj.org/showcompileinfo?solution_id='+str(RID))
	beg=page.find('<pre>')
	end=page.find('</pre>')
	page=page[(beg+5):(end)]
	fp1.write(page)
	fp1.close()

def GetStatus(user,code,language):
	global Data
	global Data1
	Data=[]
	Data1=[]
	#print code.PID
	page = getPageContent('http://poj.org/status?problem_id='+str(code.PID)+'&user_id='+user+'&result=&language='+str(language))
	while page.find("Error Occurred")!=-1 and page.find("The page is temporarily unavailable")!=-1:
		page = getPageContent('http://poj.org/status?problem_id='+str(code.PID)+'&user_id='+user+'&result=&language=')
	#print page
	#print '\n'+str(num)
	my=DealWithPages()
	my.feed(page)
	#print Data
	Data.append(Data1)
	#print Data[0][3]
	#print Data1
	while (Data[0][3]=='Compiling' or Data[0][3]=='Running '):
		Data=[]
		Data1=[]
		page = getPageContent('http://poj.org/status?problem_id='+str(code.PID)+'&user_id='+user+'&result=&language='+str(language))
		while page.find("Error Occurred")!=-1 and page.find("The page is temporarily unavailable")!=-1:
			page = getPageContent('http://poj.org/status?problem_id='+str(code.PID)+'&user_id='+user+'&result=&language=')
		my=DealWithPages()
		my.feed(page)
		Data.append(Data1)
	code.OJ_ID='POJ'
	code.PID = int(Data[0][2])		
	code.Result=Data[0][3]
	code.Memory=Data[0][4]
	code.Time=Data[0][5]
	code.Language=Data[0][6]
	code.Code_Length=Data[0][7]
	code.CEfile=''
	code.RemoteID=Data[0][0]
	#print Data[0]
	if Data[0][3]=="Compile Error":
		SaveCEfile('./app/main/POJCEfile/POJ_'+str(code.PID)+str(Data[0][0]),Data[0][0])
		code.CEfile='POJ_'+str(code.PID)+str(Data[0][0])
	return code
