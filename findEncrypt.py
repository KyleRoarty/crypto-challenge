#!/usr/bin/env python3

from singleXOR import singleByteDecrypt
import cryptoHelpers as ch

def detect(filename):
    f_point = open(filename, 'r')

    min_score = 1e309
    decrypt_str = ''

    for line in ch.neLines(f_point):
        x = singleByteDecrypt(line)
        if x is not None and x[0] is not '':
            print(x)
            if x[1] < min_score:
                decrypt_str = x[0]
                min_score = x[1]

    return decrypt_str
