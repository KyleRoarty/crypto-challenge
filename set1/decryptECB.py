#!/usr/bin/env python3

import cryptoHelpers as ch
from Crypto.Cipher import AES

def decryptECB(inFile, keystr):
    f = open(inFile, 'r').read()

    hex_in = ch.b64ToHex(f)

    hex_bytes = bytes.fromhex(hex_in)

    cipher = AES.new(keystr, AES.MODE_ECB)

    dec_bytes = cipher.decrypt(hex_bytes)

    return dec_bytes.decode('utf-8')
