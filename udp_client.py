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

# data should be added though GUI
for data in [b'Michael', b'Tracy', b'Sarah']:
    # Send Data:
    #k_ip = int(input('please enter the src IP:'))
	#k_pt = int(input('please enter the src port:'))
	s.sendto(data, (k_ip, k_pt))
	s.sendto(data, ('127.0.0.1', 9999))
    # Recv data:
    print(s.recv(1024).decode('utf-8'))

s.close()
