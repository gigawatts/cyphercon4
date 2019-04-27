import binascii
import serial
import time
port = "/dev/cu.usbmodem14101"
baud = 115200
ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
  print(ser.name + ' is open...')

r1="30 b1 30 b2 30 30 30 30 30 30 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 35 41 c6 c5 b4 c6 b1 41 b7 c6 30 30 b7 c6 30 30 b1 35 30 33 b1 39 8d 0a"
codes = [
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 30 30 30 30 30 30 30 30 30 30 30 30 b1 b1 b1 41 44 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 41 44 44 b1 c5 41 c3 c3 c5 35 35 c5 44 41 35 c3 b1 b1 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 44 c3 c6 c5 c5 44 42 30 42 30 44 c5 41 44 42 c5 c5 c6 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c3 30 c6 c6 c5 c5 b1 c5 41 44 c5 44 44 b1 c5 35 c5 b1 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 41 35 c3 b1 b1 44 b1 41 b1 41 c3 c3 c5 35 35 42 42 53 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 41 35 c3 b1 b1 b4 c5 41 35 c5 30 c6 41 c3 c3 c5 35 35 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 b1 30 41 44 c5 44 44 41 c6 c6 30 44 b1 b1 c6 b1 c6 30 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c5 b1 c6 c5 c3 35 41 c3 30 b7 41 42 b1 c5 c6 b1 b1 c5 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 42 41 30 42 41 42 44 b1 30 44 c5 c3 41 42 30 30 35 c5 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 42 33 b1 b1 b1 41 42 35 42 41 35 b1 c3 c3 41 42 41 b1 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 30 42 35 c5 35 35 c5 44 30 44 44 42 41 b1 b1 c3 41 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 35 30 b1 b1 44 b1 c6 b1 c5 44 35 30 44 41 c3 30 44 41 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c3 30 44 b1 c6 b1 c5 44 42 41 35 c5 b1 36 42 b1 30 42 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c3 30 44 c5 44 b1 35 c3 b1 30 35 c5 44 b1 30 c3 41 b1 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c6 30 35 35 b1 b1 b1 35 c5 44 35 c3 35 b1 44 b1 35 c3 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 b1 c3 c5 c6 41 b1 b1 c6 b1 c5 b1 44 30 c6 c6 b1 c3 c5 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 b1 30 30 35 c5 b1 c5 41 c6 44 b1 35 42 c5 b1 b1 c5 c6 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 30 35 35 b1 c6 b1 c5 44 c6 b1 44 44 b1 c5 42 41 c3 c3 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c6 b1 30 30 44 c5 44 30 41 35 b1 35 35 c5 41 b1 c5 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 35 41 c6 c5 b1 b1 c6 c5 35 b1 b2 c5 35 30 b1 41 c3 c5 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 44 c5 c3 30 44 c5 35 c5 c5 44 c5 44 c6 41 c3 41 44 c5 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c6 41 b1 35 b1 c6 b1 41 42 b1 c5 b4 41 b1 b1 b1 c5 35 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b2 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 42 b1 30 30 44 b1 c5 35 35 b1 b1 c6 c5 42 b1 30 30 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b2 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 42 41 44 c3 c5 b1 b1 c6 c5 42 c5 44 41 b2 b2 b1 c5 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 33 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 c5 35 c3 41 b1 41 b7 33 b1 30 c3 41 b1 35 41 b1 35 41 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 33 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 b1 30 41 44 c6 b1 b1 c5 30 c6 c6 44 b1 35 c3 c5 30 c6 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 30 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 41 b1 b1 c3 c5 44 44 30 35 c5 44 42 30 42 c3 30 b1 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 30 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 41 35 35 35 41 b1 b1 41 42 b1 c5 c3 b1 41 35 35 b1 c3 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 44 b1 41 42 30 b1 b1 c3 41 b1 b1 c3 44 30 30 44 41 44 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 44 c5 c3 b1 41 35 35 b1 c6 b1 c5 44 c6 b1 b1 c5 30 b1 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 30 c6 c6 b1 c3 b1 41 b1 c3 41 42 b1 c5 c6 b1 b1 c5 35 30 33 b1 39 8d 0a",
"30 b1 30 b2 30 b1 30 b4 b4 36 c5 56 c9 cc a0 4d cf 47 a0 a0 a0 a0 a0 35 30 c3 b1 41 42 b1 c5 b1 35 c5 c3 c3 c3 b2 30 b1 39 30 33 b1 39 8d 0a"
]

time.sleep(1)
for code in codes:
  time.sleep(1)
  ser.write(code)
  ser.write('\n\r')
  time.sleep(2)
  print code
