from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import time
PORT_NUMBER = 5000
SIZE = 128

hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Get the data from a server, on port {0}\n".format(PORT_NUMBER))

while True:
    (data,addr) = mySocket.recvfrom(SIZE)
    print(data.decode('utf-8'))
    
sys.exit()
time.sleep(3)
