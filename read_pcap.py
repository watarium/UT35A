from scapy.all import *
import binascii

packets = rdpcap('UT35A_boil_ladder_101_103.pcapng')

# Let's iterate through every packet
for packet in packets:
    bin_data = packet.load
    # print(bin_data)
    hex_data = str(binascii.hexlify(bin_data))
    hex_data = hex_data.lstrip('b')
    print(hex_data)

