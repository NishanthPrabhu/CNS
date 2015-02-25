from __future__ import print_function

__author__ = 'nishanth'

from scapy.all import *
from helper import *

def modifypacket(packet):

    print('\n###### IP Fields Modifier ######\n')

    choice = 1

    while True:
        print('\nModifiable IP fields: ')
        print('1. Fragmentation Flags')
        print('2. Identification Flags (16 bits) ')
        print('3. Checksum modification')
        print('4. Type of Service Field')
        choice = int(raw_input('Enter choice(0 to stop): '))


        if choice == 0:
            return

        elif choice == 1:
           
            modifyflags(packet)

        elif choice == 2:
    
            modifyid(packet)

        elif choice == 3:

            modifychecksum(packet)

        elif choice == 4:

            modifytos(packet)

        else:

            print('Invalid choice. Re-enter.')


# Function to modify the fragmentation offset field

def modifyflags(packet):
    # It is supposed to be a field of 3 bit flags
    # But behaves as an integer. Anyway, try to store values 0-7, total range of a 3 bit field
    newflags = raw_input('Enter the new fragmentation id: ')

    while (is_number(newflags) is False) or int(newid) > 7:
        
        print("Invalid ID, enter a valid ID(integer < 7)\n")
        newflags = raw_input('Enter the new fragmentation flags: ')

    packet[IP].flags = int(newflags)
    return

# Function to modify the fragmentation identification flags

def modifyid(packet):

    newid = raw_input('Enter the new fragmentation id: ')

    while (is_number(newid) is False) or int(newid) > 65535:
        
        print("Invalid ID, enter a valid ID( integer < 65535)\n")
        newid = raw_input('Enter the new fragmentation id: ')

    packet[IP].id = int(newid)
    return

# Function to modify the IP-level checksum

def modifychecksum(packet):

    newchksum = raw_input('Enter new data in checksum field: ')

    while (is_number(newchksum) is False) or int(newchksum) > 65535:
        
        print("Invalid checksum,enter a valid checksum: (integer < 65536) \n")
        newchksum = raw_input('Enter new data in checksum field: ')

    packet[IP].chksum = int(newchksum)
    return


# Function to modify the Type of Service field

def modifytos(packet):

    newtos = raw_input('Enter type of service: ')
    while (is_number(newtos) is False) or int(newtos) > 255:

        print("Invalid TOS, enter a valid TOS: (integer < 256)\n")
        newtos = raw_input('Enter type of service: ')
    
    packet[IP].tos = int(newtos)
    return


