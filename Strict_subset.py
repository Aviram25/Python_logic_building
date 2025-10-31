# ------------------------------------------------------------
# Program: Strict Subset Checker
# Author: Aviram Dhagat
# Description:
#   This program checks whether multiple sets (input by user)
#   are all *strict subsets* of a main set A.
#
#   A strict subset means:
#       Every element of the subset exists in the main set,
#       and the main set contains at least one extra element
#       not found in the subset.
#
#   If any subset fails this condition, the program prints False
#   immediately. Otherwise, it prints True at the end.
#
#   Example:
#       Input:
#           Main set: 1 2 3 4 5
#           Number of subsets: 2
#           Subset 1: 1 2 3
#           Subset 2: 2 5
#       Output:
#           True
# ------------------------------------------------------------

def strict_subset(a, num):
    """
    Function to check if 'num' is a strict subset of 'a'.
    
    Parameters:
        a (list): The main set.
        num (list): The subset to test.
        
    Returns:
        bool: True if all elements of 'num' exist in 'a',
              otherwise False.
    """
    for i in num:
        if i not in a:
            return False   # Found an element not present in main set
    return True             # All elements are present


# -------------------- INPUT SECTION --------------------

# Input main set A
set_a = list(map(int, input("Enter elements of the main set (A): ").split()))

# Number of subsets to check
n = int(input("Enter number of subsets to check: "))

# -------------------- PROCESSING -----------------------

# For each subset, verify if it is a strict subset of A
for i in range(n):
    num = list(map(int, input(f"Enter elements of subset {i+1}: ").split()))
    
    result = strict_subset(set_a, num)
    
    # If any subset fails, print False and stop checking further
    if result == False:
        print(False)
        break

# If all subsets are valid, print True
else:
    print(True)
