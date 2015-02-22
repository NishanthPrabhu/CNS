from __future__ import print_function

__author__ = 'nishanth'

from scapy.all import *


def modifypacket(packet):

    choice = 1

    while True:
        print('Modifiable IP fields: ')
        print('1. Fragmentation Flags')
        print('2. Identification Flags (16 bits) ')
        print('3. Checksum modification')
        print('4. Type of Service Field')
        choice = int(raw_input('Enter choice: (0 to stop) '))


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
    pass

# Function to modify the fragmentation identification flags

def modifyid(packet):

    newid = int(raw_input('Enter the new fragmentation id: '))
    packet.id = newid
    return

# Function to modify the IP-level checksum

def modifychecksum(packet):

    newchksum = int(raw_input('Enter new data in checksum field: '))
    packet.chksum = newchksum
    return


# Function to modify the Type of Service field

def modifytos(packet):

    newtos = int(raw_input('Enter type of service: '))
    packet.tos = newtos
    return


###### Helper Function ######


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False












