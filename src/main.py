'''
Created on Apr 20, 2012

@author: saeed
'''

from server import UdpServer

UDP_IP="192.168.1.7"
UDP_PORT=3000

server = UdpServer(UDP_IP,UDP_PORT)

while True:
    
    dataRaw = server.receiveData()
    
    if len(dataRaw) > 0:
        data = eval(dataRaw)
        ip = data["ip"]
        heading = data["heading"]
        s = '{"neck":' + str(heading / 2) + "}" 
        print(dataRaw + b"  ---->  " + bytes(s,"utf-8"))
        server.sendData(ip, s)
        #time.sleep( .2 )