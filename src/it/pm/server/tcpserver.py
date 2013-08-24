'''
Created on Aug 20, 2013

Multithreaded TCP Server serving compressed JSON over TCP

@author: Paolo Maresca <plo.maresca@gmail.com>
'''

import SocketServer, time

from it.pm.model.datamodel import Request, Data, Utility
from settings import CONTEXT, SERVER_BINDING, TEST_PARAMS
from SocketServer import BaseRequestHandler


class TCPServer(SocketServer.ThreadingTCPServer):
    '''
     Multi-threaded TCP server
    '''
    
    allow_reuse_address = True
    print "### Compressed JSON over TCP is Up and Running..."
    print "    - Service alias [", SERVER_BINDING['service_alias'], "]"



class TCPRequestHandler(SocketServer.BaseRequestHandler):
    '''
     Specific JSON/TCP request handler
    '''
    
    def __init__(self, request, client_address, server):
        # Read configuration parameter
        self.__isdebug = CONTEXT['debug']
        # Compression Utility
        self.__compression = Utility()
        self.__client = client_address
        # Get test parameters
        self.__resourcepath = TEST_PARAMS['path']
        self.__filename = TEST_PARAMS['file_name']
        # Call father
        BaseRequestHandler.__init__(self, request, client_address, server)
        
    
    def handle(self):
        '''
         Service handler method
        '''
        
        try:
            print "[TCPRequestHandler][handle] Connection accepted... processing"
            # Reading request (assuming a small amount of bytes)
            data = self.request.recv(1024).strip()
            # Unmarshall the request
            request = Request('', 0)
            data = request.from_json(data)
            # Print data out, if debug
            if (self.__isdebug):
                print "Received data::", str(data)
            # Read lines from a text file
            resource = []
            resource.append(self.__resourcepath)
            resource.append(self.__filename)
            testfile = open(''.join(resource), 'r')
            # Prepare the response data
            response = Data(True, [], 0)
            list = testfile.readlines()
            response.vector = list
            response.nrbytes = len(list)
            # Marshall JSON representation
            json_str = response.to_json()
            if (self.__isdebug):
                print "(Original) Dimension::", len(json_str)
            c_response = self.__compression.compress(json_str)
            if (self.__isdebug):
                print "(Compressed) Dimension::", len(c_response)
            start = time.time()
            self.request.sendall(c_response)
            print "[TCPRequestHandler][handle] Bunch of compressed data sent back!"
            end = time.time()
            if (self.__isdebug):
                print "Delivery::Time Elapsed::", str(end - start)
        except Exception, e:
            print "Exception upon message reception: ", e
        finally:
            testfile.close()

