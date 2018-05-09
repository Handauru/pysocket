#This is a gadget for sending UDP
# 1. Send UDP
# 2. configure the data size
# 3. configure the send interval
# 4. configure the dst addr
# 4.1 Unicast
# 4.2 Broadcast
# 4.3 Multicast
#---------------------------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Originated from https://github.com/michaelliao/learn-python3/blob/master/samples/socket/udp_server.py

import socket

#HOST = input('please enter the dst IP:')
#HOST = '127.0.0.1'
#c=type(HOST)
#print(c)
#PORT = int(input('please enter the dst port:'))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((HOST, PORT))

s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

# keep the port on listening
while True:
    # Recv data:
    data, addr = s.recvfrom(1024) # what's the 1024 for?
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8') # how to modify to what i wnat?
    s.sendto(reply.encode('utf-8'), addr)

