#!/usr/bin/python

from scapy.all import *

send(fuzz(IP(dst="1.1.1.1"))/ICMP()/fuzz(UDP())/fuzz(DNS())/fuzz(DHCP()),loop=1)

#working
