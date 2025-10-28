# ------------------------------------------------------------
# Program: Print All Prime Numbers in a Given Range
# Author: [Your Name]
# Description:
#   This program takes a start and end value as input
#   and prints all prime numbers between them (inclusive).
#   A prime number is a number greater than 1 that is divisible
#   only by 1 and itself.
# ------------------------------------------------------------

# Take range input from the user
start = int(input("Enter the starting number: "))   # Example: 5
end = int(input("Enter the ending number: "))       # Example: 11

# Loop through each number in the given range
for i in range(start, end + 1):
    # Numbers less than 2 are not prime
    if i < 2:
        continue

    # Check divisibility from 2 to i-1
    for j in range(2, i):
        if i % j == 0:      # If divisible, not prime
            break
    else:
        # Executed only if the loop completes without a break
        print(i)

# ------------------------------------------------------------
# Example Input:
#   Enter the starting number: 5
#   Enter the ending number: 11
#
# Output:
#   5
#   7
#   11
# ------------------------------------------------------------
