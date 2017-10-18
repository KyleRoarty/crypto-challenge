#!/usr/bin/env python3

import cryptoHelpers as ch
import hexto64
import singleXOR
import repeatingXOR

def decryptRepeatingXOR(filename):
    f = open(filename, 'r').read().strip().replace('\n','')
    print(f)
    hex_str2 = hex_str = hexto64.b64ToHex(f)

    key_hdist = []

    for i in range(2, 41):
        j = i*8
        hdist = ch.hammingDist(hex_str[:j], hex_str[j:2*j])/i
        key_hdist.append((i, hdist))

    key_hdist.sort(key=lambda tup: tup[1])

    print(key_hdist[0])
    split_str = []
    for i in range(0, key_hdist[0][0]):
        split_str.append(''.join([hex_str[j:j+2] for j in range(2*i, len(hex_str), 2*key_hdist[0][0])]))

    key = ''
    for sub_str in split_str:
        key += singleXOR.singleByteDecrypt(sub_str)[1]

    print(key)
    return ch.hexToAscii(repeatingXOR.repeatingXOR(hex_str2, key))
