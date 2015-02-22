from __future__ import print_function

__author__ = 'nishanth'

import sys
from scapy.all import *


payload = ""


#Function to accept payload for packets

def acceptLoad():

    global payload

    payload = raw_input('Enter data payload for packet: ')



#Function to create the packets with IP, ICMP layers

def createPacket():

    global payload

    acceptLoad()
    packet = IP()/payload

    print('Packet being sent: ')
    print(packet.show2())

    for i in range(10):
        send(packet)



#sequence number
#frag offset
#flag
#tos
#identification field
#checksum modification?


if __name__ == '__main__':

    print('Packet creator')
    createPacket()