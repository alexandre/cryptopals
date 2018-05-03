"""

Convert hex to base64

The string:

49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
Cryptopals Rule

Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""

import base64


def convert_hex_to_ascii(hex_string: str) -> str:

    # String spplited into hex chunks of 2 characters
    hex_chunks = [hex_string[n: n + 2] for n in range(0, len(hex_string), 2)]

    return ''.join(chr(int(chunk, 16)) for chunk in hex_chunks)


def convert_ascii_to_base64(ascii_string: str) -> bytes:
    return base64.b64encode(ascii_string.encode())
