import binascii
import serial
import time
port = "/dev/cu.usbmodem14101"
baud = 115200
ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
  print(ser.name + ' is open...')

r1="30 b1 30 b2 30 30 30 30 30 30 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 35 41 c6 c5 b4 c6 b1 41 b7 c6 30 30 b7 c6 30 30 b1 35 30 33 b1 39 8d 0a"
line=ser.readline()
line2=ser.readline()
line3=ser.readline()
ser.write(r1)
ser.write('\n\r')
time.sleep(2)
line=ser.readline()
line2=ser.readline()
line3=ser.readline()
time.sleep(2)
