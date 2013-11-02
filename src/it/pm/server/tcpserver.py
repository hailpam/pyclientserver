'''
Created on Aug 20, 2013

Multithreaded TCP Server serving compressed JSON over TCP

@author: Paolo Maresca <plo.maresca@gmail.com>
'''

import SocketServer, time, gzip, sys

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
        self.__compressedcontent = CONTEXT['compressed_content']
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
            request.from_json(data)
            # Print data out, if debug
            if (self.__isdebug):
                print "Received data::", str(request)
            # Read lines from a text file
            resource = []
            resource.append(self.__resourcepath)
            resource.append(self.__filename)
            # Prepare the response data
            response = Data(True, [], 0)
            # Test if compressed content is needed
            list = []
            zippedfile = None
            testfile = None
            if (self.__compressedcontent):
                zippedfile = gzip.open(''.join(resource)+".gz", "r+")
                list = zippedfile.readlines()
                print "(Compressed) Content size [", sys.getsizeof(list), "]"
            else:
                testfile = open(''.join(resource), 'r')
                list = testfile.readlines()
                print "(Uncompressed) Content size [", sys.getsizeof(list), "]"
            response.vector = list
            response.nrbytes = int(sys.getsizeof(list))
            # Marshall JSON representation
            json_str = response.to_json()
            if (self.__isdebug):
                print "(Original) JSON Dimension::", sys.getsizeof(json_str)
            c_response = self.__compression.compress(json_str)
            if (self.__isdebug):
                print "(Compressed) JSON Dimension::", sys.getsizeof(c_response)
            start = time.time()
            self.request.sendall(c_response)
            print "[TCPRequestHandler][handle] Bunch of compressed data sent back!"
            end = time.time()
            if (self.__isdebug):
                print "Delivery::Time Elapsed::", str(end - start)
        except Exception, e:
            print "Exception upon message reception: ", e
        finally:
            if (testfile):
                testfile.close()
            if (zippedfile):
                zippedfile.close()

