'''
Created on Apr 20, 2012

@author: saeed
'''

import socket
from message import Message

class Server:
    '''
    Server is a parent class that defines methods to send and receive data
     will include UdpServer, WebSocketServer, etc...
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    pass

class UdpServer(Server):

    def __init__(self, ip, port):
        Server.__init__(self, ip, port)
        self.sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
        self.sock.bind( (ip,port) )
        
    def __str__(self):
        return "UDP Server \n  IP: " + self.ip + "\n  PORT: " + str(self.port)

    def receiveData(self):
        data, addr = self.sock.recvfrom( 1024 )
        #prints a string but crashes on OSC msg
        #print("received: " + data.decode("utf-8"))
        m = Message()
        m.parse(data)
        return m
        
    def sendData(self, ip, message):
        self.sock.sendto( bytes(str(message),"utf-8") + b"\n", 0, (ip, 4000) )
    
    
##################    
# self-test code #
##################

if __name__ == '__main__':
    udp = UdpServer('192.168.1.7', 3000)
    print(udp)
    
    
    