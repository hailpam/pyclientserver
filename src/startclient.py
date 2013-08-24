'''
Created on Aug 24, 2013

JSON/TCP client main process

@author: Paolo Maresca <plo.maresca@gmail.com>
'''


from it.pm.client.tcpclient import TCPClient


def main():
    # Creating the client thread
    client = TCPClient()
    client.start()
    
    # Wait until the end of processing
    client.join()


if __name__ == '__main__':
    main()