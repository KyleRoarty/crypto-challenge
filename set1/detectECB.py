#!/usr/bin/env python3

import cryptoHelpers as ch

def detectECB(infile):
    f = open(infile, 'r')

    lines = ch.neLines(f)

    lines_bytes = [bytes.fromhex(l) for l in lines]

    is_encrypted = []

    for l in lines_bytes:
        split_l = [l[i:i+16] for i in range(0, len(l), 16)]
        unique = set(split_l)

        if len(split_l) != len(unique):
            is_encrypted.append(True)
        else:
            is_encrypted.append(False)

    return [lines_bytes[i].hex() for i,v in enumerate(is_encrypted) if v is True]
