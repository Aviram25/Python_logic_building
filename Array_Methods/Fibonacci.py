# ------------------------------------------------------------
# Program: Fibonacci Generator with Offset Yield 
# Author: Aviram Dhagat
# Description:
#   This program generates Fibonacci numbers using a generator
#   and yields the third-last number in the sequence at each step.
#
#   Note:
#     - The generator builds the Fibonacci sequence up to `num`
#     - It yields the value at position `i - 1` (i.e., l[-3])
#     - Only the first 5 yielded values are printed
# ------------------------------------------------------------

# ------------------------------------------------------------
# Function: fib(num)
#   Generates Fibonacci numbers and yields the third-last value
#   from the current list at each iteration.
# ------------------------------------------------------------
def fib(num):
    l = [0, 1]  # Initialize Fibonacci list with first two numbers
    for i in range(1, num + 1):
        l.append(l[i - 1] + l[i])  # Append next Fibonacci number
        temp = l[-3]               # Get the third-last element
        yield temp                 # Yield the offset Fibonacci value

# ------------------------------------------------------------
# Step 1: Create generator object for 10 Fibonacci steps
# ------------------------------------------------------------
res = fib(10)

# ------------------------------------------------------------
# Step 2: Print the first 5 yielded values from the generator
# ------------------------------------------------------------
for j in range(5):
    print(next(res))  # Output: 0, 1, 1, 2, 3
