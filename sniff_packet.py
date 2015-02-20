from __future__ import print_function

__author__ = 'jhanji'

import sys
import scapy.all as scapy


a=scapy.sniff(filter="ip")
a.nsummary()
#print(type(a))

for item in a:
    print(item.show2())