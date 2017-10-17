#!/usr/bin/env python3

import sys
import cryptoHelpers as ch
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

    hex_str = in_str if ch.isHex(in_str) else ch.asciiToHex(in_str)

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
        print(bit_str[-(len(bit_str) % 4)-4:])
        pad = -4 + ((len(b64_str) % 4)-2)*2
        print(pad)
        bit_str = bit_str[:pad]


    while len(bit_str) is not 0:
        hex_str += format(int(bit_str[:4], 2), '01x')
        bit_str = bit_str[4:]

    return hex_str
