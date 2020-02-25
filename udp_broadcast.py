#coding=utf-8
from time import sleep
import socket
'''
udp broadcast packet generator:
input: 
1. Dst Port
2. pkts amount
3. pkts interval
'''
network = '<broadcast>'
MESSAGE = 'Msg Send!'
t = 0

DST_PORT = int(input('Destnation Port:'))
PKT_COUNT = int(input("pkts to send:"))
PKT_INTERVAL = int(input("time interval(>100ms) between pkts :"))/1000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while t < PKT_COUNT:
	s.sendto(MESSAGE.encode('utf-8'), (network, DST_PORT))
	t+=1
	print('Sending %s/%s pkt.' %(t, PKT_COUNT))
	sleep(PKT_INTERVAL)
