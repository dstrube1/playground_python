# tableScraper.py
# get data from a table in frameset

from bs4 import BeautifulSoup
from collections import deque
import sys
from urllib.parse import urlsplit
import requests

original_url = 'https://my.lifetime.life/'  # "/Users/dstrube/Downloads/makespace/samplepage.html"

# urls to be scraped
unscraped = deque([original_url])

# scraped urls
scraped = set()

#main
def main(args):
	while len(unscraped):
		url = unscraped.popleft()  # popleft(): Remove and return an element from the left side of the deque
		try:
			if not getInfo(url):
				return
		except Exception as exception:
			print('Exception caught : ' + str(exception))
			return

def getInfo(url):
	try:
		# move unsraped_url to scraped_urls set
		scraped.add(url)
		parts = urlsplit(url)
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		if '/' in parts.path:
			path = url[:url.rfind('/')+1]
		else:
			path = url
		
		print(str(len(unscraped))+"; Crawling URL %s" % url) 
		try:
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			response = requests.get(url, headers = headers)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
			# ignore pages with errors and continue with next url
			print('Caught skippable exception in getInfo at call to requests.get')
			return True
		
		# Get page's content data here and do stuff with it
		
		# create a beutiful soup for the html document
		soup = BeautifulSoup(response.text, features='html.parser') 
		print('len(response.text):' + str(len(response.text)))
		# print("response.text: " + response.text)
		allFrames = soup.find_all('frame')  # "a")
		print('len(allFrames):' + str(len(allFrames)))

		appendCount = 0
		for frame in allFrames: 
			# extract sourceed url from the frame
			if 'src' in frame.attrs:
				source = frame.attrs['src']
			else:
				source = ''
		
			# resolve relative sources (starting with /)
			if source.startswith('/'):
				source = base_url + source
		
			elif not source.startswith('http'):
				source = path + source
		
			# if domain in source:  # and issourceGood(source, sourcePhase):
			if source not in unscraped and source not in scraped:
				appendCount += 1
				unscraped.append(source)

	except Exception as exception:
		print('Exception caught in getInfo: ' + str(exception))
		return False
	return True


if __name__ == '__main__':
    main(sys.argv)