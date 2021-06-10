import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time
import Adafruit_ADS1x15
SERVER_IP   = '192.168.1.232'
PORT_NUMBER = 5000
SIZE = 1024
adc = Adafruit_ADS1x15.ADS1115()
GAIN=1
values = [0]*100
value1=0
R2=33000.0
R1 = 68000.0
print ("Server sending packets to IP {0}, via port {1}\n".format(SERVER_IP,PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )

while True:
    for i in range(100):
        values[i] = adc.read_adc(0,gain=GAIN)+89
        value1=adc.read_adc(1,gain=1)
        print (max(values))
        voltage = (max(values)/1024.0)*3300
        print ("Voltage",round(voltage,1))
        vtg = ('Voltage = {} mV '.format(round(voltage,1)))
        current = ((voltage-1650)/0.185)
        print("Current",round(current,2))
        cur = ('Current = {} mA '.format(round(current,2)))
        mySocket.sendto(str(cur).encode('utf-8'),(SERVER_IP,PORT_NUMBER)) #Current measurement using ACS712
        mySocket.sendto(str(vtg).encode('utf-8'),(SERVER_IP,PORT_NUMBER)) # Voltage measurement using ACS712
        bvoltage=value1*(5.0/32768)*((R1+R2)/R2)-2.1 # For Battery Voltage using 9V battery
        print("External Battery:{} V".format(round(bvoltage,2)))
        bvtg=("External Battery:{} V".format(round(bvoltage,2)))
        mySocket.sendto(str(bvtg).encode('utf-8'),(SERVER_IP,PORT_NUMBER))
        time.sleep(3)
sys.exit()

