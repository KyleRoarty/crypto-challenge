#!/usr/bin/env python3

import cryptoHelpers as ch
import hexto64
import singleXOR

def decryptRepeatingXOR(filename):
    f = open(filename, 'r').read().strip()
    hex_str = hexto64.b64ToHex(f)

    key_len = 0
    min_hdist = 1e309

    for i in range(2, 41):
        hdist = ch.hammingDist(hex_str[:i], hex_str[i:2*i])/i
        if hdist < min_hdist:
            min_hdist = hdist
            key_len = i


