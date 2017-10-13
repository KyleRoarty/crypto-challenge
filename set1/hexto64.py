#!/usr/bin/env python3

import sys
from argparse import ArgumentParser

BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def getArgs():
    parser = ArgumentParser()
    parser.add_argument('hexstr', type=str, action='store',
                        help='String of hex digits to be converted to base64')

    return parser.parse_args()

def hexTo64(hex_str):
    if len(hex_str) % 4 is not 0:
        print("Not implemented, lol")
        sys.exit(1)

    b64_str = []

    while len(hex_str) is not 0:
        conv_chars = int(hex_str[:3], 16)
        b64_str.append(BASE64_CHARS[conv_chars >> 6])
        b64_str.append(BASE64_CHARS[conv_chars & ~(-1 << 6)])
        hex_str = hex_str[3:]

    return ''.join(b64_str)

def main():
    args = getArgs()
    print(hexTo64(args.hexstr))

if __name__ == '__main__':
    main()
