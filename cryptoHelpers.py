#!/usr/bin/env python3

BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
def _octetToChars(trip_oct, padding):
    rev_chars = ''
    bits = int(trip_oct, 16)

    for x in range(0, padding):
        rev_chars = BASE64_CHARS[-1] + rev_chars
        bits = bits >> 6

    for x in range(padding, 4):
        rev_chars = BASE64_CHARS[bits & ~(-1 << 6)] + rev_chars
        bits = bits >> 6

    return rev_chars

def hexTo64(in_str):

    hex_str = in_str if isHex(in_str) else asciiToHex(in_str)

    b64_str = ''

    while len(hex_str) is not 0:
        padding = 0
        parse = hex_str[:6]
        if len(parse) is not 6:
            padding = int((6-len(parse))/2)
            parse += '0'*padding*2

        b64_str +=_octetToChars(parse, padding)
        hex_str = hex_str[6:]

    return b64_str

def b64ToHex(b64_str):

    b64_str = b64_str.replace('=','')
    b64_str = b64_str.replace('\n','')
    bit_str = ''
    hex_str = ''


    for char in b64_str:
        try:
            bit_str += format(BASE64_CHARS.index(char), '06b')
        except ValueError:
            pass

    if len(b64_str) % 4 is not 0:
        pad = -4 + ((len(b64_str) % 4)-2)*2
        bit_str = bit_str[:pad]


    while len(bit_str) is not 0:
        hex_str += format(int(bit_str[:4], 2), '01x')
        bit_str = bit_str[4:]

    return hex_str

def neLines(f):
    return filter(None, (line.strip() for line in f))

def asciiToHex(ascii_str):
    hex_str = ''
    for char in ascii_str:
        hex_str += format(ord(char), '02x')
    return hex_str

def hexToAscii(hex_str):
    return ''.join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])

def hexToBinary(hex_str):
    return format(int(hex_str, 16), "0{}b".format(len(hex_str)*4))

def binaryToHex(bin_str):
    if len(bin_str)/4 == len(bin_str)//4:
        return format(int(bin_str, 2), "0{}x".format(len(bin_str)//4))
    else:
        # ValueError occurs when bin_str isn't divisible by 4
        return -1

def isHex(str_1):
    try:
        int(str_1, 16)
    except ValueError:
        return False

    return False if (str_1 == '' or str_1 == None) else True

def hammingDist(hex_1, hex_2):
    return xorHex(hex_1, hex_2).count('1')

def xorHex(hex_1, hex_2):

    hex_1 = hex_1 if isHex(hex_1) else asciiToHex(hex_1)
    hex_2 = hex_2 if isHex(hex_2) else asciiToHex(hex_2)

    bin_1 = hexToBinary(hex_1)
    bin_2 = hexToBinary(hex_2)

    return format(int(bin_1, 2) ^ int(bin_2, 2), '0{}b'.format(len(bin_1)))


