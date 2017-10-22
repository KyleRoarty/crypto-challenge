#!/usr/bin/env python3

from fixedXOR import fixedXOR
import cryptoHelpers as ch
# from wikipedia, alphabetical order
CHAR_FREQ_SP = (0.0651738, 0.0124248, 0.0217339, 0.0349835,
                0.1041442, 0.0197881, 0.0158610, 0.0492888,
                0.0558094, 0.0009033, 0.0050529, 0.0331490,
                0.0202124, 0.0564513, 0.0596302, 0.0137645,
                0.0008606, 0.0497563, 0.0515760, 0.0729357,
                0.0225134, 0.0082903, 0.0171272, 0.0013692,
                0.0145984, 0.0007836, 0.1918182)

CHAR_FREQ = (0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
             0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
             0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
             0.00978, 0.02360, 0.00150, 0.01974, 0.00074)

FREQ_SW = CHAR_FREQ_SP

def chiSquared(ascii_str):
    ascii_str_low = ascii_str.lower()
    str_len = 0
    char_counts = [0] * 27

    for char in ascii_str_low:
        if ord(char) == 9 or ord(char) == 10 or ord(char) == 13 or ord(char) == 32:
            char_counts[26] += 1
            str_len += 1
            pass
        elif ord(char) > 126 or ord(char) < 32:
            return 1e309
        elif ord(char) >= 97 and ord(char) <= 122:
            char_counts[ord(char)-97] += 1
            str_len += 1

    exp_counts = [c*str_len for c in FREQ_SW]
    chi_sq = 0

    try:
        for act, exp in zip(char_counts, exp_counts):
            chi_sq += pow(act-exp, 2)/exp

        return chi_sq/str_len
    except ZeroDivisionError:
        return 1e309

def singleByteDecrypt(hex_str):
    min_val = 1e309
    mv_string = ''
    mv_key = ''

    extend = len(hex_str)//2

    for i in range(0, 128):
        ret_hex_str = fixedXOR(hex_str, format(i, '02x')*extend)
        if ch.isHex(ret_hex_str):
            ret_ascii_str = ch.hexToAscii(ret_hex_str)
        else:
            continue

        chi_sq = chiSquared(ret_ascii_str)
        if chi_sq < min_val:
            min_val = chi_sq
            mv_string = ret_ascii_str
            mv_key = chr(i)

    return [mv_string, mv_key, min_val]
