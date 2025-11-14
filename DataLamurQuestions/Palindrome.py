def isPalindrome(phrase):
    """
    Check if a phrase is a palindrome (reads same forwards and backwards)
    Ignores spaces, punctuation, and case
    
    Args:
        phrase: String to check
    
    Returns:
        True if palindrome, False otherwise
    """
    
    # Step 1: Create an empty string to store cleaned characters
    cleaned = ""
    
    # Step 2: Iterate through each character in the input phrase
    for char in phrase:
        # Check if character is alphanumeric (letter or number)
        # This filters out spaces, punctuation, and special characters
        if char.isalnum():
            # Add the lowercase version of the character to cleaned string
            # .lower() ensures case-insensitive comparison
            cleaned += char.lower()
    
    # Step 3: Compare cleaned string with its reverse
    # cleaned[::-1] reverses the string
    # If they're equal, it's a palindrome
    return cleaned == cleaned[::-1]


# Example usage with explanations:

# Example 1: "Taco cat"
# Step 1: cleaned = ""
# Step 2: Loop through each character:
#   'T' → isalnum? Yes → cleaned = "t"
#   'a' → isalnum? Yes → cleaned = "ta"
#   'c' → isalnum? Yes → cleaned = "tac"
#   'o' → isalnum? Yes → cleaned = "taco"
#   ' ' → isalnum? No → skip
#   'c' → isalnum? Yes → cleaned = "tacoc"
#   'a' → isalnum? Yes → cleaned = "tacoca"
#   't' → isalnum? Yes → cleaned = "tacocat"
# Step 3: "tacocat" == "tacocat"[::-1] → "tacocat" == "tacocat" → True

print(isPalindrome("Taco cat"))  # True

# Example 2: "A man, a plan, a canal: Panama"
# cleaned becomes: "amanaplanacanalpanama"
# reversed: "amanaplanacanalpanama"
# Equal? True
print(isPalindrome("A man, a plan, a canal: Panama"))  # True

# Example 3: "race a car"
# cleaned becomes: "raceacar"
# reversed: "racaecar"
# Equal? False
print(isPalindrome("race a car"))  # False
