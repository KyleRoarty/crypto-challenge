#!/usr/bin/env python3

from singleXOR import singleByteDecrypt

def neLines(f):
    return filter(None, (line.strip() for line in f))

def detect(filename):
    f_point = open(filename, 'r')

    for line in neLines(f_point):
        x = singleByteDecrypt(line)
        if x is not None and x is not '':
            print(x)
