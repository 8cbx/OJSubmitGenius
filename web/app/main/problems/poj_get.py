#-*- coding: utf-8 -*-
#encoding=utf8
import MySQLdb
import urllib
import sys
import httplib2
import HTMLParser
import sys
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
flag = 0
index = 'http://poj.org/'
picin = 0
flagofsmall = 0
Data=""
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
		global Data
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
			#print '<img ',
			Data = Data + '<img '
			for name,value in attrs:
				#print name,
				Data = Data + name
				if name == 'src':
					#print '="'+index+value+'"',
					Data = Data + '="'+index+value+'"'+ '/>'
				else:
					#print '='+value,
					#print '/>',
					Data = Data +'='+value + '/>'
	def handle_data(self, data):
		global flag
		global flagofsmall
		global Data
		#print flagofsmall,
		stack_size = self.st.getLength()
		if data == '<':
			#print '\b'+data,
			data=data.strip()
			Data = Data + '\b'+data
			flagofsmall = 1
		else:
			if stack_size == 2 and flag == 1:
				flag = flag-1
				#print data,
				data=data.strip()
				Data = Data+ data
			else:
				if stack_size == 2 and flag == 2:
					#print data,
					data=data.strip()
					Data = Data + data
				else:
					if stack_size == 2 and flag == 0:
						if flagofsmall == 0:
							#print '\n'
							Data = Data + '\n'
						#print data,
						data=data.strip()
						Data = Data + data
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
def db_add(data,num):
	#values=[num]
	fp2=open('POJ_'+str(num),'w')
	fp2.write("-PID-\n"+str(num)+'\n')
	begin=data.find('Time Limit:',0,len(data))
	#print begin
	current=data[1:int(begin-1)]
	fp2.write("-Title:-\n"+current+'\n')
	data=data[(begin+12):]
	#values.append(current)
	begin=data.find('Memory Limit:',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Time Limit:-\n'+current+'\n')
	data=data[(begin+14):]
	#values.append(current)
	begin=data.find('Total Submissions:',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Memory Limit:-\n'+current+'\n')
	data=data[(begin+19):]
	#values.append(current)
	begin=data.find('Accepted:',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Total Submissions:-\n'+current+'\n')
	data=data[(begin+10):]
	#values.append(int(current))
	begin=data.find('Description',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Accepted:-\n'+current+'\n')
	data=data[(begin+12):]
	#values.append(int(current))
	begin=data.find('Input',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Description:-\n'+current+'\n')
	data=data[(begin+6):]
	#values.append(current)
	begin=data.find('Output',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Input:-\n'+current+'\n')
	data=data[(begin+7):]
	#values.append(current)
	begin=data.find('Sample Input',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Output:-\n'+current+'\n')
	data=data[(begin+13):]
	#values.append(current)
	begin=data.find('Sample Output',0,len(data))
	current=data[0:int(begin-1)]
	fp2.write('-Sample Input:-\n'+current+'\n')
	data=data[(begin+14):]
	#values.append(current)
	begin=data.find('Hint',0,len(data))
	if begin==-1:
		begin=data.find('Source',0,len(data))
		current=data[0:int(begin-1)]
		fp2.write('-Sample Output:-\n'+current+'\n')
		#data=data[(begin+5):]
		#values.append(current)
		fp2.write('-Hint:-\n'+'\n')
		begin=data.find('Source',0,len(data))
		#current=data[0:int(begin-1)]
		data=data[(begin+7):]
		fp2.write('-Source:-\n'+data+'\n')
	else :
		current=data[0:int(begin-1)]
		fp2.write('-Sample Output:-\n'+current+'\n')
		data=data[(begin+5):]
		#values.append(current)
		begin=data.find('Source',0,len(data))
		current=data[0:int(begin-1)]
		fp2.write('-Hint:-\n'+current+'\n')
		data=data[(begin+7):]
		#values.append(current)
		fp2.write('-Source:-\n'+data+'\n')
	#values.append(data)
	#print values
	fp2.close()

if __name__ == '__main__':
	fp = open("detals.txt","r")
	conn=MySQLdb.connect(host='46.101.10.209',user='root',passwd='123456',port=3306,db='test',charset='utf8')
	cur=conn.cursor()
	cur.execute("alter table problems default character set utf8;")
	conn.commit()
	arr=fp.readlines()
	for lines in arr:
		#values=[]
		values = lines.replace("\n","").split(",")
		#values.append(lines)
		print values
		print values[0]
		print values[1].encode("utf-8")
		now = datetime.utcnow()
		cur.execute('insert into problems (PID,OJ_ID,Title,Total_Submissions,Accepted,LastUpdate) values(%s,%s,%s,%s,%s,%s);',(values[0],'POJ',values[1].encode("utf-8"),values[2],values[3],now))
		conn.commit()
		page = getPageContent('http://poj.org/problem?id='+str(values[0]))
		while page.find("Error Occurred")!=-1 and page.find("The page is temporarily unavailable")!=-1:
			page = getPageContent('http://poj.org/problem?id='+str(values[0]))
		#print page
		#print '\n'+str(num)
		Data=""
		my=DealWithPages()
		my.feed(page)
		db_add(Data,values[0])
		arr=fp.readline()
		#print "Data :\n"+Data
	fp.close()
	conn.close()
	cur.close()
