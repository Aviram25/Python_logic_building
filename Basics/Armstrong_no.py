# ------------------------------------------
# Program: Check if a 3-digit number is an Armstrong number
# Author: [Your Name]
# Description:
#   An Armstrong number (also called a narcissistic number) is a number
#   that is equal to the sum of the cubes of its digits.
#   Example: 153 → 1³ + 5³ + 3³ = 153
# ------------------------------------------

# Take input from the user
n = int(input("Enter a 3-digit number: "))  # Example: 153

# Extract individual digits
b = n % 10          # Extracts the last digit → 3
c = n % 100         # Extracts the last two digits → 53
d = c // 10         # Extracts the middle digit → 5
e = n // 100        # Extracts the first digit → 1

# Check Armstrong condition:
# If the sum of the cubes of each digit equals the original number
if n == (b**3 + d**3 + e**3):
    print("Armstrong Number ")
else:
    print("Not an Armstrong Number ")


# ------------------------------------------
# Alternate approach (using loop) – works for any number of digits
# Uncomment below to test a more general version
# ------------------------------------------
"""
num = n             # Store original number
temp = 0            # Variable to hold the sum of cubes of digits

while n > 0:
    digit = n % 10              # Extract the last digit
    temp += digit ** 3          # Add cube of that digit
    n = n // 10                 # Remove last digit from n

# Compare the result with the original number
if temp == num:
    print("Armstrong Number ")
else:
    print("Not an Armstrong Number ")
"""
