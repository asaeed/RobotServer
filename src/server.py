'''
Created on Apr 20, 2012

@author: saeed
'''

import socket

class Server:
    '''
    Server is a parent class that defines methods to send and receive data
     will include UdpServer, WebSocketServer, etc...
    '''
    pass

class UdpServer(Server):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
        self.sock.bind( (ip,port) )
        
    def __str__(self):
        return "UDP Server \n  IP: " + self.ip + "\n  PORT: " + str(self.port)

    def receiveData(self):
        data, addr = self.sock.recvfrom( 1024 )
        #prints a string but crashes on OSC msg
        #print("received: " + data.decode("utf-8"))
    
        if data[0] == 123 and data[-1] == 125: #check for '{' and '}'
            return data
        
    def sendData(self, ip, data):
        self.sock.sendto( bytes(data,"utf-8") + b"\n", 0, (ip, 4000) )
    
if __name__ == '__main__':
    # self-test code
    udp = UdpServer('192.168.1.7', 3000)
    print(udp)
    
    
    