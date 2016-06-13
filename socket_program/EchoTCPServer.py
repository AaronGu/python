#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver

class EchoRequestHandler(socketserver.StreamRequestHandler):
    """ demo request handler """

    def handle(self):
        self.data = self.rfile.readline().strip()
        print("%s write: %s" % (self.client_address, self.data))
        self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = 'localhost', 5639

    server = socketserver.TCPServer((HOST, PORT), EchoRequestHandler)
    print("ECHO TCP server is running ...")
    server.serve_forever()