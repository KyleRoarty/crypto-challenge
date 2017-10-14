#!/usr/bin/env python3

from fixedXOR import fixedXOR
import cryptoHelpers as ch
# from wikipedia
CHAR_FREQ = {'a':8.167,
             'b':1.492,
             'c':2.782,
             'd':4.253,
             'e':12.702,
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
             'z':0.074,
             'A':8.167*.11682,
             'B':1.492*.04434,
             'C':2.782*.05238,
             'D':4.253*.03174,
             'E':12.702*.02799,
             'F':2.228*.04027,
             'G':2.015*.01642,
             'H':6.094*.042,
             'I':6.966*.0729,
             'J':0.153*.005,
             'K':0.772*.00456,
             'L':4.025*.02415,
             'M':2.406*.0382,
             'N':6.749*.02284,
             'O':7.507*.07631,
             'P':1.929*.0431,
             'Q':0.095*.00222,
             'R':5.987*.02826,
             'S':6.327*.06686,
             'T':9.056*.15978,
             'U':2.758*.0118,
             'V':0.978*.00824,
             'W':2.360*.05497,
             'X':0.150*.00045,
             'Y':1.974*.00763,
             'Z':0.074*.00045}

def _valueString(ascii_str):
    ascii_str_low = ''.join(ascii_str.split())
    value = 0
    for char in ascii_str_low:
        try:
            value += CHAR_FREQ[char]
        except KeyError:
            value -= 3.84

    return value/len(ascii_str_low)

def singleByteDecrypt(hex_str):
    max_val = 0
    mv_string = ''
    mv_key = ''

    extend = int(len(hex_str)/2)

    for i in range(0, 128):
        ret_hex_str = fixedXOR(hex_str, format(i, '02x')*extend)
        try:
            ret_bytes = bytearray.fromhex(ret_hex_str)
            ret_ascii_str = ret_bytes.decode('ascii')
        except (UnicodeDecodeError, TypeError) as e:
            #print(e)
            continue

        value = _valueString(ret_ascii_str)
        if value > max_val:
            max_val = value
            mv_string = ret_ascii_str
            mv_key = chr(i)

    #print(mv_key)
    return mv_string
