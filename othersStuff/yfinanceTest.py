import yfinance as yf
#from pandas_datareader.data import get_quote_yahoo
#from pandas_datareader import data as pdr
#from datetime import datetime, timedelta

#msft = yf.Ticker("MSFT")
#open = msft.info["open"]
#print("open: "+str(open))
#close = msft.info["previousClose"]
#print("close: "+str(close))
#print("volume: "+str(msft.info["volume"]))
#stocks = ["MSFT"]
#df = get_quote_yahoo(stocks)
#print("regularMarketChangePercent: "+str(df['regularMarketChangePercent'][0]))
#marketChange = ((open - close)/close)*100
#print("computed marketChange: " + str(marketChange))

#yf.pdr_override() 
stocks = ["CSCO", "MSFT"]
#yeseterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
#today = datetime.strftime(datetime.now(), '%Y-%m-%d')
#data = pdr.get_data_yahoo(stocks, start=yeseterday, end=today)
#print("open: "+str(data.info.open))#["open"][1]))
for stock in stocks:
	data = yf.Ticker(stock)
	symbol = data.info["symbol"]
	open = data.info["open"]
	close = data.info["previousClose"]
	volume = data.info["volume"]
	marketChange = ((open - close)/close)*100
	print("symbol: "+symbol+"; open: "+str(open)+"; close: "+str(close))
