from __future__ import print_function

__author__ = 'jhanji'

from scapy.all import *


# Function to detail detailed raw hex of packets received

def displaypacket(packet):

    packet.show()

# Function to look for packets in the network

def catchpackets():

    sniff(filter="ip", prn=displaypacket)


if __name__=='__main__':

    catchpackets()