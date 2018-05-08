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

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind port & IP:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

while True:
    # Recv data:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)

