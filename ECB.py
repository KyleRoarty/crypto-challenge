#!/usr/bin/env python3

import cryptoHelpers as ch
from Crypto.Cipher import AES


def setupECB(inFile, asc,  keystr):
    f = ch.neLines(open(inFile, 'r').read())
    hex_in = ch.asciiToHex(f) if asc else ch.b64ToHex(f)

    hex_bytes = bytes.fromhex(hex_in)

    cipher = AES.new(keystr, AES.MODE_ECB)

    return [cipher, hex_bytes]

def decryptECB(inFile, keystr):

    [cipher, hex_bytes] = setupECB(inFile, False, keystr)

    dec_bytes = cipher.decrypt(hex_bytes)

    return dec_bytes.decode('utf-8')

def encryptECB(inFile, keystr):

    [cipher, hex_bytes] = setupECB(inFile, True, keystr)

    dec_bytes = cipher.encrypt(hex_bytes)

    return ch.hexTo64(dec_bytes.hex())
