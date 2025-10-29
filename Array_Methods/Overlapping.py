# ------------------------------------------------------------
# Program: List Overlap Checker 
# Author: Aviram Dhagat
# Description:
#   This program checks whether two lists share any common elements.
#
#   Example:
#     l1 = [1, 2, 3]
#     l2 = [3, 4, 5]
#     Output: True (because 3 is common)
# ------------------------------------------------------------

# ------------------------------------------------------------
# Function: overlapping(l1, l2)
#   Returns True if any element in l1 is also in l2.
#   Uses Python's built-in 'any' function for concise logic.
#   (Commented-out version shows nested loop approach)
# ------------------------------------------------------------
def overlapping(l1, l2):
    # Brute-force version (commented out):
    # for i in l1:
    #     for j in l2:
    #         if i == j:
    #             return True
    # return False

    # Optimized version using generator expression
    return any(i in l2 for i in l1)

# ------------------------------------------------------------
# Step 1: Define two sample lists
# ------------------------------------------------------------
l1 = [1, 2, 3, 4, 5, 60]
l2 = [10, 20, 30, 40, 50, 60]

# ------------------------------------------------------------
# Step 2: Check for overlap and print result
# ------------------------------------------------------------
res = overlapping(l1, l2)
print(res)  # Output: True (since 60 is common)
