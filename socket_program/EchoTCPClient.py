#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

HOST, PORT = 'localhost', 5639
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(data + '\n')

    received = sock.recv(1024)
finally:
    sock.close()

print("Send:     %s" % (data))
print("received: %s" % (received))