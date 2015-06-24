#encoding=utf8
import urllib
import sys
import httplib2
import HTMLParser
def getPageContent(url):
    headers = {'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)', 'cache-control':'no-cache'}    
    local=urllib.urlopen(url).read()
    return local 
def POJ_Check():
	page = getPageContent('http://poj.org/status')
	coun=0
	while page.find("Error Occurred")!=-1 and page.find("The page is temporarily unavailable")!=-1 and coun<=5:
		page = getPageContent('http://poj.org/status')
		coun=coun+1
	if coun>5:
		return 0
	if page.count('Presentation Error')+page.count('Time Limit Exceeded')+page.count('Memory Limit Exceeded')+page.count('Wrong Answer')+page.count('Runtime Error')+page.count('Output Limit Exceeded')+page.count('Compile Error')+page.count('Compiling')+page.count('Running & Judging')==0:
		return 0
	return 1
def CheckOjStatus(OJ_ID):
	if OJ_ID=='POJ':
		return POJ_Check()
	
