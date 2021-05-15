from scapy.all import ARP, Ether, srp
import socket
import argparse
import socket
import threading
from queue import Queue


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ran = (s.getsockname()[0])
my = ran[0:11]+"1/24"
s.close()


target = my
# make the ARP packet
arp = ARP(pdst=target)
# ether packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# the packet
packet = ether/arp

result = srp(packet, timeout=4, verbose=0)[0]

hosts = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    hosts.append(received.psrc)

print(hosts)
