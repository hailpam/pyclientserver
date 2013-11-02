'''
Created on Aug 24, 2013

Settings module

@author: Paolo Maresca <plo.maresca@gmail.com>
'''


# Server bindings
SERVER_BINDING = {
    'address': '127.0.0.1',
    'port': '10000',
    'service_alias': 'JSON/TCP Server'
}


# Contextual settings
CONTEXT = {
    'debug': True,
    'client_socket_buffer': 8192,
    'compressed_content': False 
}


# Useful parameters for test purposes
TEST_PARAMS = {
    'path': '../data/',
    'file_name': 'test.txt'
}
