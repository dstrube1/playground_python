#Purpose: Parse weather from official, government, and free source

#option 1:
#https://www.weather.gov/documentation/services-web-api#
#https://weather-gov.github.io/api/gridpoints

#option 2+:
#https://www.ncdc.noaa.gov/cdo-web/webservices
#https://www.ncdc.noaa.gov/cdo-web/webservices/v2
#https://www.ncdc.noaa.gov/cdo-web/token

import datetime
import json
import requests
import sys
from dateutil.parser import *
from dateutil.relativedelta import *

userAgent = "(gatech.edu, ds@gatech.edu)"
headers = {'User-Agent': userAgent}
_url = "https://api.weather.gov/points/[lat],[lon]"
propertiesKey = "properties"

def hasKey(_keys, _key):
	if _key in _keys:
		return True
	print("Expected key '" + _key + "' not found.")
	return False

def convertCelsiusToFahrenheit(celsius):
	#https://www.pythonforbeginners.com/code-snippets-source-code/python-code-celsius-and-fahrenheit-converter
	return ((9.0/5.0) * celsius) + 32

def getTemperature(object):
	#Get temperature from dictionary with confusing structure-
	#sourceUnit = F, but uom = C (?!)
	sourceUnitKey = "sourceUnit"
	uomKey = "uom" #unit of measure
	valuesKey = "values"
	if (not hasKey(object.keys(), sourceUnitKey)) \
		or (not hasKey(object.keys(), uomKey) \
		or (not hasKey(object.keys(), valuesKey))):
		return 0
	sourceUnit = object[sourceUnitKey]
	if sourceUnit != "F":
		print("Unexpected sourceUnit: " + sourceUnit)
		return 0
	uom = object[uomKey]
	if uom != "unit:degC":
		print("Unexpected uom: " + uom)
		return 0
	_values = object[valuesKey]
	if len(_values) == 0:
		print("Empty values")
		return 0
	tempOut = _values[0]["value"]
	#print("tempOut: " + str(tempOut))
	return convertCelsiusToFahrenheit(tempOut)

def getForecastUrl():
	with requests.get(_url, headers=headers) as response:
		if response.status_code != 200:
			print("Error: response.status_code: " + str(response.status_code))
			return None
		dict = json.loads(response.content.decode('utf-8'))
	#print(dict)
	if not hasKey(dict.keys(), propertiesKey):
		return
	properties = dict[propertiesKey]
	forecastKey = "forecast"
	if not hasKey(properties.keys(), forecastKey):
		return None
	return properties[forecastKey]
	
def getForecastGridDataUrl():
	with requests.get(_url, headers=headers) as response:
		if response.status_code != 200:
			print("Error: response.status_code: " + str(response.status_code))
			return None
		dict = json.loads(response.content.decode('utf-8'))
	#print(dict)
	if not hasKey(dict.keys(), propertiesKey):
		return
	properties = dict[propertiesKey]
	forecastGridDataKey = "forecastGridData"
	if not hasKey(properties.keys(), forecastGridDataKey):
		return None
	return properties[forecastGridDataKey]

def getIcon(forecastUrl):
	with requests.get(forecastUrl, headers=headers) as response:
		if response.status_code != 200:
			print("Error: response.status_code: " + str(response.status_code))
			return None
		dict = json.loads(response.content.decode('utf-8'))
	#print(dict)
	if not hasKey(dict.keys(), propertiesKey):
		return None
	properties = dict[propertiesKey]
	periodsKey = "periods"
	if not hasKey(properties.keys(), periodsKey):
		return None
	periods = properties[periodsKey]
	iconKey = "icon"
	if not hasKey(periods[0].keys(), iconKey):
		return None
	return periods[0][iconKey]

def getMaxAndMinTemperatureF(forecastGridDataUrl):
	with requests.get(forecastGridDataUrl, headers=headers) as response:
		if response.status_code != 200:
			print("Error: response.status_code: " + str(response.status_code))
			return None
		dict = json.loads(response.content.decode('utf-8'))
	if not hasKey(dict.keys(), propertiesKey):
		return None
	properties = dict[propertiesKey]
	maxTemperatureKey = "maxTemperature"
	minTemperatureKey = "minTemperature"
	if (not hasKey(properties.keys(), maxTemperatureKey)) or (not hasKey(properties.keys(), minTemperatureKey)):
		return None
	#These are objects, not numbers
	maxTemperature = properties[maxTemperatureKey]
	minTemperature = properties[minTemperatureKey]
	return int(getTemperature(maxTemperature)), int(getTemperature(minTemperature))

