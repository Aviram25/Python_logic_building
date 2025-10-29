# ------------------------------------------------------------
# Program: Longest Word Finder 
# Author: Aviram Dhagat
# Description:
#   This program finds the longest word in a given list of strings.
#
#   Example:
#     Input: ["apple", "banana", "dragonfruit"]
#     Output: "dragonfruit"
# ------------------------------------------------------------

# ------------------------------------------------------------
# Function: find_longest_word(s)
#   Iterates through the list and keeps track of the longest word seen so far.
#   Compares each word's length with the current longest.
# ------------------------------------------------------------
def find_longest_word(s):
    temp = ""  # Temporary variable to store the longest word
    for i in s:
        if len(i) > len(temp):  # If current word is longer, update temp
            temp = i
    return temp  # Return the longest word found

# ------------------------------------------------------------
# Step 1: Define a sample list of words
# ------------------------------------------------------------
words = ["apple", "banana", "cherry", "dragonfruit",
         "elderberry", "fig", "grape"]

# ------------------------------------------------------------
# Step 2: Call the function and print the result
# ------------------------------------------------------------
res = find_longest_word(words)
print(res)  # Output: elderberry
