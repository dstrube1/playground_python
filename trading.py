#Algorithmic Trading
#https://www.youtube.com/watch?v=xfzGZB4HhEE
#circa 10:46

#https://iexcloud.io/console/
filePrivate = "../../private/private.txt"
symbol = 'AAPL'
api_url = f''
data = requests.get(api_url).json()
print(data)