def getCurrentTemperature(forecastGridDataUrl):
	with requests.get(forecastGridDataUrl, headers=headers) as response:
		if response.status_code != 200:
			print("Error: response.status_code: " + str(response.status_code))
			return 0
		dict = json.loads(response.content.decode('utf-8'))
	if not hasKey(dict.keys(), propertiesKey):
		return 0
	properties = dict[propertiesKey]
	temperatureKey = "temperature"
	if not hasKey(properties.keys(), temperatureKey):
		return 0
	temperature = properties[temperatureKey]
	sourceUnitKey = "sourceUnit"
	uomKey = "uom" #unit of measure
	valuesKey = "values"
	if (not hasKey(temperature.keys(), sourceUnitKey)) \
		or (not hasKey(temperature.keys(), uomKey) \
		or (not hasKey(temperature.keys(), valuesKey))):
		return 0
	sourceUnit = temperature[sourceUnitKey]
	if sourceUnit != "F":
		print("Unexpected sourceUnit: " + sourceUnit)
		return 0
	uom = temperature[uomKey]
	if uom != "unit:degC":
		print("Unexpected uom: " + uom)
		return 0
	#This is the list of objects with time and temperature
	_values = temperature[valuesKey]
	if len(_values) == 0:
		print("Empty values")
		return 0
	validTimeKey = "validTime"
	valueKey = "value"
	prevValue = _values[0]
	validTime = parse(prevValue[validTimeKey].split('+')[0])
	now = datetime.datetime.now()
	#print("now = " + str(now))
	
	#Find which value has time closest to now without being in the future;
	#dateutil parser and relativedelta are quite handy!
	for _value in _values:
		#Parse everything before the timezone indicator
		#https://dateutil.readthedocs.io/en/stable/examples.html#parse-examples
		tempTime = parse(_value[validTimeKey].split('+')[0]) 
		#Compare to now
		#https://dateutil.readthedocs.io/en/stable/relativedelta.html
		delta = relativedelta(now, tempTime)
		hours = delta.hours
		days = delta.days
		prevValue = _value
		if days < 0 or hours <= 0:
			break
	#print("tempTime: " + str(tempTime))
	#print("delta: " + str(delta))
	#print("prevValue: " + str(prevValue))
	return int(convertCelsiusToFahrenheit(prevValue[valueKey]))

def main(args):
	global _url
	try:
		#Default: Lawrenceville
		lat = "33.9983683"
		lon = "-84.0572139"
		for arg in args :
			if arg.startswith("lat="):
				#print ("arg: " + arg)
				lat = arg.split("=")[1]
			if arg.startswith("lon="):
				lon = int(arg.split("=")[1])

		_url = _url.replace("[lat]",lat).replace("[lon]",lon)
		
		now = datetime.datetime.now()
		print("now = " + str(now))
		
		#We could get both of these urls in one method (like we do with getMaxAndMinTemperatureF),
		#but for now it's not an issue, and seems cleaner to do it like this:
		forecastUrl = getForecastUrl()
		forecastGridDataUrl = getForecastGridDataUrl()
		#print("forecastUrl: " + forecastUrl)
		#print("forecastGridDataUrl: " + forecastGridDataUrl)
		
		#output formatter:
		#https://jsonformatter.curiousconcept.com/
		
		#Get icon
		icon = getIcon(forecastUrl)
		print("icon: " + icon)
		
		#Get today's max and min
		maxTemperatureF,minTemperatureF = getMaxAndMinTemperatureF(forecastGridDataUrl)
		print("maxTemperatureF: " + str(maxTemperatureF))
		print("minTemperatureF: " + str(minTemperatureF))
		
		#Get current temperature
		currentTemperature = getCurrentTemperature(forecastGridDataUrl)
		print("currentTemperature: " + str(currentTemperature))

	except Exception as exception:
		print("Exception caught: " + str(exception))

if __name__ == '__main__':
	main(sys.argv)
