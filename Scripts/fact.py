#!/usr/bin/env python3
#!# -*- coding: utf-8 -*- 
import re
import os 
import datetime
import xml.etree.ElementTree as ET
import urllib.request

def getFact():
	
	#~ # Download from Wikipedia
	
	month = datetime.datetime.today().month
	day = datetime.datetime.today().day
	url ="https://ja.wikipedia.org/wiki/%e7%89%b9%e5%88%a5:%e3%83%87%e3%83%bc%e3%82%bf%e6%9b%b8%e3%81%8d%e5%87%ba%e3%81%97"
	r = urllib.request.urlopen(url + "/"+str(month)+"%e6%9c%88"+str(day)+"%e6%97%a5")
	file = r.read().decode("utf-8")
	
	#~ t = open("Factsample.txt","r")
	#~ file = t.read()
	#~ t.close()
	
	text = (ET.fromstring(file)[1][3][7].text).split("\n")
	step = 0 
	event = []
	birth = []
	for v in text:
		if v == "== できごと ==":
			step = 1
		elif v == "== 誕生日 ==":
			step = 2
		elif v == "== 忌日 ==":
			step = 3
		elif v == "== 記念日・年中行事 ==":
			step = 4
		elif v == "== フィクションのできごと ==":
			step = 5

		if v[:2] == "* ":
			word = v[2:].replace("。","｡ ")
			word = word.replace("、","､ ")
			if step ==1:
				s = re.split(r"<ref.*</ref>",word)
				event.append("".join(s))
			elif step == 2:
				s = re.split(r"<ref.*</ref>",word)
				birth.append("".join(s))

	# open the file for writitng
	#~ fact_file = open('../Downloads/fact.cml', 'w')
	fact_file = open('Downloads/fact.cml', 'w')
	
	# write the fact
	for data in event:
		fact_file.write('event:' + data + '\n')
	for data in birth:
		fact_file.write('birth:' + data + '\n')
	fact_file.write("status:FILLED")
	
	# close the file
	fact_file.close()
	
getFact()
