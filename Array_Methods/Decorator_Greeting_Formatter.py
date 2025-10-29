# ------------------------------------------------------------
# Program: Decorator Greeting Formatter 
# Author: Aviram Dhagat
# Description:
#   This program demonstrates the use of a Python decorator to
#   modify the behavior of a function. Specifically, it converts
#   the input greeting to uppercase before printing it.
#
#   Example:
#     Input: "Aur bhai? Sab Badhiya?"
#     Output: "AUR BHAI? SAB BADHIYA?"
# ------------------------------------------------------------

# ------------------------------------------------------------
# Decorator: more_greet(inner)
#   Takes a function and returns a new function (wrapper)
#   that transforms the first argument to uppercase before
#   passing it to the original function.
# ------------------------------------------------------------
def more_greet(inner):
    def wrapper(*args):
        word = args[0]           # Extract the first argument
        word = word.upper()      # Convert it to uppercase
        return inner(word)       # Call the original function with modified input
    return wrapper

# ------------------------------------------------------------
# Function: display_greeting(word)
#   Prints the greeting message.
#   Decorated with @more_greet to ensure input is uppercased.
# ------------------------------------------------------------
@more_greet
def display_greeting(word):
    print(word)

# ------------------------------------------------------------
# Step 1: Call the decorated function with a casual greeting
# ------------------------------------------------------------
display_greeting("Aur bhai? Sab Badhiya?")  # Output: AUR BHAI? SAB BADHIYA?
