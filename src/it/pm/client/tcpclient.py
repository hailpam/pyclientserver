'''
Created on Aug 20, 2013

TCP Client requesting and receiving compressed JSON over TCP

@author: Paolo Maresca <plo.maresca@gmail.com>
'''

import socket, time, threading, sys

from  it.pm.model.datamodel import Request, Data, Utility
from settings import CONTEXT, SERVER_BINDING
from threading import Thread


class TCPClient(threading.Thread):
    '''
     JSON/TCP client thread
    '''
    
    def __init__(self):
        '''
         Class constructor
        '''
        Thread.__init__(self)
        
        # Remote service bindings
        self.__serverhost = SERVER_BINDING['address']
        self.__serverport = int(SERVER_BINDING['port'])
        # Working mode
        self.__isdebug = CONTEXT['debug']
        # Buffer settings
        self.__bufferdim = int(CONTEXT['client_socket_buffer'])
        # Compression helper
        self.__compression = Utility()
        
    
    def run(self):
        '''
         Thread handler
        '''
        
        try:
            # Request creation
            data = Request('GET', 100)
            # Client socket binding
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.__serverhost, self.__serverport))
            # Sending JSON data over the socket
            sock.send(data.to_json())
            print "[TCPClient][run] Request sent..."
            start = time.time()
            response = self.__receive_data(sock)
            end = time.time()
            if (self.__isdebug):
                print "Reception::Time Elapsed::", str(end - start)
                print "(Compressed) Dimension::", sys.getsizeof(response)
            # Treating compressed data
            result = self.__compression.decompress(response)
            data = Data(False, [], 0)
            data.from_json(result)
            if (int(data.nrbytes) == sys.getsizeof(data.vector)):
                print "[TCPClient][run] Integrity is OK"
            print "[TCPClient][run] Data\n", str(data.vector[:2])
        except Exception, e:
            print "Error::NET::sending exception [", str(e), "]"
        finally:
            sock.close()

    
    def __receive_data(self, client_socket):
        '''
         Helper method: buffered network reader
        '''
        
        print "[TCPClient][run] ... Receiving response ..."
        data = ''
        while True:
            # Iteratively read the socket according to buffer size
            result = client_socket.recv(self.__bufferdim)
            if (not result):
                break
            data += result
        
        return data
