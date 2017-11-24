#!/usr/bin/env python3

import cryptoHelpers as ch
from Crypto.Cipher import AES

def decryptECB(in_data, isFile, key_bytes):
    if isFile:
        in_bytes = ch.b64ToBytes(ch.parseInput(in_data, isFile, False))
    else:
        in_bytes = in_data

    cipher = AES.new(key_bytes, AES.MODE_ECB)

    return cipher.decrypt(in_bytes)

def detectECB(in_file):
    f = open(in_file, 'r').read().splitlines()

    f_bytes = [ch.hexToBytes(l) for l in f]

    is_encrypted = []

    for l in f_bytes:
        split_l = [l[i:i+16] for i in range(0, len(l), 16)]
        unique = set(split_l)

        if len(split_l) != len(unique):
            is_encrypted.append(True)
        else:
            is_encrypted.append(False)

    return [ch.bytesToHex(f_bytes[i]) for i,v in enumerate(is_encrypted) if v is True]


