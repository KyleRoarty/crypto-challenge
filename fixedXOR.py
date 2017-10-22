import cryptoHelpers as ch

def fixedXOR(hex_1, hex_2):
    hex_1 = hex_1 if ch.isHex(hex_1) else ch.asciiToHex(hex_1)
    hex_2 = hex_2 if ch.isHex(hex_2) else ch.asciiToHex(hex_2)

    if len(hex_1) != len(hex_2):
        return -1

    xor_hex_bits = ch.xorHex(hex_1, hex_2)

    return ch.binaryToHex(xor_hex_bits)
