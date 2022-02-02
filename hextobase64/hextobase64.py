import base64

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

byte_array = bytearray.fromhex(hex)
print(byte_array)
base64_value = base64.b64encode(byte_array)
print(base64_value)
