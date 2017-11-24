#!/usr/bin/env python

from math import ceil
from singleByteXOR import singleByteDecrypt
import cryptoHelpers as ch

def repeatingByteEncrypt(in_data, isFile, key_bytes):
    in_str = ch.parseInput(in_data, isFile, True)
    line_bytes = ch.strToBytes(in_str)
    if line_bytes == -1:
        line_bytes = in_str

    ext_key = key_bytes*ceil(len(line_bytes)/len(key_bytes))
    if len(ext_key) != len(line_bytes):
        ext_key = ext_key[:len(line_bytes)-len(ext_key)]
    enc_bytes = ch.xorBytes(line_bytes, ext_key)

    return enc_bytes

def repeatingByteDecrypt(filename):
    f = open(filename, 'r')
    f_line = ''.join(ch.neLines(f))
    f_bytes = ch.b64ToBytes(f_line)

    ''' Array of tuples of the # of bytes, and hamming distance of the first'''
    ''' i bytes, and second i bytes                                         '''
    key_hdist = []

    for i in range(2, 41):
        ''' No clue why *4 is needed, but it is...                          '''
        hdist = ch.hammingDist(f_bytes[:i*4], f_bytes[i*4:4*2*i])/i
        key_hdist.append((i, hdist))

    key_hdist.sort(key=lambda tup: tup[1])
    min_hdist = key_hdist[0][0]
    split_bytes = []
    for i in range(0, min_hdist):
        split_bytes.append(f_bytes[i:len(f_bytes):min_hdist])

    key = b''
    for sub_bytes in split_bytes:
        key += singleByteDecrypt(sub_bytes)[2]

    return repeatingByteEncrypt(f_bytes, False, key)
