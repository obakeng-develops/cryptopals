# Cryptopals, Set 1, Challenge 2
# Obakeng Mosadi, 2022
import base64
from itertools import cycle


def fixed_xor(stringOne, stringTwo):

    binaryOne = bin(int(stringOne, 16))[2:]
    binaryTwo = bin(int(stringTwo, 16))[2:]

    checkLength = len(binaryOne) if len(
        binaryOne) > len(binaryTwo) else len(binaryTwo)

    binaryOne = binaryOne.zfill(checkLength)
    binaryTwo = binaryTwo.zfill(checkLength)

    xor_combination = [int(a) ^ int(b) for (a, b) in zip(binaryOne, binaryTwo)]

    stringResult = "".join([str(bits) for bits in xor_combination])

    final = hex(int(stringResult, 2))[2:]

    print(final)


fixed_xor("1c0111001f010100061a024b53535009181c",
          "686974207468652062756c6c277320657965")
