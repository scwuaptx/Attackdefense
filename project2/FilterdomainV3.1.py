#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#The program will filiter the domain,which forward ip less than 4,then record it in the goodresult
#If the asn of ip are different ,then record it in the badresult
#Source file : list   Result file : goodresult and badreuslt
#if IP > 4 and ASN > 1 and not cdn than record in badresult
#if IP > 4 but ASN == 1 or is cdn than record in goodresult

import os
import popen2


#DomainToIP() return ip list which is forwarded by the domain
def DomainToIP(domain):
	IPlist=[]
	domain = "".join(domain.split())
	for dns in [" "," 139.175.55.244"," 8.8.8.8"]:
		DataOut,DataIn = popen2.popen2("host -t A " + domain + dns)
		SeparateIP = DataOut.readlines()
		for i in range (len(SeparateIP)-1):
			temp = SeparateIP[i].split()
			if len(temp) > 0 :
				try :
					IP = temp[3]
					if IP not in "alias" :
						if IP not in IPlist :
							IPlist.append(IP)
				except:
					continue

 	return IPlist

#NumberOfAsn() return the asn which is forwarded by the IP 
def IPtoASN(IPlist):
	ASNlist = []
	Countrylist = []
	for IP in IPlist :
		try :
			ASNOut,IPIN = popen2.popen2("whois -h whois.cymru.com -c "+IP)		
			SeparateASN = (ASNOut.read()).split("\n")
			temp = SeparateASN[2].split('|')
			ASN = temp[0]
			Country = temp[2]
			if ASN not in ASNlist :
				ASNlist.append(ASN)
			if Country not in Countrylist :
				Countrylist.append(Country)
		except :
			continue
		
	return ASNlist,Countrylist

#TryCDN will check the domain whether belong to cdn.
def TryCDN(domain):
	CDN = ["akamai","cdn","akafms","amazon","google","adobe"]
	DataOut,DataIn = popen2.popen2("host -t NS " + domain)
	SeparateIP = (DataOut.read()).split(".")
	for i in CDN :
		if i in SeparateIP :
			return True
	return False

if __name__=='__main__':
	fileopengood = open('goodresult','w')
	fileopenbad = open('badresult','w')	
	for domain in open('list'):  
		IPlist = DomainToIP(domain)
		ASNlist,Countrylist = IPtoASN(IPlist)
		if len(IPlist) > 4 :
			if not TryCDN(domain) and len(ASNlist) > 1 and len(Countrylist) > 1 :
				fileopenbad.write(domain)
			else :
				fileopengood.write(domain)
				
	fileopengood.close()
	fileopenbad.close()

