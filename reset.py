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
