from __future__ import print_function

__author__ = 'nishanth'

import sys
import scapy.all as scapy

def acceptInput():

    #Accepts the packet field parameters to fill in while creating the packet

    print('Possible fields to fill:  ')
    packetDict = {}
    packetDict['src'] = raw_input('Enter source IP address: ')
    packetDict['dst'] = raw_input('Enter destination IP address: ')
    packetDict['ttl'] = int(raw_input('Enter time to live: '))
    packetDict['id'] = int(raw_input('Enter ID of packet: '))
    packetDict['pay'] = raw_input('Enter packet payload data: ')
    packetDict['option'] = raw_input('Enter the packet options(optional): ')

    #Enter more fields here to fill up

    return packetDict


def createPacket(packDet):

    #Create the IP packets with the user-entered details

    pack = scapy.IP()
    pack.src = packDet['src']
    pack.dst = packDet['dst']
    pack.ttl = packDet['ttl']
    pack.id = packDet['id']
    pack.pay = packDet['pay']
    pack.options = packDet['option']

    print(pack.show2())


if __name__ == '__main__':

    print('Packet Generator\n')
    packetInfo = {}
    packetInfo = acceptInput()
    createPacket(packetInfo)