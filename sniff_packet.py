from __future__ import print_function

__author__ = 'jhanji'

import sys
from scapy.all import *


def displaypacket(packet):

    packet.show()


def catchpackets():

    sniff(filter="ip", prn=displaypacket)


if __name__=='__main__':

    catchpackets()