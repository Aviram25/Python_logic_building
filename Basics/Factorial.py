# ------------------------------------------------------------
# Program: Generate Factorials from 0! to 10!
# Author: Aviram Dhagat
# Description:
#   This program calculates and prints the factorial of all
#   numbers from 0 to 10.
#   The factorial of a number n (written as n!) is the product
#   of all positive integers from 1 up to n.
#   Example: 5! = 1 × 2 × 3 × 4 × 5 = 120
# ------------------------------------------------------------

# Initialize variable to store factorial value
fact = 1

# Loop from 0 to 10 (inclusive)
for i in range(11):
    # For 0! and 1!, factorial is always 1
    if i < 2:
        fact = 1
    else:
        # Multiply the current factorial by i to get i!
        fact = fact * i

    # Display factorial in formatted style
    print(f"{i}! = {fact}")

# ------------------------------------------------------------
# Output Example:
# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# ...
# 10! = 3628800
# ------------------------------------------------------------
