#!/usr/bin/python

from scapy.all import *

send(IP(dst="1.1.1.1")/fuzz(NTP(version=4)),loop=1)

#Working
