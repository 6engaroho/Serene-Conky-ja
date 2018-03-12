#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

def main():
	t = open("Downloads/meigen","r")
	file = t.read()
	t.close()
	
	meigen = file.split("\n%\n")
	number = 50 
	
	# open the file for writitng
	quote_file = open('Downloads/quote.cml', 'w')
	
	for i in range(1,number +1):
		v = meigen[random.randrange(len(meigen) -1)]
	
	# write the quote
		lines = v.splitlines()
		word = " ".join(lines[:-1]).replace("。","｡ ").replace("、","､ ")
		quote_file.write(str(i)+ '_quote:')
		quote_file.write(word+'\n' )
		quote_file.write(str(i)+ '_author:' + lines[-1].lstrip() +'\n')
		
	quote_file.write("status:FILLED")
	
	# close the file
	quote_file.close()
main()
