# ------------------------------------------------------------
# Program: Analyze Digits of a Number
# Author: Aviram Dhagat
# Description:
#   This program takes an integer input and performs three analyses:
#     1. Counts total number of digits.
#     2. Calculates the sum of all digits.
#     3. Counts how many digits are even and how many are odd.
# ------------------------------------------------------------

# Take input from the user
num = int(input("Enter a number: "))

# Create copies of the number for multiple calculations
Num1 = num   # for sum of digits
Num2 = num   # for counting even and odd digits

# ------------------------------------------------------------
# PART 1 — Count the number of digits
# ------------------------------------------------------------
count = 0
while num > 0:
    num = num // 10       # Remove the last digit
    count += 1            # Increment digit counter
print(f"Total digits: {count}")

# ------------------------------------------------------------
# PART 2 — Find the sum of all digits
# ------------------------------------------------------------
temp = 0
while Num1 > 0:
    digit = Num1 % 10     # Extract last digit
    temp += digit         # Add it to sum
    Num1 = Num1 // 10     # Remove last digit
print(f"Sum of digits: {temp}")

# ------------------------------------------------------------
# PART 3 — Count even and odd digits
# ------------------------------------------------------------
even = 0
odd = 0
while Num2 > 0:
    digit = Num2 % 10     # Extract last digit
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    Num2 = Num2 // 10
print(f"Even digits: {even}, Odd digits: {odd}")

# ------------------------------------------------------------
# Example Input / Output
# Input:  12345
# Output:
#   Total digits: 5
#   Sum of digits: 15
#   Even digits: 2, Odd digits: 3
# ------------------------------------------------------------
