from __future__ import print_function

__author__ = 'jhanji'

import sys
import scapy.all as scapy


def displaypacket(packet):

    print(len(packet))


def catchpackets():

    packets = scapy.sniff(filter="ip", prn=displaypacket)


if __name__=='__main__':

    catchpackets()