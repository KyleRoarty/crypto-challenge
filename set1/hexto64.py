#!/usr/bin/env python3

import sys
import cryptoHelpers as ch
BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def _octetToChars(trip_oct, padding):
    rev_chars = []
    bits = int(trip_oct, 16)

    for x in range(0, padding):
        rev_chars.append(BASE64_CHARS[-1])
        bits = bits >> 6

    for x in range(padding, 4):
        rev_chars.append(BASE64_CHARS[bits & ~(-1 << 6)])
        bits = bits >> 6

    return reversed(rev_chars)

def hexTo64(in_str):
    try:
        int(in_str, 16)
        hex_str = in_str
    except ValueError:
        try:
            in_str.encode('ascii')
            hex_str = ch.asciiToHex(in_str)
        except UnicodeEncodeError:
            return -1

    b64_str = []

    while len(hex_str) is not 0:
        padding = 0
        parse = hex_str[:6]
        if len(parse) is not 6:
            padding = int((6-len(parse))/2)
            parse += '0'*padding*2

        b64_str.extend(_octetToChars(parse, padding))
        hex_str = hex_str[6:]

    return ''.join(b64_str)
