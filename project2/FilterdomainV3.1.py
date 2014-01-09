#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#The program will filiter the domain,which forward ip less than 4,then record it in the goodresult
#If the asn of ip are different ,then record it in the badresult
#Source file : list   Result file : goodresult and badreuslt
#if IP > 4 and ASN > 1 and Country > 1 and Var > 0 and not cdn than record in badresult
#if IP > 4 but ASN == 1 or is cdn than record in goodresult

import os
import popen2


#DomainToIP() return ip list which is forwarded by the domain
def DomainToIP(domain):
	IPlist={}
	domain = "".join(domain.split())
	for dns in [" "," @139.175.55.244"," @8.8.8.8"]:
		DataOut,DataIn = popen2.popen2("dig +noall +answer " + domain + dns)
		SeparateIP = DataOut.readlines()
		for i in range (len(SeparateIP)-1):
			temp = SeparateIP[i].split()
			if len(temp) > 0 :
				try :
					IP = temp[4].strip()
					types = temp[3].strip()
					TTL = int(temp[1].strip())
					if types is "A" :
						if IP not in IPlist :
							IPlist[IP] = 1
						else :
							IPlist[IP] = IPlist[IP] + 1
				except:
					continue

 	return IPlist,TTL

#NumberOfAsn() return the asn with country which is forwarded by the IP 
def IPtoASN(IPlist):
	ASNlist = {}
	for IP in IPlist :
		try :
			ASNOut,IPIN = popen2.popen2("whois -h whois.cymru.com -c "+IP)		
			SeparateASN = (ASNOut.read()).split("\n")
			temp = SeparateASN[2].split('|')
			ASN = temp[0]
			Country = temp[2]
			if ASN not in ASNlist :
				ASNlist[ASN] = Country
		except :
			continue
		
	return ASNlist	

#TryCDN will check the domain whether belong to cdn.
def TryCDN(domain):
	CDN = ["akamai","cdn","akafms","amazon","google","adobe"]
	DataOut,DataIn = popen2.popen2("host -t NS " + domain)
	SeparateIP = (DataOut.read()).split(".")
	for i in CDN :
		if i in SeparateIP :
			return True
	return False

#Variance_IP() calculate Variance of IP
def Variance_IP(IPlist):
	Variance = 0
	mean = float(sum(IPlist.values())/len(IPlist))
	for IP in IPlist :
		Variance += (IPlist[IP]-mean)**2
	return float(Variance/len(IPlist))

if __name__=='__main__':
	fileopengood = open('goodresult','w')
	fileopenbad = open('badresult','w')	
	for domain in open('list'):  
		IPlist,TTL = DomainToIP(domain)
		ASNlist = IPtoASN(IPlist)
		Country = set(ASNlist.values())
		if len(IPlist) > 4 :
			if not TryCDN(domain) and Variance_IP(IPlist) > 0 and TTL < 600 :
				if len(ASNlist) > 1 and len(Country) > 1 :
					fileopenbad.write(domain)
			else :
					fileopengood.write(domain)
				
	fileopengood.close()
	fileopenbad.close()

