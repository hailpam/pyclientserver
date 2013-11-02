'''
Created on Aug 20, 2013

System Data Model module

@author: Paolo Maresca <plo.maresca@gmail.com> 
'''


import json
import zlib

class Request(object):
    '''
     Define a simple request data type
    '''
    
    
    def __init__(self, name, code):
        '''
         Initialize Data instance
        '''
        
        self.name = name
        self.code = code
    
    
    def to_json(self):
        '''
         Convert this instance to its JSON representation
        '''
        
        self.__dict__['name'] = self.name
        self.__dict__['code'] = self.code
        
        return json.dumps(self.__dict__, indent=4)
    
    
    def from_json(self, sting):
        '''
         Conert the JSON representation to a this instance
        '''
        
        dict = json.loads(sting)
        self.__dict__ = dict
        self.name = dict['name'] 
        self.code = dict['code'] 
        
    def __str__(self):
        return str("request: "+str(self.name)+" - code: "+str(self.code))


class Data(object):
    '''
     Define a simple response data type (data centric)
    '''
    
    def __init__(self, outcome, vector, nr_of_bytes):
        '''
         Initialize Data instance
        '''
        
        self.outcome = outcome
        self.vector = vector
        self.nrbytes = nr_of_bytes
        
    
    def to_json(self):
        '''
         Convert this instance to its JSON representation
        '''
        
        self.__dict__['outcome'] = self.outcome
        self.__dict__['vector'] = self.vector
        self.__dict__['nrbytes'] = self.nrbytes
         
        return json.dumps(self.__dict__, indent = 4)
    
    
    def from_json(self, str):
        '''
         Conert the JSON representation to a this instance
        '''
        
        self.__dict__ = json.loads(str)
        self.outcome = self.__dict__['outcome']
        self.vector = self.__dict__['vector']
        self.nrbytes = self.__dict__['nrbytes']
        
        
    def __str__(self):
        return str("outcome: "+str(self.outcome)+" -nr of bytes: "+str(self.nrbytes)+" - vector: "+str(self.vector))
    
    
class Utility(object):
    '''
     Utility class mainly providing compression/decompression services
    '''
    
    def compress(self, data):
        '''
         Compress input text-based data in compressed byte representation
        '''
        string = str(data)
        
        return zlib.compress(string, zlib.Z_BEST_COMPRESSION)
    
    def decompress(self, data):
        '''
         Decompress an input compressed byte representation in its orgingal
         text-based data
        '''
        string = str(zlib.decompress(data))
        
        return string
