import socket
import time
import math

UDP_IP="192.168.1.7"
UDP_PORT=3000

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sock.bind( (UDP_IP,UDP_PORT) )

while True:
    dataRaw, addr = sock.recvfrom( 1024 )
    #prints a string but crashes on OSC msg
    #print("received: " + data.decode("utf-8"))
    
    if dataRaw[0] == 123 and dataRaw[-1] == 125: #check for '{' and '}'
        data = eval(dataRaw)
        ip = data["ip"]
        heading = data["heading"]
        s = '{"neck":' + str(heading / 2) + "}" 
        print(dataRaw + b"  ---->  " + bytes(s,"utf-8"))
        if len(dataRaw) > 0:
            sock.sendto( bytes(s,"utf-8") + b"\n", 0, (ip, 4000) )
            #time.sleep( .2 )