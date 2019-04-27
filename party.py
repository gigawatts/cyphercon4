import binascii
import serial
import time
import argparse
import sys

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Some script')
    parser.add_argument('-D', '--device', help='serial port device', default='/dev/ttyACM0')
    results = parser.parse_args(args)
    return (results.device)

device = check_arg(sys.argv[1:])

baud = 115200
ser = serial.Serial(device, baud, timeout=1)
if ser.isOpen():
  print(ser.name + ' is open...')

d1="30 b1 30 b2 30 33 30 30 30 b1 d7 c9 d2 c5 b1 a0 a0 a0 a0 a0 a0 a0 a0 30 b1 b2 33 b4 35 36 b7 b8 39 41 42 c3 44 c5 c6 30 b1 30 33 b1 39 8d 0a"
d2="30 b1 30 b2 30 30 30 30 30 b1 d7 c9 d2 c5 b2 a0 a0 a0 a0 a0 a0 a0 a0 c6 c5 41 44 c3 30 c5 44 35 c3 41 c6 c5 42 c5 c5 c6 35 30 33 b1 39 8d 0a"
d3="30 b1 30 b2 30 b2 30 30 30 b1 d7 c9 d2 c5 b2 a0 a0 a0 a0 a0 a0 a0 a0 42 30 42 30 35 c6 41 c3 c5 b8 42 41 44 c6 30 30 44 35 30 33 b1 39 8d 0a"
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

ser.write(d1)
ser.write('\n\r')
time.sleep(2)
line=ser.readline()
line2=ser.readline()
line3=ser.readline()
time.sleep(2)

ser.write(d2)
ser.write('\n\r')
time.sleep(2)
line=ser.readline()
line2=ser.readline()
line3=ser.readline()
time.sleep(2)

ser.write(d3)
ser.write('\n\r')
time.sleep(2)
line=ser.readline()
line2=ser.readline()
line3=ser.readline()
