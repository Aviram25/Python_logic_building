# ------------------------------------------------------------
# Program: Subset Verification using Python
# Author: Aviram Dhagat
# Description:
#   This program checks whether one list (Set A) is a subset
#   of another list (Set B) for multiple test cases.
#
#   A subset means that *all elements of A* are contained in B.
#   The logic uses simple iteration and membership testing.
#
#   Time Complexity: O(n * m)
#       n = length of Set A
#       m = length of Set B
# ------------------------------------------------------------

def subset(a, b):
    """
    Function to check if list 'a' is a subset of list 'b'.
    
    Parameters:
        a (list): The first list (Set A)
        b (list): The second list (Set B)
        
    Returns:
        bool: True if all elements of 'a' exist in 'b', else False
    """
    for j in a:
        if j not in b:
            return False   # Return False if any element of A is missing in B
    else:
        return True        # Return True if loop completes without break


# Read number of test cases
t = int(input("Enter number of test cases: "))

# Process each test case
for i in range(t):
    # Input Set
