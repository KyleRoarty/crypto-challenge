#!/usr/bin/env python3

from fixedXOR import fixedXOR
from math import ceil
import cryptoHelpers as ch

def repeatingXOR(str_in, key):
    hex_str = str_in if ch.isHex(str_in) else ch.asciiToHex(str_in)
    b_key = key if ch.isHex(key) else ch.asciiToHex(key)

    ext_key = b_key*ceil(len(hex_str)/len(b_key))
    if len(ext_key) is not len(hex_str):
        ext_key = ext_key[:len(hex_str)-len(ext_key)]

    return fixedXOR(hex_str, ext_key)

