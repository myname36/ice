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

for host in hosts:
    # print(host)
    q = Queue()
    open_ports = []

    def port_scan(port):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((host, port))
            return True
        except:
            return False

    def filling(p_list):
        for port in p_list:
            q.put(port)

    def chandler():
        while not q.empty():
            port = q.get()
            if port_scan(port):
                # print(port)
                open_ports.append(port)

    p_list = range(1, 1024)
    filling(p_list)

    t_list = []
    for th in range(100):
        thread = threading.Thread(target=chandler)
        t_list.append(thread)

    for thread in t_list:
        thread.start()
    for thread in t_list:
        thread.join()

    comb = [host]

    for ha in open_ports:
        comb.append(ha)
    print(comb)
