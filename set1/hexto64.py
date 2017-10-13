#!/usr/bin/env python3

import sys
from argparse import ArgumentParser

BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def getArgs():
    parser = ArgumentParser()
    parser.add_argument('hexstr', type=str, action='store',
                        help='String of hex digits to be converted to base64')
    parser.add_argument('-s','--string', action='store_true',
                        help='Is the string an ASCII string?')

    return parser.parse_args()

def octetToChars(trip_oct, padding):
    rev_chars = []
    bits = int(trip_oct, 16)
    for x in range(0, padding):
        rev_chars.append(BASE64_CHARS[-1])
        bits = bits >> 6

    for x in range(padding, 4):
        rev_chars.append(BASE64_CHARS[bits & ~(-1 << 6)])
        bits = bits >> 6

    return reversed(rev_chars)

def hexTo64(hex_str):

    b64_str = []

    while len(hex_str) is not 0:
        padding = 0
        parse = hex_str[:6]
        if len(parse) is not 6:
            padding = int((6-len(parse))/2)
            parse += '0'*padding*2

        b64_str.extend(octetToChars(parse, padding))
        hex_str = hex_str[6:]

    return ''.join(b64_str)

def asciiToHex(ascii_str):
    hex_ret = []

    for c in ascii_str:
        hex_ret.append(format(ord(c), 'x'))

    return ''.join(hex_ret)

def main():
    args = getArgs()
    hex_str = args.hexstr

    if args.string:
        hex_str = asciiToHex(hex_str)

    print(hexTo64(hex_str))

if __name__ == '__main__':
    main()
