# Starting from here:
# https://github.com/dstrube1/playground_python/blob/master/emailScraper.py

from bs4 import BeautifulSoup
import time
import requests
import sys

def get_time(seconds):
	# Copied from my CS 7641 Assignment 2
	if int(seconds / 60) == 0:
		if int(seconds) == 0:
			return str(round(seconds, 3)) + ' seconds'
		return str(int(seconds)) + ' second(s)'
	minutes = int(seconds / 60)
	seconds = int(seconds % 60)
	if int(minutes / 60) == 0:
		return str(minutes) + ' minute(s) and ' + str(seconds) + ' second(s)'
	hours = int(minutes / 60)
	minutes = int(minutes % 60)
	# Assuming this won't be called for any time span greater than 24 hours
	return str(hours) + ' hour(s), ' + str(minutes) + ' minute(s), and ' + str(seconds) + ' second(s)'

def main(args):
	if len(args) <= 1:
		print('Usage: python3 MSJScraper.py {url}')
		return
	# args[0] : MSJScraper.py
	url = args[1]
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		response = requests.get(url, headers = headers)
		print('response.text:')
		print(response.text)
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
		# ignore pages with errors and continue with next url
		print('Caught exception')

if __name__ == '__main__':
	start = time.time()
	main(sys.argv)
	end = time.time()
	print('\nDone in ' + get_time(end - start))

# TODO: WIP

