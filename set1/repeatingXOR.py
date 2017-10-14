#!/usr/bin/env python3

from fixedXOR import fixedXOR
from math import ceil
import cryptoHelpers as ch

def repeatingXOR(str_in, key):
    b_key = ''
    hex_str = ''

    b_key = ch.asciiToHex(key)
    hex_str = ch.asciiToHex(str_in)

    ext_key = b_key*ceil(len(hex_str)/len(b_key))
    if len(ext_key) is not len(hex_str):
        ext_key = ext_key[:len(hex_str)-len(ext_key)]
    print(fixedXOR(hex_str, ext_key))
