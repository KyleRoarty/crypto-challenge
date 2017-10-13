#!/usr/bin/env python3

from fixedXOR import fixedXOR

# from wikipedia
CHAR_FREQ = {'a':8.167,
             'b':1.492,
             'c':2.782,
             'd':4.253,
             'e':2.702,
             'f':2.228,
             'g':2.015,
             'h':6.094,
             'i':6.966,
             'j':0.153,
             'k':0.772,
             'l':4.025,
             'm':2.406,
             'n':6.749,
             'o':7.507,
             'p':1.929,
             'q':0.095,
             'r':5.987,
             's':6.327,
             't':9.056,
             'u':2.758,
             'v':0.978,
             'w':2.360,
             'x':0.150,
             'y':1.974,
             'z':0.074}

def _valueString(ascii_str):
    ascii_str_low = ascii_str.lower()
    value = 0
    for char in ascii_str_low:
        try:
            value += CHAR_FREQ[char]
        except KeyError:
            value += 0

    return value

def singleByteDecrypt(hex_str):
    searchstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    max_val = 0
    mv_string = ''
    mv_key = ''

    extend = int(len(hex_str)/2)

    for letter in searchstring:
        ret_hex_str = fixedXOR(hex_str, format(ord(letter), 'x')*extend)
        try:
            ret_bytes = bytearray.fromhex(ret_hex_str)
            ret_ascii_str = ret_bytes.decode('ascii')
        except UnicodeDecodeError:
            print("Uh oh...")
            return -1

        value = _valueString(ret_ascii_str)
        if value > max_val:
            max_val = value
            mv_string = ret_ascii_str
            mv_key = letter

    return mv_string
