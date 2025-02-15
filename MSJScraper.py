# Starting from here:
# https://github.com/dstrube1/playground_python/blob/master/emailScraper.py

#from bs4 import BeautifulSoup
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
		headers = {#'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'Accept-Encoding':'gzip, deflate, br, zstd',
			'Accept-Language': 'en-US,en;q=0.9',
			'Cache-Control': 'max-age=0',
			'Cookie': 'MUID=2CC68EFDA51D6CEB3F6C8138A4316DBE; display-culture=en-US; ai_user=1NDDP|2024-10-03T00:34:24.927Z; MicrosoftApplicationsTelemetryDeviceId=6cc7118e-f002-4d6f-945b-65c684fed8d0; handleWcpConsentGCSVNext={%22Required%22:true%2C%22Analytics%22:true%2C%22SocialMedia%22:true%2C%22Advertising%22:true}; MSFPC=GUID=e5b687bd60fc4d6aa119c53424674738&HASH=e5b6&LV=202401&V=4&LU=1705938849499; fptctx2=H3ihr9e92IdW6yd1ZgQ9SxLzXxHcL2CcU%252fZDGCdp0wEYNy8xdX4c8lmMocog7EfmuT%252bwIlryuhPoLrxUzIaHzdhfDNjl8GTlKuhbdk9oljSo1RFJEMKYFN6p5SfjGp5M4xEjHz14UyFbUfatHhE4n43R83tKHiorBm9csgU7cReqfmq%252bwlWb4%252bnsDJqiDywgD2KAXR6BTXX16fhuXb6RAxAeKxEpTMMCk2vGAX18a7PXEyFb4fv3g8PaXGmtn9nkQ1m2vWd2Yncbge2KWZx6omh1CIUH2RopTMY2QR3h2%252bdJFRWewKtEjjPBxb1pi3py9lLey7ERmGGnGZ9wVFJMhg%253d%253d; at_check=true; AMCVS_EA76ADE95776D2EC7F000101%40AdobeOrg=1; AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg=1585540135%7CMCIDTS%7C20005%7CMCMID%7C70762806631203242063957907667774242628%7CMCAAMLH-1729003325%7C7%7CMCAAMB-1729003325%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-1133088764%7CMCOPTOUT-1728405725s%7CNONE%7CMCAID%7C31DA84A47E152004-60000993182E6FF6%7CvVersion%7C4.4.0; mbox=session#4bac355748254ab685050600e4e43920#1728400385|PC#4bac355748254ab685050600e4e43920.34_0#1762585224; _uetvid=7ea15900858311ef8d107da8b4bd222b; ANON=A=DD29A703C387FF4392C0A052FFFFFFFF&E=1e56&W=4; NAP=V=1.9&E=1dfc&C=mmOGfyH4klFuJFkhxCHYuHH9ZtpDwXgNfj9FsMHVfGWwRbojrEOAmA&W=1; MC1=GUID=bfc0f8f6033b40caa7478e67dc4dc0fb&HASH=bfc0&LV=202501&V=4&LU=1737512831933; MSCC=NR; MS0=b296b5d029534e08b3097956c5ececd8; auth_session=e7ac2607-26ab-4b6c-ae9e-d7e9dfbfc96c; servicehealthchecker=; ai_session=1IArc35LNWTuQ05+u3D3V6|1739476062976|1739477765384',
			#'Connection': 'keep-alive',
			'DNT': '1',
			'If-Modified-Since': 'Tue, 10 Dec 2024 07:40:53 GMT',
			#'If-None-Match': 'W/"0x8DD18EDF9EBADBD"',
			'Priority': 'u=0, i',
			'Sec-Ch-Ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
			'Sec-Ch-Ua-Mobile': '?0',
			'Sec-Ch-Ua-Platform': '"macOS"',
			'Sec-Fetch-Dest': 'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'same-origin',
			'Sec-Fetch-User': '?1',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
			}
		response = requests.head(url, headers = headers)
		print('response.status_code:')
		print(response.status_code)

		response = requests.get(url, headers = headers)
		print('response.text:')
		print(response.text)

		#print('response.content:')
		#print(response.content)
		
	except (requests.exceptions.MissingSchema):
		print('Caught exception: MissingSchema')
	except (requests.exceptions.ConnectionError):
		print('Caught exception: ConnectionError')

if __name__ == '__main__':
	start = time.time()
	main(sys.argv)
	end = time.time()
	print('\nDone in ' + get_time(end - start))

# TODO: WIP

