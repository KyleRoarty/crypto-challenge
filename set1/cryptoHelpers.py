#!/usr/bin/env python3

def asciiToHex(ascii_str):
    hex_str = ''
    for char in ascii_str:
        hex_str += format(ord(char), '02x')
    return hex_str

def neLines(f):
    return filter(None, (line.strip() for line in f))
