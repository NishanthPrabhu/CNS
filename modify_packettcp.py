from __future__ import print_function

__author__ = 'nishanth'

from scapy.all import *
from helper import *

def modifypacket(packet):

    print('\n###### TCP Fields Modifier ######\n')

    choice = 1

    while True:
        print('\nModifiable TCP fields: ')
        print('1. TCP-level checksum')
        print('2. TCP reserved bits (4 bits -- 0 to 15)')
        #print('3.')
        #print('4.')
        choice = int(raw_input('Enter choice( 0 to stop):  '))


        if choice == 0:
            return

        elif choice == 1:

            modifychecksum(packet)

        elif choice == 2:

            modifyreserved(packet)

        else:

            print('Invalid choice. Re-enter.')

def modifychecksum(packet):

    newchksum = raw_input('Enter new data in checksum field: ')

    while (is_number(newchksum) is False) or int(newchksum) > 65535:

        print("Invalid checksum,enter a valid checksum: (integer < 65536) \n")
        newchksum = raw_input('Enter new data in checksum field: ')

    packet[TCP].chksum = int(newchksum)
    return



def modifyreserved(packet):

    res = raw_input('Enter data for reserved field( 0 < integer < 15 )')

    while (is_number(res) is False) or int(res) > 15:

        print('Invalid entry. Integer less than 15 required: ')
        res = raw_input('Enter data for reserved field: ')

    packet[TCP].reserved = int(res)
    return




