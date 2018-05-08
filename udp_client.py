#This is a gadget for sending UDP
# 1. Send UDP
# 2. configure the data size
# 3. configure the send interval
# 4. configure the dst addr
# 4.1 Unicast
# 4.2 Broadcast
# 4.3 Multicast
#-------------------------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Originated from https://github.com/michaelliao/learn-python3/blob/master/samples/socket/udp_client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # Send Data:
    s.sendto(data, ('127.0.0.1', 9999))
    # Recv data:
    print(s.recv(1024).decode('utf-8'))

s.close()
