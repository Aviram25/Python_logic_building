# --------------------------------------------------------
# Program: Find Unique Element from a List of Family IDs
# Author: Aviram Dhagat
# Description:
#   Given a list of integers (family room numbers or IDs),
#   this program identifies and prints the element that 
#   occurs exactly once in the list.
#
#   It uses Python’s built-in `collections.Counter` 
#   for efficient frequency counting (O(N) time).
# --------------------------------------------------------

from collections import Counter   # Import Counter for fast element frequency counting

# Input the size of each group (not used directly but part of problem structure)
k = int(input("Enter the group size: "))

# Input list of family IDs or room numbers
families = list(map(int, input("Enter family IDs separated by space: ").split()))

# Create a Counter object → dictionary-like structure with {element: frequency}
count = Counter(families)

# Iterate through each element and its frequency
for key, value in count.items():
    # Print the element that appears exactly once
    if value == 1:
        print(f"Unique element (appears only once): {key}")
