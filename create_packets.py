from __future__ import print_function

__author__ = 'nishanth'

import sys
import scapy.all as scapy

class steg:

    def acceptInput(self):

        # Accepts the packet field parameters to fill in while creating the packet

        print('Possible fields to fill:  ')
        packetdict = {}
        #packetdict['src'] = raw_input('Enter source IP address: ')
        #packetdict['dst'] = raw_input('Enter destination IP address: ')
        #packetdict['ttl'] = int(raw_input('Enter time to live: '))
        #packetdict['id'] = int(raw_input('Enter ID of packet: '))
        packetdict['src'] = '127.0.0.1'
        packetdict['dst'] = '127.0.0.1'
        packetdict['ttl'] = 11
        packetdict['id'] = 1234

        packetdict['pay'] = raw_input('Enter packet payload data: ')
        packetdict['option'] = raw_input('Enter the packet options(optional): ')

        # Enter more fields here to fill up

        return packetdict


    def createPacket(self,packDet):

        # Create the IP packets with the user-entered details

        pack = scapy.IP()
        pack.src = packDet['src']
        pack.dst = packDet['dst']
        pack.ttl = packDet['ttl']
        pack.id = packDet['id']
        pack.pay = packDet['pay']
        pack.options = packDet['option']

        print('Packet being sent: ')
        print(pack.show2())

        for i in range(10):
            scapy.send(pack)


ob = steg()
print('Packet Generator\n')
packetInfo = {}
packetInfo = ob.acceptInput()
ob.createPacket(packetInfo)
