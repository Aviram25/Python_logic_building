# ------------------------------------------------------------
# Program: Check if All Characters in a String Are Uppercase
# Author: Aviram Dhagat
# Description:
#   This program takes a string input and verifies whether all
#   alphabetic characters (ignoring spaces) are uppercase letters (A–Z).
# ------------------------------------------------------------

# Take input from user
n = input("Enter a string: ")

# Remove spaces for character checking
list1 = n.replace(' ', '')

# ------------------------------------------------------------
# Loop through each character and verify if it falls in A–Z range
# ASCII values:
#   'A' → 65
#   'Z' → 90
# So valid uppercase letters have ASCII codes between 65–90.
# ------------------------------------------------------------
for i in range(len(list1)):
    if list1[i] < chr(65) or list1[i] > chr(90):   # outside 'A'–'Z'
        print(" Not all characters are uppercase.")
        break
else:
    # This 'else' runs only if the loop completes without break
    print("All characters are uppercase!")

# -----------------
