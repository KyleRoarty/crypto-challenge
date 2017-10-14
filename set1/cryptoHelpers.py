#!/usr/bin/env python3

def asciiToHex(ascii_str):
    hex_str = ''
    for char in ascii_str:
        hex_str += format(ord(char), '02x')
    return hex_str

def neLines(f):
    return filter(None, (line.strip() for line in f))

def hexToBinary(hex_str):
    return format(int(hex_str, 16), "0{}b".format(len(hex_str)*4))

def isHex(str_1):
    try:
        int(str_1, 16)
    except ValueError:
        return False

    return True

def hammingDist(hex_1, hex_2):

    hex_1 = hex_1 if isHex(hex_1) else asciiToHex(hex_1)
    hex_2 = hex_2 if isHex(hex_2) else asciiToHex(hex_2)

    bin_1 = hexToBinary(hex_1)
    bin_2 = hexToBinary(hex_2)

    bin_xor = format(int(bin_1, 2) ^ int(bin_2, 2), '0{}b'.format(len(bin_1)))

    return bin_xor.count('1')
