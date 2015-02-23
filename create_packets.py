from __future__ import print_function

__author__ = 'nishanth'

import sys
from scapy.all import *
import modify_packetip
import modify_packettcp


payload = ""


# Function to accept payload for packets

def acceptload():

    global payload

    payload = raw_input('Enter data payload for packet: ')


# Function to create the packets with IP, ICMP layers

def createpacket():

    global payload

    acceptload()
    #packet = IP()/payload
    packet = IP()/TCP()/payload
    #packet = IP()/ICMP()/payload

    print('Unedited packet: ')
    print(packet.show2())

    choice = int(raw_input('\nDo you wish to modify the packet? '))
    if choice==1:

        print('\n1. IP level Fields')
        print('2. TCP level Fields')
        print('3. Both TCP and IP')
        modchoice = int(raw_input('Enter your choice: '))

        if modchoice == 1:

            modify_packetip.modifypacket(packet)

        elif modchoice == 2:

            modify_packettcp.modifypacket(packet)

        else:

            modify_packetip.modifypacket(packet)
            modify_packettcp.modifypacket(packet)


        print('Edited packet: ')
        print(packet.show2())

    send(packet)




if __name__ == '__main__':

    print('###### Packet creator ###### \n')
    createpacket()