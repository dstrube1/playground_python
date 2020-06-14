#emailScraper
#get emails of doctors at Emory, Grady, small atlanta clinics, etc

#started here:
#https://medium.com/swlh/how-to-scrape-email-addresses-from-a-website-and-export-to-a-csv-file-c5d1becbd1a0
#then revised to be threaded to catch frozen gets

from bs4 import BeautifulSoup
from collections import deque
import datetime
import pandas as pd
import re
import requests
import sys
import threading
import time
from urllib.parse import urlsplit

original_url = "https://www.gradyhealth.org"
domain = "grady"
baseUrl = "gradyhealth.org"

#original_url = "http://www.emory.edu/coronavirus//"
#domain = "emory"
#baseUrl = "emory.edu"
linkPhase = 1

# to save urls to be scraped
unscraped = deque([original_url])

# to save scraped urls
scraped = set()

# to save fetched emails
emails = set() 

isTimeToBreak = False
timeout = 10.0

#BEGIN Thread class
class MyThread(threading.Thread):
	def __init__(self, url):
		super(MyThread, self).__init__()
		self._stop_event = threading.Event()
		self.url = url
	
	def run(self):
		global isTimeToBreak
		while not self.stopped():
			try:
				if not getInfo(self.url):
					#isTimeToBreak = True
					pass
				return
			except Exception as exception:
				print("Exception caught in MyThread run: " + str(exception))
				isTimeToBreak = True
				return
	
	def stop(self):
		self._stop_event.set()
	
	def stopped(self):
		return self._stop_event.is_set()
#END Thread class

def getTime():
	timeFormat = "%H:%M:%S"
	return datetime.datetime.now().strftime(timeFormat)
	
def getTimeForFile():
	timeFormat = "%H-%M-%S"
	return datetime.datetime.now().strftime(timeFormat)
	
def isLinkGood(link, phase):
	if phase >= 1:
		if ".gz" in link or ".pdf" in link or ".ppt" in link or ".doc" in link:
			return False
		elif ".png" in link or ".jpg" in link or ".mp4" in link:
			return False
	if phase >= 2:
		if "/../" in link or "#" in link or "?" in link or "tel:" in link:
			return False
		elif "\t" in link or "  " in link or "javascript:" in link:
			return False
	if phase >= 3:
		if baseUrl not in link:
			return False
	return True

def getTimeElapsed(_start):
	totalElapsed = int(time.time() - _start)
	hours = int(totalElapsed / (60*60))
	totalElapsed = totalElapsed % (60*60)
	minutes = int(totalElapsed / 60)
	seconds = totalElapsed % 60
	timeElapsed = ""
	if hours > 0:
		timeElapsed += str(hours) + "h"
	if minutes > 0:
		timeElapsed += str(minutes) + "m"
	timeElapsed += str(seconds) + "s"
	return timeElapsed
	

def getInfo(url):
	try:
		# move unsraped_url to scraped_urls set
		scraped.add(url)
		parts = urlsplit(url)
		#SplitResult(scheme='https', netloc='www.google.com', path='/example', query='', fragment='')
		
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		if '/' in parts.path:
			path = url[:url.rfind('/')+1]
		else:
			path = url

		#print("len(unscraped): "+str(len(unscraped))+"; total elapsed: "+'{:.0f}'.format(time.time() - _start)
		#	+" Crawling URL %s" % url) 
		
		print(str(len(unscraped))+"; "+ getTimeElapsed(_start) + "; Crawling URL %s" % url) 
		try:
			response = requests.get(url)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
			# ignore pages with errors and continue with next url
			return True
	
		# You may edit the regular expression as per your requirement
		# re.I: (ignore case)
		new_emails_com = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", 
			response.text, re.I)) 
		new_emails_edu = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.edu", 
			response.text, re.I)) 
		new_emails_gov = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.gov", 
			response.text, re.I)) 
		new_emails_org = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.org", 
			response.text, re.I)) 
		new_emails_net = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.net", 
			response.text, re.I)) 
		
		emails.update(new_emails_com)
		emails.update(new_emails_edu)
		emails.update(new_emails_gov)
		emails.update(new_emails_org)
		emails.update(new_emails_net)
	
		# create a beutiful soup for the html document
		soup = BeautifulSoup(response.text, features="html.parser") 
		print("len(response.text):" + str(len(response.text)))
		print("response.text: " + response.text)
		allLinks = soup.find_all("a")
		print("len(allLinks):" + str(len(allLinks)))
		for anchor in allLinks: 
			# extract linked url from the anchor
			if "href" in anchor.attrs:
				link = anchor.attrs["href"]
			else:
				link = ''
		
			# resolve relative links (starting with /)
			if link.startswith('/'):
				link = base_url + link
		
			elif not link.startswith('http'):
				link = path + link
		
			#if domain in link and isLinkGood(link, linkPhase):
			if link not in unscraped and link not in scraped:
				unscraped.append(link)
	except Exception as exception:
		print("Exception caught in getInfo: "+str(exception))
		return False
	return True

def connectionMonitor(url, thread, timeout):
	if thread.isAlive():
		#print("(" + url + " > " + str(timeout) + "s)")
		thread.stop()
	timer.cancel()

def writeWhatYouGot():
	df = pd.DataFrame(emails, columns=["Email"]) 
	df.to_csv('email_'+domain+'_'+getTimeForFile()+'.txt', index=False, mode='a')
		
#main
def main(args):
	global isTimeToBreak
	global timer
	global _start
	_start = time.time()
	count = 0
	print("size of unscraped; time elapsed; ...")
	while len(unscraped):
		count += 1
		if count > 2:
			break
		url = unscraped.popleft()  # popleft(): Remove and return an element from the left side of the deque
		thread = MyThread(url)
		timer = threading.Timer(timeout, connectionMonitor, kwargs = {"url": url, "thread": thread, "timeout": timeout}) 
		thread.daemon = True
		thread.start()
		timer.start()
		thread.join(timeout)
		if isTimeToBreak:
			break #if a stopping error was encountered, stop
		if thread.is_alive():
			print("Thread joined (at " + getTime() + ") but is still alive. Waiting for it to die (2min limit)", end='', flush=True) 
			waitCount = 0
			while thread.is_alive():
				#wait for the thread to stop running after timeout
				print(".", end='', flush=True)
				waitCount += 1
				if waitCount > 24:
					print(" We've waited over "+str(int(waitCount / 12))+" minute(s) "
						+"for this thread to die. Exiting at " + getTime())
					writeWhatYouGot()
					sys.exit()
				thread.stop()
				time.sleep(5)
			print()

	df = pd.DataFrame(emails, columns=["Email"]) 
	df.to_csv('email_'+domain+'.txt', index=False, mode='a')

if __name__ == '__main__':
    main(sys.argv)