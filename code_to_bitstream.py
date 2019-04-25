import binascii

codes = [
"0102030001WIRE1        0123456789ABCDEF010319",
"0102000001WIRE2        FEADC0ED5CAFEBEEF50319",
"0102020001WIRE2        B0B05FACE8BADF00D50319"
]


def parity_brute_force(x):
    bit = 0
    num_bits = 0
    while x:
        bitmask = 1 << bit
        bit += 1
        if x & bitmask:
            num_bits += 1
        x &= ~bitmask

    return num_bits % 2

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def toggleBit(int_type, offset):
  mask = 1 << offset
  return(int_type ^ mask)



for code in codes:
  string_code = ""
  for code_c in code:
    code_b = text_to_bits(code_c)
    code_i = int(code_b, 2)
    code_p = parity_brute_force(code_i)
    if code_p == 1:
      #code_b = code_b + 128
      string_code = string_code + str(hex(code_i + 128)[2:]) + " "
    if code_p == 0:
      string_code = string_code + str( hex(code_i)[2:]) + " "
  print string_code + "8d 0a"
