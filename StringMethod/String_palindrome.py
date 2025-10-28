# ------------------------------------------------------------
# Program: Palindrome Checker for Strings
# Author: [Your Name]
# Description:
#   This program checks whether a given string is a palindrome.
#   A palindrome reads the same forward and backward (e.g., "Madam", "Racecar").
#   It ignores spaces, punctuation, and case differences.
# ------------------------------------------------------------

# Take input from the user
s = input("Enter a string to check for palindrome: ")

# ------------------------------------------------------------
# Clean the input string:
#   - Convert to lowercase to make it case-insensitive
#   - Keep only alphanumeric characters (ignore spaces, commas, etc.)
# ------------------------------------------------------------
s1 = ''.join(c.lower() for c in s if c.isalnum())

# Reverse the cleaned string
a = s1[::-1]

# ------------------------------------------------------------
# Compare original cleaned string with its reverse
# ------------------------------------------------------------
if a == s1:
    print(" It is a palindrome!")
else:
    print(" Not a palindrome.")

# ------------------------------------------------------------
# Example Input / Output
# Input:  A man, a plan, a canal: Panama
# Output:  It is a palindrome!
#
# Input:  Hello World
# Output:  Not a palindrome.
# ------------------------------------------------------------
