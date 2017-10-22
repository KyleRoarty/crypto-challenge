#!/usr/bin/env python3

def pad(string, blk_len):
    str_bytes = string.encode('utf-8')

    diff = len(str_bytes) % blk_len

    if diff == 0:
        return string
    else:
        diff = blk_len - diff
        return (str_bytes+bytes([diff])*diff).decode('utf-8')
