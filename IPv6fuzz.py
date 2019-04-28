#!/usr/bin/python

from scapy.all import *

send(IP(dst="1.1.1.1")/fuzz(IPv6()),loop=1)

#Working
