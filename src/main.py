'''
Created on Apr 20, 2012

@author: saeed
'''

from server import UdpServer
from message import Message
import globals

UDP_IP="192.168.1.7"
UDP_PORT=3000

server = UdpServer(UDP_IP,UDP_PORT)

while True:
    
    messageIn = server.receiveData()
    
    if (messageIn):
        ip = messageIn.ip
        heading = messageIn.heading
        messageOut = Message()
        #messageOut.neck = heading / 2
        if heading <= 180:
            messageOut.neck = globals.mapNum(heading, 0, 180, 180, 0)
        else:
            messageOut.neck = globals.mapNum(heading, 180, 360, 180, 0)
        print(str(messageIn) + "  ---->  " + str(messageOut))
        server.sendData(ip, messageOut)
        
        
        