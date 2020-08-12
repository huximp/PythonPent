#!/usr/bin/python
import sys

from scapy.all import *

conf.verb = 0

portas= [21,22,23,25,80,443,110]
for ip in range(1,255):
	iprange = "192.168.0.%s" %ip
	pIP = IP(dst=iprange)
	pacote = pIP/ICMP()
	resp, noresp = sr(pacote)
	print (resp.show())
	for resposta in resp:
#		porta = resposta[1][TCP].sport
#		flag = resposta[1][TCP].flags
#		if (flag == "SA"):
		print (resposta[1][IP].src)
exit()
