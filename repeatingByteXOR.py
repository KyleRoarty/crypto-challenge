#!/usr/bin/env python

from math import ceil
import cryptoHelpers as ch

def repeatingByteEncrypt(filename, key_bytes):
    f = open(filename, 'r')
    f_ne = [x+'\n' for x in ch.neLines(f)]
    len_f = len(f_ne)
    enc_bytes = []
    rot = 0
    count = 1


    for line in f_ne:
        if count == len_f:
            line = line[:-1]
        line_bytes = ch.strToBytes(line)

        ext_key = ch.rotate(key_bytes, rot)*ceil(len(line_bytes)/len(key_bytes))
        if len(ext_key) != len(line_bytes):
            ext_key = ext_key[:len(line_bytes)-len(ext_key)]
        print(line_bytes)
        print(ext_key)
        enc_bytes.append(ch.xorBytes(line_bytes, ext_key))
        rot = (rot + len(ext_key)%len(key_bytes)) % len(key_bytes)
        count+=1

    return enc_bytes
