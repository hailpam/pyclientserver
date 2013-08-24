'''
Created on Aug 24, 2013

Start TCP server main process

@author: Paolo Maresca <plo.maresca@gmail.com>
'''


from it.pm.server.tcpserver import TCPServer, TCPRequestHandler
from settings import SERVER_BINDING

def main():
    server = TCPServer((SERVER_BINDING['address'], int(SERVER_BINDING['port'])), TCPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()