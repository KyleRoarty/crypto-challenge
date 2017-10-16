#!/usr/bin/env python3

from fixedXOR import fixedXOR
import cryptoHelpers as ch
# from wikipedia, alphabetical order
CHAR_FREQ = (.08167,
             .01492,
             .02782,
             .04253,
             .12702,
             .02228,
             .02015,
             .06094,
             .06966,
             .00153,
             .00772,
             .04025,
             .02406,
             .06749,
             .07507,
             .01929,
             .00095,
             .05987,
             .06327,
             .09056,
             .02758,
             .00978,
             .02360,
             .00150,
             .01974,
             .00074)

def chiSquared(ascii_str):
    ascii_str_low = ascii_str.lower()
    str_len = 0
    char_counts = [0] * 26

    for char in ascii_str_low:
        if ord(char) >= 97 and ord(char) <= 122:
            char_counts[ord(char)-97] += 1
            str_len += 1

    exp_counts = [c*str_len for c in CHAR_FREQ]
    chi_sq = 0

    try:
        for act, exp in zip(char_counts, exp_counts):
            chi_sq += pow(act-exp, 2)/exp

        return chi_sq
    except ZeroDivisionError:
        return 1e309

def singleByteDecrypt(hex_str):
    min_val = 1e309
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

        chi_sq = chiSquared(ret_ascii_str)
        if chi_sq < min_val:
            min_val = chi_sq
            mv_string = ret_ascii_str
            mv_key = chr(i)

    return mv_string
