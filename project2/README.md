Introduction
============
The project is find 4 bad fast-flux domain and 7 good fast-flux domain.Which domain need to forward to 4 different ip.

Fast-Flus
---------
	A domain name used in a fast-flux service network maps to multiple IP. So I used the NumberOfIP() check the IP maps greater than 4 first. Because I don't want to wait the TTL, I used mutiple dns to check the IP maps. Must domain name which used in a fast-flux usually represents a different ASN, that is, the IP maps belong to different country. So I used the NumberOfASN() to check the number of ASN. If the number of ASN are greater than 1, than record the domain in the badresult. Because the domain maybe the domain which used in a fast-flux service. But there are many company provide some cdn which has some behavior similar as fast-flux service, so I used TryCDN() to check the doman whether belong to some cdn which are famous. Then record it to goodresult,because it maps to multiple IP.


Filterdomain.py
===============
the program will filter the domain which forward less 4 different ip and the ip are different form asn

FilterdomainV2.py
=================

the program is similar as Filterdomain.py but it use three dns server to filter.

FilterdomainV3.py
=================

the program is similar as FilterdomainV2.py but fliter the cdn domain.
