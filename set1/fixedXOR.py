
HEX_CHARS = '0123456789abcdef'

def _hexCharToBinary(char):
    int_char = int(char, 16)
    bit_arr = []

    for i in range(0, 4):
        bit_arr.insert(0, int_char & 1)
        int_char = int_char >> 1

    return bit_arr

def _hexStrToBinary(hex_str):
    ret_arr = []
    for c in hex_str:
        ret_arr += _hexCharToBinary(c)

    return ret_arr

def _binStrXOR(bin_1, bin_2):
    ret_arr = []

    for i in range(0, len(bin_1)):
        ret_arr.append(bin_1[i] ^ bin_2[i])

    return ret_arr

def _binStrToHexChar(bin_1):
    hex_char = 0

    for c in bin_1:
        hex_char = (hex_char << 1) | c

    return HEX_CHARS[hex_char]

def _binStrToHex(bin_1):
    ret_arr = []

    while len(bin_1) is not 0:
        sub_bin_str = bin_1[:4]
        ret_arr.append(_binStrToHexChar(sub_bin_str))
        bin_1 = bin_1[4:]

    return ''.join(ret_arr)

def fixedXOR(hex_1, hex_2):
    try:
        int(hex_1, 16)
        int(hex_2, 16)
    except ValueError:
        return -1

    if len(hex_1) is not len(hex_2):
        return -2


    hex_bits_1 = _hexStrToBinary(hex_1)
    hex_bits_2 = _hexStrToBinary(hex_2)

    xor_hex_bits = _binStrXOR(hex_bits_1, hex_bits_2)

    print(_binStrToHex(xor_hex_bits))
