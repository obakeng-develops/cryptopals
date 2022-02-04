# Cryptopals, Set 1, Challenge 2
# Obakeng Mosadi, 2022
import base64
from itertools import cycle


def fixed_xor(stringOne, stringTwo):

    stringOneByteArray = bytearray.fromhex(stringOne)
    stringTwoByteArray = bytearray.fromhex(stringTwo)

    base64StringOne = base64.b64encode(stringOneByteArray)
    base64StringTwo = base64.b64encode(stringTwoByteArray)

    if len(stringOneByteArray) != len(stringTwoByteArray):
        print("Buffers are not of equal-length")

    xored = bytes(a ^ b
                  for (a, b) in zip(base64StringOne, cycle(base64StringTwo)))


fixed_xor("1c0111001f01010006", "1a024b53535009181c")
