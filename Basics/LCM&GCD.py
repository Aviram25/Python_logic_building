# ------------------------------------------------------------
# Program: Find GCD and LCM of Two Numbers
# Author: Aviram Dhagat
# Description:
#   This program calculates:
#     1. GCD (Greatest Common Divisor) — the largest number that divides both a and b.
#     2. LCM (Least Common Multiple) — the smallest number that is a multiple of both.
#
#   It uses simple loops to find both values.
# ------------------------------------------------------------

# Take input from the user
a = int(input("First number: "))
b = int(input("Second number: "))

# ------------------------------------------------------------
# PART 1 — Calculate GCD (Greatest Common Divisor)
# ------------------------------------------------------------
GCD = 1  # Initialize

# Loop through all possible divisors up to the smaller number
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        GCD = i  # Update when common divisor found

print(f"GCD (Greatest Common Divisor): {GCD}")

# ------------------------------------------------------------
# PART 2 — Calculate LCM (Least Common Multiple)
# ------------------------------------------------------------
# Initialize LCM as product of the two numbers
lcm = a * b

# Loop to find the smallest number divisible by both a and b
for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break  # Stop after finding first common multiple

print(f"LCM (Least Common Multiple): {lcm}")

# ------------------------------------------------------------
# Example Input / Output
# Input:
#   First number: 12
#   Second number: 18
# Output:
#   GCD (Greatest Common Divisor): 6
#   LCM (Least Common Multiple): 36
# ------------------------------------------------------------
