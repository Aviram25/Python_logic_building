# ------------------------------------------------------------
# Program: Element-wise Summation of Multiple Tuples
# Author: Aviram Dhagat
# Description:
#   This program takes three tuples of equal length (t1, t2, t3)
#   and creates a new tuple where each element is the sum of
#   corresponding elements from all three tuples.
#
#   Example:
#       t1 = (1, 2, 3, 4)
#       t2 = (3, 5, 2, 1)
#       t3 = (2, 2, 3, 1)
#   Output: (6, 9, 8, 6)
# ------------------------------------------------------------

# Define the input tuples
t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

# ------------------------------------------------------------
# Step 1: Combine tuples element-wise using zip()
#   zip() pairs up elements from each tuple at the same index
#   Example: [(1,3,2), (2,5,2), (3,2,3), (4,1,1)]
# ------------------------------------------------------------
res = tuple(zip(t1, t2, t3))

# ------------------------------------------------------------
# Step 2: Sum the elements in each tuple to get element-wise totals
# ------------------------------------------------------------
a = (
    sum(res[0]),
    sum(res[1]),
    sum(res[2]),
    sum(res[3])
)

# ------------------------------------------------------------
# Step 3: Display the result
# ------------------------------------------------------------
print("Resultant tuple (element-wise sum):", a)

# ------------------------------------------------------------
# Output:
# Resultant tuple (element-wise sum): (6, 9, 8, 6)
# ------------------------------------------------------------
