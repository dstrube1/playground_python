import requests
# https://realpython.com/python-requests/

URL = "https://public-api.wordpress.com/wpcom/v2/work-with-us"
response = requests.get(URL)

print("response.status_code: ", response.status_code) # 404
#print("response.content: ", response.content)
# ^This is a binary form of this:
print("response.text: ", response.text)
# =>  "Instructions: Expected 'X-future' header with value 'automattician'"

#print("response.headers: ", response.headers)

# Looking for a secret...
response = requests.get(URL, headers={"X-future": "automattician"})
print("response.status_code: ", response.status_code)
print("response.text: ", response.text)
