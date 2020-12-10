#!/usr/bin/python3.4
import binascii
import socket

'''
Following script will send a UDP packet using as source IP and source MAC current NIC configuration
Scenario 1. You received .pcap file from which you want to replay udp_payload in hex format and use it on your script.
Scenario 2. Send over the network RIP update for a network like 10.10.10.0/24 with metric value 16.
'''

def send_udp_message(message, address, port):
    """send_udp_message sends a message to UDP server

    message should be a hexadecimal encoded string
    """
    message = message.replace(" ", "").replace("\n", "")
    server_address = (address, port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(binascii.unhexlify(message), server_address)
        data, _ = sock.recvfrom(4096)
    finally:
        sock.close()
    return binascii.hexlify(data).decode("utf-8")

#Scenario 1
message= '409d81800001000d0000000003617069086d697870616e656c03636f6d0000010001c00c00010001000002280004a936811cc00c00010001000002280004a9368103c00c00010001000002280004a9368112c00c00010001000002280004a9368122c00c00010001000002280004a9368119c00c00010001000002280004a9368124c00c00010001000002280004a9368108c00c00010001000002280004a9368123c00c00010001000002280004a9368128c00c00010001000002280004a936810fc00c00010001000002280004a936810dc00c00010001000002280004a9368107c00c00010001000002280004a9368106'
packet = send_udp_message(message, "10.76.9.15", 53)

#Scenario 2
message = '02 02 00 00 00 02 00 00 0b 0b 0b 00 ff ff ff 00 00 00 00 00 00 00 00 10'
packet = send_udp_message(message, "172.24.4.11", 520)
