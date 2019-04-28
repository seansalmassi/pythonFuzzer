#!/usr/bin/python

from scapy.all import *

send(fuzz(IP(dst="1.1.1.1")),loop=1)

#Working
