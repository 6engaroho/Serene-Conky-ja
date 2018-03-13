#!/usr/bin/env python3
#!# -*- coding: utf-8 -*- 
import re
import os 
import datetime
import xml.etree.ElementTree as ET
import urllib.request

def readConfiguration(): 
	config = {
	"unit":  "si"
	}
	return config

def icons(ja, day_or_n):	
	print(ja)
	if ja == "晴れ":
		if day_or_n == "day":
			return "clear-day"
		else:
			return "clear-night"
	elif ja == "曇り":
		return "cloudy"
	elif ja.find("晴") >= 0 and ja.find("曇") >= 0:
		if day_or_n == "day":
			return "partly-cloudy-day"
		else:
			return "partly-cloudy-night"
	elif ja.find("雨") >= 0:
		return "rain"
	elif ja.find("雪") >= 0:
		return "snow"
	elif ja == "みぞれ":
		return "sleet"
	else:
		return "default"

# 都市設定
city = '22' ;#静岡市 livedoor-Weather-hack
ycity = '5010';#静岡市 yahoo天気予報
loc = "静岡"

def getTemp():
	
	# parse temperature
	
	url = "http://weather.livedoor.com/forecast/rss/amedas/temp/%s.xml"
	r = urllib.request.urlopen(url % (city))	
	file = r.read().decode("utf-8")


	#~ t = open("Tmpsample.txt","r")
	#~ file = t.read()
	#~ t.close()
	
	temp = ""
	
	root = ET.fromstring(file)
	for desc in root.iter('item'):
		title = desc.find('title').text
		if title[:len(loc) +1] == loc +" ":
			sep = re.search(r"(\d+)[^\d\-]+(-?[\d\.]+)", title)
			temp = sep.group(2)
			break
	return temp

def getWind():
	
	# parse wind
	
	url = "http://weather.livedoor.com/forecast/rss/amedas/wind/%s.xml"
	r = urllib.request.urlopen(url % (city))	
	file = r.read().decode("utf-8")

	#~ t = open("Wndsample.txt","r")
	#~ file = t.read()
	#~ t.close()
	
	windspd = []

	root = ET.fromstring(file)
	for desc in root.iter('item'):
		title = desc.find('title').text
		if title[:len(loc) +1] == loc +" ":
			sep = re.search(r"]\s([東西南北]+)の風\s([\d+\.?]*\d)m/s", title)
			#~ winddir = sep.group(1)
			windspd.append(sep.group(2))
			break
	return windspd
	
def getWeather():
	
	# parse yahoo weather
	
	url = "http://rss.weather.yahoo.co.jp/rss/days/%s.xml"
	r = urllib.request.urlopen(url % (ycity))	
	file = r.read().decode("utf-8")
	
	#~ t = open("AMEsample.txt","r")
	#~ file = t.read()
	#~ t.close()
	
	entry = []
	root = ET.fromstring(file)
	
	for desc in root.iter('channel'):
		title = desc.find('lastBuildDate').text
		entry.append(title)
		
	for desc in root.iter('item'):
		title = desc.find('title').text
		entry.append(title)
	return entry
	
def readWeather(config):
	
	# get the details fo the current weather
	data = {}
	
	entry = getWeather()
	data['update_at'] = entry[0]
	
	temp = getTemp()
	data['temperature'] = "%.1f" % (float(temp))	
	windspd = getWind()
	data['wind'] = windspd[0]
	data['feel'] = "%.1f" % (float(temp) - float(windspd[0]))

	data['summary'] = entry[8].split(" - ")[0]
	
	now = entry[1].split(" - ")
	
	hour = datetime.datetime.today().hour
	if 6 <= hour <= 18 :
		data["icon"] = icons(now[0].split(" 】 ")[1],"day")
	else:
		data["icon"] = icons(now[0].split(" 】 ")[1],"night")
		


	
	# get day by day data
	
	day_index = 1 # with 1 being today
	
	for i in range(day_index,5):
		day = entry[i].split(" - ")
		
		data[str(i) + '_' + 'icon'] = icons(day[0].split(" 】 ")[1],"day")
		data[str(i) + '_' + 'summary'] = day[0]
		
		sep = re.search(r"(-?[\d\.]+)℃/(-?[\d\.]+)℃", day[1])

		data[str(i) + '_' + 'maxTemp'] = sep.group(1)
		data[str(i) + '_' + 'minTemp'] = sep.group(2)

		# get the units
	units = "si"
		# put the unit specific details
	if units == 'si':
			data['temp_unit'] = 'C'
			data['speed_unit'] = 'm/s'
	elif units == 'ca':
			data['temp_unit'] = 'C'
			data['speed_unit'] = 'km/h'
	else:
			data['temp_unit'] = 'F'
			data['speed_unit'] = 'mph'

	return data


def writeWeather(data):
	# open the file for writitng
	#~ weather_file = open('../Downloads/weather.cml', 'w')
	weather_file = open('Downloads/weather.cml', 'w')
	# write the weather
	for key in data:
			weather_file.write(key + ':' + str(data[key]) + '\n')
	# close the file
	weather_file.close()


# read the configuration
config = readConfiguration()

# read the weatther
data = readWeather(config)

# change the status
data['status'] = 'FILLED'

# write the weather
writeWeather(data)

#~ import notify2
#~ notify2.init(u"weather")
#~ n = notify2.Notification(u"title", u"message")
#~ n.show()
