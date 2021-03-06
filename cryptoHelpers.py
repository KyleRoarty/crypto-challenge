#!/usr/bin/env python3

import base64

''' Converts input hex string to bytes, returning -1 if input isn't hex     '''
def hexToBytes(in_str):
    try:
        return bytes.fromhex(in_str)
    except ValueError:
        return -1

''' Converts input bytes to hex, returns -1 if input isn't bytes            '''
''' Check for other exceptions?                                             '''
def bytesToHex(in_bytes):
    try:
        return in_bytes.hex()
    except AttributeError:
        return -1

''' Converts a string in b64 format to bytes, return -1 if input isn't      '''
''' valid unicode                                                           '''
def b64ToBytes(in_str):
    try:
        return base64.b64decode(in_str.encode('utf-8'))
    except (TypeError, UnicodeError) as e:
        return -1

''' Converts bytes to base 64 formatted string. Return -1 if bytes aren't   '''
''' in valid unicode format                                                 '''
def bytesTo64(in_bytes):
    try:
        return base64.b64encode(in_bytes).decode('utf-8')
    except (TypeError, UnicodeError) as e:
        return -1

''' Takes a string, returns bytes. Return -1 if string isn't valid unicode  '''
def strToBytes(in_str):
    try:
        return in_str.encode('utf-8')
    except (UnicodeError, AttributeError) as e:
        return -1
''' Takes bytes, return string. Return -1 if bytes don't decode to unicode  '''
def bytesToStr(in_bytes):
    try:
        return in_bytes.decode('utf-8')
    except (UnicodeError, AttributeError) as e:
        return -1

''' Filters out empty lines from an input file.read()                       '''
def neLines(f, nlines = False):
    lines = filter(None, (line.strip() for line in f))
    if nlines:
        ret_lines = [line+'\n' for line in lines]
        ret_lines[-1] = ret_lines[-1][:-1]
    else:
        ret_lines = [line for line in lines]

    return ret_lines

def parseInput(f_or_b, isFile, nlines = False):
    if isFile:
        f = open(f_or_b, 'r')
        return ''.join(neLines(f, nlines))
    else:
        return f_or_b

''' Rotates byte list by num, returns rotated list                          '''
def rotate(in_bytes, num):
    return in_bytes[num:]+in_bytes[:num]

''' Takes two bytestrings of equal length, xors them together               '''
def xorBytes(bs_1, bs_2):
    if len(bs_1) != len(bs_2):
        return -1

    return bytes([a^b for (a,b) in zip(bs_1, bs_2)])

''' Returns hamming dist (number of different bits of two strings           '''
def hammingDist(bs_1, bs_2):
    xord = xorBytes(bs_1, bs_2)
    return bin(int(bytesToHex(xord), base=16)).count('1')

def pkcs7(bs, pad_length):
    diff = (pad_length - len(bs) % pad_length) % pad_length
    if diff > 255:
        # Can't represent using pkcs
        return -1

    return bs + bytes([diff])*diff

