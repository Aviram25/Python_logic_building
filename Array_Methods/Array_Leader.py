# ------------------------------------------------------------
# Program: Array Leader Finder 
# Author: Aviram Dhagat
# Description:
#   This script contains two approaches to identify "leaders" in an array.
#   A leader is an element that is greater than all elements to its right.
#
#   Example Input: [16, 17, 4, 3, 5, 2]
#   Expected Output: [17, 5, 2]
# ------------------------------------------------------------

# ------------------------------------------------------------
# Approach 1: Brute-force method using nested loops
#   For each element, check if any element to its right is greater.
#   If not, it's a leader and gets added to the result list.
# ------------------------------------------------------------

l = []  # List to store leaders
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i] < s[j]:  # If any element to the right is greater, break
            break
    else:
        l.append(s[i])  # If no greater element found, it's a leader
print(l)

# ------------------------------------------------------------
# Approach 2: Optimized reverse traversal method
#   Traverse the array from right to left, keeping track of the current leader.
#   If an element is greater than the current leader, it's added to the result.
# ------------------------------------------------------------

n = len(arr) - 1  # Last index of the array
x = []            # List to store leaders
leader = 0        # Initialize leader to 0 (or float('-inf') for general case)

for i in range(n, -1, -1):  # Traverse from end to start
    if arr[i] == leader:
        x.append(arr[i])    # Add if equal to current leader
        leader = arr[i]     # Update leader

    if arr[i] > leader:
        x.append(arr[i])    # Add if greater than current leader
        leader = arr[i]     # Update leader

x.reverse()  # Reverse to restore original order
return x     # Return the list of leaders
