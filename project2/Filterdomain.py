#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#The program will filiter the domain which forward ip less than 4
#Source file : list   Result file : result 

import os
import popen2

#NumberOfIP() check the number of ip which is forwarded by the domain
def NumberOfIP(domain):
	IP,DataIn = popen2.popen2("host -t A "+domain)
	SeparateIP = (IP.read()).split("\n")
	number = len(SeparateIP)

	return number

if __name__=='__main__':
	fileopen = open('result','w')
	for domain in open('list'):  
		if NumberOfIP(domain) > 4:
			fileopen.write(domain)
	fileopen.close()
