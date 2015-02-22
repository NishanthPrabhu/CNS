from __future__ import print_function

__author__ = 'nishanth'

import sys
from scapy.all import *
import modify_packet


payload = ""


# Function to accept payload for packets

def acceptload():

    global payload

    payload = raw_input('Enter data payload for packet: ')


# Function to create the packets with IP, ICMP layers

def createpacket():

    global payload

    acceptload()
    packet = IP()/payload
    #packet = IP()/ICMP()/payload

    print('Unedited packet: ')
    print(packet.show2())

    modify_packet.modifypacket(packet)

    print('Edited packet: ')
    print(packet.show2())
    send(packet)


if __name__ == '__main__':

    print('Packet creator')
    createpacket()