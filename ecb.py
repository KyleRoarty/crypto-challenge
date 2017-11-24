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
