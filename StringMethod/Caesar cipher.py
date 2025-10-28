# ------------------------------------------------------------
# Program: Caesar Cipher (Shift by 3) – Decryption
# Author: Aviram Dhagat
# Description:
#   This program decrypts a message that was encoded using a
#   Caesar cipher with a right shift of 3 letters.
#
#   Example:
#     Encrypted Text: def
#     Decrypted Text: abc
#
#   The cipher mapping shifts each character forward by 3 positions.
#   Example Mapping: a → d, b → e, ..., x → a, y → b, z → c
# ------------------------------------------------------------

# Cipher dictionary (each letter shifted by +3)
cypher_text = {
    'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h',
    'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
    'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r',
    'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w',
    'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'
}

# ------------------------------------------------------------
# Step 1: Create reverse dictionary for decryption
#   This flips key-value pairs so we can decode back.
# ------------------------------------------------------------
decypher_text = {value: key for key, value in cypher_text.items()}

# ------------------------------------------------------------
# Step 2: Take encrypted text as input
# ------------------------------------------------------------
text = input("Enter encrypted text: ").lower()

# ------------------------------------------------------------
# Step 3: Decrypt each character using the reverse mapping
# ------------------------------------------------------------
decoded = ""
for char in text:
    # Decode only if charac
